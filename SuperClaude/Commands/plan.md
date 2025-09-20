---
name: plan
description: "Generate executable development plans using meta-agent orchestration"
category: orchestration
complexity: advanced
mcp-servers: [sequential]
personas: [computational-strategist, superclaude-framework]
---

# /sc:plan - Intelligent Plan Generation & Execution

Bridge natural language requests to executable SuperClaude workflows through meta-agent orchestration.

## Usage
```
/sc:plan "request" [--execute] [--save name] [--review] [--dry-run]
```

## Purpose: Transform Intent into Action

Users describe **what** they want, meta-agents determine **how** to achieve it.

## How It Works

### Phase 1: Path Analysis
**Computational-Strategist finds optimal command sequence**
- Applies graph theory (SSSP) to command space
- Identifies shortest path through SuperClaude capabilities
- Outputs structured efficiency cookbook

### Phase 2: Orchestration Design
**SuperClaude-Framework enriches execution details**
- Maps required agents and specialists
- Adds flags, MCP servers, and dependencies
- Structures validation and rollback procedures

### Phase 3: Plan Generation
**Creates executable JSON plan**
```json
{
  "plan_id": "generated_id",
  "goal": "user_request",
  "complexity": 0.0-1.0,
  "steps": [
    {
      "command": "/sc:command",
      "args": "arguments",
      "agents": ["required-agents"],
      "validation": "success_criteria"
    }
  ]
}
```

### Phase 4: Execution Options
- **Review Mode** (default): Display plan for user approval
- **Execute Mode** (--execute): Run immediately after generation
- **Save Mode** (--save): Store for later execution
- **Dry Run** (--dry-run): Simulate without actual execution

## Usage Patterns

### Interactive Planning
```bash
# Generate and review before execution
/sc:plan "build React authentication system"
# → Shows detailed plan
# → User reviews steps
# → Confirms execution
```

### Automated Execution
```bash
# Generate and execute immediately
/sc:plan "refactor auth.js for better security" --execute
# → Generates plan
# → Validates safety
# → Executes steps
```

### Template Creation
```bash
# Save plan for reuse
/sc:plan "standard API endpoint setup" --save api-template
# → Generates reusable plan
# → Stores in ~/.claude/plans/
```

## Plan Structure

### Metadata Layer
- Goal statement and success criteria
- Complexity score (0.0-1.0)
- Estimated execution time
- Resource requirements

### Execution Layer
- Sequential command steps
- Parallel execution opportunities
- Agent and MCP server assignments
- Validation checkpoints

### Safety Layer
- Rollback procedures
- Error recovery strategies
- State preservation points
- Manual intervention hooks

## Integration Points

### Meta-Agent Coordination
```yaml
computational-strategist:
  role: "Find optimal command path"
  output: "Efficiency cookbook with rationale"

superclaude-framework:
  role: "Orchestrate framework resources"
  output: "Enriched execution details"
```

### Execution Mechanisms
```yaml
custom_command:
  location: ~/.claude/commands/execute-plan.md
  trigger: "/execute-plan plan-id"

monitoring_hook:
  location: ~/.claude/hooks/plan-monitor.py
  events: [PostToolUse, UserPromptSubmit]
```

## Examples

### Complex Development Task
```bash
/sc:plan "migrate legacy jQuery app to React with TypeScript"
# Generates comprehensive migration plan:
# 1. /sc:analyze - Assess current codebase
# 2. /sc:research - React migration patterns
# 3. /sc:design - Component architecture
# 4. /sc:implement - Incremental migration
# 5. /sc:test - Validation suite
# 6. /sc:document - Migration guide
```

### Security Improvement
```bash
/sc:plan "audit and fix authentication vulnerabilities" --execute
# Auto-executes security workflow:
# 1. /sc:analyze --focus security
# 2. /sc:brainstorm @security-engineer
# 3. /sc:implement security-fixes
# 4. /sc:test security-suite
```

### Learning Workflow
```bash
/sc:plan "teach me React hooks progressively"
# Creates educational plan:
# 1. /sc:research React hooks basics
# 2. /sc:explain @learning-guide useState
# 3. /sc:implement simple-examples
# 4. /sc:explain @learning-guide useEffect
# 5. /sc:implement complex-examples
```

## Validation & Safety

### Pre-Execution Checks
- Validate all commands exist
- Check agent availability
- Verify file permissions
- Assess risk level

### During Execution
- Progress tracking via TodoWrite
- State checkpoints after each step
- Error detection and recovery
- User interrupt handling

### Post-Execution
- Success validation
- Cleanup temporary resources
- Generate execution report
- Update plan templates

## Advanced Features

### Conditional Logic
Plans support conditional execution:
```json
{
  "condition": "if tests pass",
  "then": "/sc:deploy",
  "else": "/sc:debug"
}
```

### Parallel Execution
Identifies independent steps:
```json
{
  "parallel": [
    "/sc:test frontend",
    "/sc:test backend",
    "/sc:analyze performance"
  ]
}
```

### Plan Composition
Combine smaller plans:
```bash
/sc:plan "full stack feature" --compose auth-plan api-plan ui-plan
```

## Output Format

```
🎯 Plan: [Goal Statement]
📊 Complexity: 0.7 | ⏱️ Est. Time: 45 min

📋 Steps:
1. /sc:research "React patterns"
   → Agents: frontend-architect
   → Output: Documentation stored

2. /sc:design component-architecture
   → Agents: system-architect
   → Dependencies: Step 1

3. /sc:implement components --validated
   → Agents: frontend-architect, quality-engineer
   → Validation: Tests pass

💾 Save as: feature_plan_2024.json
✅ Ready to execute? [Y/n]
```

## Error Handling

### Known Limitations
- Cannot execute system commands directly
- Requires user confirmation for destructive operations
- Limited to SuperClaude command vocabulary

### Recovery Strategies
- Automatic rollback on critical failures
- State preservation for manual recovery
- Alternative path suggestions
- Graceful degradation options