#!/usr/bin/env python3
"""
SuperClaude Plan Executor v2 - State Machine Pattern
Orchestrates execution of compiled plans with atomic operations.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, Optional, List
from enum import Enum
from dataclasses import dataclass


class StepType(Enum):
    """Types of atomic operations in compiled plans."""
    ATOMIC_TOOL = "atomic_tool"     # Direct tool call (Read, Write, etc.)
    MCP_CALL = "mcp_call"           # MCP server function call
    THINK = "think"                  # Main Claude reasoning
    BASH = "bash"                    # Shell command execution


@dataclass
class ExecutionContext:
    """Maintains execution state across steps."""
    plan_id: str
    current_step: int = 0
    state: Dict[str, Any] = None
    completed_steps: List[str] = None
    failed_steps: List[str] = None

    def __post_init__(self):
        if self.state is None:
            self.state = {}
        if self.completed_steps is None:
            self.completed_steps = []
        if self.failed_steps is None:
            self.failed_steps = []


class CompiledPlanExecutor:
    """
    State machine executor for compiled plans.
    Returns instructions for main Claude to execute.
    """

    def __init__(self, plan_path: Path):
        self.plan_path = plan_path
        self.plan = self._load_plan()
        self.context = ExecutionContext(
            plan_id=self.plan.get('plan_id', 'unknown')
        )

    def _load_plan(self) -> Dict[str, Any]:
        """Load compiled plan from JSON."""
        with open(self.plan_path, 'r') as f:
            plan = json.load(f)

        # Validate it's a compiled plan
        if plan.get('compilation_version') != '2.0':
            raise ValueError("This executor requires compiled plans (v2.0)")

        return plan

    def _resolve_variables(self, text: str) -> str:
        """Replace {{variable}} references with actual values from state."""
        def replace_var(match):
            var_path = match.group(1)

            # Handle nested paths like auth_files[0]
            if '[' in var_path:
                base, index = var_path.split('[')
                index = int(index.rstrip(']'))
                value = self.context.state.get(base, [])
                return str(value[index]) if index < len(value) else ''

            return str(self.context.state.get(var_path, ''))

        return re.sub(r'\{\{([^}]+)\}\}', replace_var, text)

    def get_next_instruction(self) -> Dict[str, Any]:
        """
        Get the next atomic operation for main Claude to execute.

        Returns:
            Dictionary with instruction details or completion status.
        """
        if self.context.current_step >= len(self.plan['steps']):
            return {
                "status": "complete",
                "message": "All steps executed successfully",
                "results": self.context.state
            }

        step = self.plan['steps'][self.context.current_step]
        step_type = StepType(step['type'])

        # Build instruction based on step type
        instruction = {
            "step_id": step['step_id'],
            "description": step['description'],
            "type": step_type.value
        }

        if step_type == StepType.ATOMIC_TOOL:
            instruction["action"] = "execute_tool"
            instruction["tool"] = step['tool']
            instruction["params"] = self._resolve_variables(
                json.dumps(step['params'])
            )
            instruction["params"] = json.loads(instruction["params"])

        elif step_type == StepType.MCP_CALL:
            instruction["action"] = "call_mcp"
            instruction["server"] = step['mcp_server']
            instruction["function"] = step['function']
            instruction["params"] = self._resolve_variables(
                json.dumps(step['params'])
            )
            instruction["params"] = json.loads(instruction["params"])

        elif step_type == StepType.THINK:
            instruction["action"] = "think"
            instruction["prompt"] = self._resolve_variables(step['prompt'])

        elif step_type == StepType.BASH:
            instruction["action"] = "bash"
            instruction["command"] = self._resolve_variables(step['command'])

        return instruction

    def record_result(self, step_id: str, result: Any, success: bool = True):
        """
        Record the result of an executed step.

        Args:
            step_id: The ID of the completed step
            result: The execution result
            success: Whether the step succeeded
        """
        current_step = self.plan['steps'][self.context.current_step]

        if success:
            # Store result if step specifies storage
            if 'store_as' in current_step:
                self.context.state[current_step['store_as']] = result

            self.context.completed_steps.append(step_id)
            self.context.current_step += 1
        else:
            self.context.failed_steps.append(step_id)
            # Could trigger rollback here

    def get_status(self) -> Dict[str, Any]:
        """Get current execution status."""
        total_steps = len(self.plan['steps'])
        return {
            "plan_id": self.context.plan_id,
            "progress": f"{self.context.current_step}/{total_steps}",
            "completed": self.context.completed_steps,
            "failed": self.context.failed_steps,
            "current_state": list(self.context.state.keys())
        }

    def needs_rollback(self) -> bool:
        """Check if rollback is needed."""
        return len(self.context.failed_steps) > 0

    def get_rollback_instructions(self) -> List[str]:
        """Get rollback commands if defined."""
        return self.plan.get('rollback', [])


def main():
    """Example usage for testing."""
    import sys

    if len(sys.argv) != 2:
        print("Usage: plan_executor_v2.py <plan.json>")
        sys.exit(1)

    plan_path = Path(sys.argv[1])
    executor = CompiledPlanExecutor(plan_path)

    print(f"📋 Loaded plan: {executor.plan['goal']}")
    print(f"   Steps: {len(executor.plan['steps'])}")

    # Simulate execution loop
    while True:
        instruction = executor.get_next_instruction()

        if instruction.get('status') == 'complete':
            print("\n✅ Plan execution complete!")
            break

        print(f"\n▶️  Step {instruction['step_id']}: {instruction['description']}")
        print(f"   Action: {instruction.get('action', 'unknown')}")

        # In real usage, main Claude would execute here
        # For testing, just mark as complete
        executor.record_result(instruction['step_id'], "simulated_result")

    print("\nFinal Status:")
    print(json.dumps(executor.get_status(), indent=2))


if __name__ == "__main__":
    main()