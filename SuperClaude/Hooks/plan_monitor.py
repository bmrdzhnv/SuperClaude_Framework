#!/usr/bin/env python3
"""
SuperClaude Plan Monitor Hook
Monitors for plan generation and offers execution options.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime


class PlanMonitor:
    """Monitor for SuperClaude plan generation and execution."""

    def __init__(self):
        self.plans_dir = Path.home() / ".claude" / "plans"
        self.plans_dir.mkdir(parents=True, exist_ok=True)
        self.config_file = Path.home() / ".claude" / "plan_config.json"
        self.load_config()

    def load_config(self):
        """Load plan monitoring configuration."""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                'auto_execute': False,
                'auto_save': True,
                'review_required': True,
                'max_complexity': 0.8
            }

    def save_config(self):
        """Save plan monitoring configuration."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def detect_plan_generation(self, result: dict) -> dict:
        """Detect if a plan was generated in the tool result."""
        # Look for indicators that a plan was generated
        if not result.get('tool') == 'Write':
            return None

        # Check if the file path indicates a plan
        file_path = result.get('file_path', '')
        if '/plans/' in file_path and file_path.endswith('.json'):
            try:
                with open(file_path, 'r') as f:
                    return json.load(f)
            except:
                pass

        # Check result content for plan structure
        content = result.get('content', '')
        if '"plan_id"' in content and '"steps"' in content:
            try:
                return json.loads(content)
            except:
                pass

        return None

    def analyze_plan(self, plan: dict) -> dict:
        """Analyze plan for complexity and safety."""
        analysis = {
            'complexity': plan.get('complexity', 0.5),
            'steps': len(plan.get('steps', [])),
            'has_rollback': bool(plan.get('rollback')),
            'estimated_time': self.estimate_time(plan),
            'risk_level': self.assess_risk(plan)
        }
        return analysis

    def estimate_time(self, plan: dict) -> int:
        """Estimate execution time in seconds."""
        # Simple estimation: 30 seconds per step
        return len(plan.get('steps', [])) * 30

    def assess_risk(self, plan: dict) -> str:
        """Assess risk level of plan execution."""
        complexity = plan.get('complexity', 0.5)
        has_rollback = bool(plan.get('rollback'))

        if complexity > 0.8:
            return 'high' if not has_rollback else 'medium'
        elif complexity > 0.5:
            return 'medium' if not has_rollback else 'low'
        else:
            return 'low'

    def save_plan(self, plan: dict) -> Path:
        """Save plan to plans directory."""
        plan_id = plan.get('plan_id', datetime.now().strftime('%Y%m%d_%H%M%S'))
        plan_file = self.plans_dir / f"{plan_id}.json"

        with open(plan_file, 'w') as f:
            json.dump(plan, f, indent=2)

        return plan_file

    def prompt_user_action(self, plan: dict, analysis: dict) -> str:
        """Prompt user for action on generated plan."""
        print("\n" + "="*50)
        print("📋 PLAN GENERATED")
        print("="*50)
        print(f"Goal: {plan.get('goal', 'Unknown')}")
        print(f"Steps: {analysis['steps']}")
        print(f"Complexity: {analysis['complexity']:.1f}")
        print(f"Est. Time: {analysis['estimated_time']}s")
        print(f"Risk: {analysis['risk_level']}")

        if self.config['auto_execute'] and analysis['complexity'] <= self.config['max_complexity']:
            print("\n🚀 Auto-execution enabled for this complexity level")
            return 'execute'

        print("\nOptions:")
        print("  [e] Execute plan now")
        print("  [r] Review plan details")
        print("  [s] Save for later")
        print("  [x] Skip (do nothing)")

        choice = input("\nChoose action [e/r/s/x]: ").lower()
        return choice

    def execute_plan(self, plan_file: Path):
        """Trigger plan execution."""
        print(f"\n▶️  Executing plan: {plan_file.name}")
        # Would trigger the execute-plan command here
        # For now, just print instructions
        print(f"Run: /execute-plan @{plan_file}")

    def review_plan(self, plan: dict):
        """Display detailed plan review."""
        print("\n" + "="*50)
        print("📋 PLAN DETAILS")
        print("="*50)

        for i, step in enumerate(plan.get('steps', []), 1):
            print(f"\nStep {i}:")
            print(f"  Command: {step.get('command')}")
            print(f"  Args: {step.get('args', 'none')}")
            if step.get('agents'):
                print(f"  Agents: {', '.join(step['agents'])}")
            if step.get('depends_on'):
                print(f"  Dependencies: {step['depends_on']}")
            if step.get('validation'):
                print(f"  Validation: {step['validation']}")

        if plan.get('rollback'):
            print("\nRollback Procedures:")
            for proc in plan['rollback']:
                print(f"  - {proc}")

    def process(self, event_type: str, data: dict):
        """Process hook event."""
        if event_type != 'post_tool_use':
            return

        # Check if a plan was generated
        plan = self.detect_plan_generation(data)
        if not plan:
            return

        # Analyze the plan
        analysis = self.analyze_plan(plan)

        # Save plan if configured
        if self.config['auto_save']:
            plan_file = self.save_plan(plan)
            print(f"\n💾 Plan saved: {plan_file.name}")
        else:
            plan_file = None

        # Get user action
        if self.config['review_required'] or analysis['risk_level'] == 'high':
            action = self.prompt_user_action(plan, analysis)

            if action == 'e':
                if plan_file:
                    self.execute_plan(plan_file)
                else:
                    plan_file = self.save_plan(plan)
                    self.execute_plan(plan_file)
            elif action == 'r':
                self.review_plan(plan)
                # Ask again after review
                retry = input("\nExecute now? [y/n]: ").lower()
                if retry == 'y':
                    if not plan_file:
                        plan_file = self.save_plan(plan)
                    self.execute_plan(plan_file)
            elif action == 's':
                if not plan_file:
                    plan_file = self.save_plan(plan)
                print(f"✅ Plan saved for later: {plan_file.name}")
            # else: skip


def handle_post_tool_use(result: dict):
    """Hook entry point for PostToolUse events."""
    monitor = PlanMonitor()
    monitor.process('post_tool_use', result)


def handle_user_prompt_submit(prompt: str) -> str:
    """Hook entry point for UserPromptSubmit events."""
    # Intercept execution requests
    if prompt.strip().startswith('/execute-plan'):
        # Could modify or enhance the execution request here
        pass
    return prompt


# Entry point for hook system
if __name__ == '__main__':
    # This would be called by the hook system
    # For testing, simulate a plan generation
    test_plan = {
        'plan_id': 'test_plan',
        'goal': 'Test plan execution',
        'complexity': 0.5,
        'steps': [
            {
                'command': '/sc:analyze',
                'args': 'test.js',
                'agents': ['quality-engineer']
            }
        ],
        'rollback': ['git reset --hard']
    }

    monitor = PlanMonitor()
    analysis = monitor.analyze_plan(test_plan)
    action = monitor.prompt_user_action(test_plan, analysis)
    print(f"\nAction selected: {action}")