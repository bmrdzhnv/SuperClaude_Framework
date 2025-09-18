# SuperClaude Framework Cross-Reference Matrix

## Command → Agent Relationships

### Direct Command-Agent Dependencies
| Command | Primary Agents | Secondary Agents |
|---------|---------------|------------------|
| `/sc:analyze` | - | system-architect, root-cause-analyst |
| `/sc:build` | backend-architect | devops-architect |
| `/sc:business-panel` | business-panel-experts | - |
| `/sc:design` | system-architect | frontend-architect, backend-architect |
| `/sc:document` | technical-writer | - |
| `/sc:implement` | backend-architect | python-expert, frontend-architect |
| `/sc:improve` | refactoring-expert | performance-engineer |
| `/sc:spec-panel` | requirements-analyst | - |
| `/sc:test` | quality-engineer | security-engineer |
| `/sc:troubleshoot` | root-cause-analyst | performance-engineer |
| `/sc:explain` | learning-guide | socratic-mentor |

## Command → Mode Activation

### Mode Trigger Patterns
| Mode | Triggering Commands | Auto-Activation Context |
|------|-------------------|------------------------|
| **Brainstorming** | `/sc:brainstorm` | Vague requests, exploration keywords |
| **Business Panel** | `/sc:business-panel` | Strategic documents, business analysis |
| **Introspection** | `/sc:reflect` | Error recovery, self-analysis requests |
| **Orchestration** | `/sc:select-tool` | Multi-tool operations, >3 files |
| **Task Management** | `/sc:task`, `/sc:implement`, `/sc:build` | >3 steps, complex scope |
| **Token Efficiency** | All commands with `--uc` | Context >75%, resource constraints |

## Command → MCP Server Usage

### Primary MCP Integration
| Command | Context7 | Sequential | Magic | Morphllm | Playwright | Serena |
|---------|----------|------------|-------|----------|------------|--------|
| `/sc:analyze` | ✓ | ✓ | | | | |
| `/sc:business-panel` | | ✓ | | | | |
| `/sc:design` | ✓ | ✓ | | | | |
| `/sc:document` | ✓ | | | | | |
| `/sc:implement` | ✓ | | ✓ | | | |
| `/sc:improve` | | | | ✓ | | |
| `/sc:index` | ✓ | ✓ | | | | |
| `/sc:load` | | | | | | ✓ |
| `/sc:save` | | | | | | ✓ |
| `/sc:test` | | | | | ✓ | |

## Agent → Mode Relationships

### Agent Mode Preferences
| Agent | Primary Modes | Activation Context |
|-------|--------------|-------------------|
| **backend-architect** | Task Management, Orchestration | Implementation tasks |
| **business-panel-experts** | Business Panel | Strategic analysis |
| **frontend-architect** | Orchestration, Token Efficiency | UI development |
| **learning-guide** | Brainstorming, Introspection | Educational contexts |
| **performance-engineer** | Orchestration, Token Efficiency | Optimization tasks |
| **python-expert** | Task Management | Python development |
| **quality-engineer** | Task Management, Orchestration | Testing workflows |
| **refactoring-expert** | Token Efficiency, Orchestration | Code improvements |
| **requirements-analyst** | Brainstorming, Business Panel | Specification work |
| **root-cause-analyst** | Introspection, Task Management | Debugging |
| **security-engineer** | Orchestration | Security audits |
| **socratic-mentor** | Brainstorming, Introspection | Learning sessions |
| **system-architect** | Task Management, Orchestration | Design work |
| **technical-writer** | Token Efficiency | Documentation |

## Mode → MCP Server Preferences

### Optimal MCP Selection by Mode
| Mode | Preferred MCP Servers | Usage Pattern |
|------|---------------------|---------------|
| **Brainstorming** | Context7 | Documentation lookup for ideas |
| **Business Panel** | Sequential | Multi-expert coordination |
| **Introspection** | Sequential | Meta-cognitive analysis |
| **Orchestration** | All servers | Optimal tool selection |
| **Task Management** | Serena | Memory persistence |
| **Token Efficiency** | Morphllm | Compressed operations |

## Workflow Patterns

### Common Command Sequences
```
1. Discovery → Implementation → Testing
   /sc:brainstorm → /sc:design → /sc:implement → /sc:test

2. Analysis → Improvement → Documentation
   /sc:analyze → /sc:improve → /sc:document

3. Session Management
   /sc:load → [work commands] → /sc:save

4. Problem Solving
   /sc:troubleshoot → /sc:analyze → /sc:implement → /sc:test

5. Business Strategy
   /sc:business-panel → /sc:spec-panel → /sc:design → /sc:estimate
```

### Agent Collaboration Patterns
```
1. Full Stack Development
   system-architect → backend-architect + frontend-architect → devops-architect

2. Quality Assurance
   quality-engineer + security-engineer → performance-engineer

3. Requirements to Implementation
   requirements-analyst → system-architect → python-expert

4. Learning Path
   socratic-mentor → learning-guide → technical-writer

5. Optimization Workflow
   root-cause-analyst → performance-engineer → refactoring-expert
```

## Dependency Chains

### Command Dependency Tree
```
/sc:workflow
├── /sc:design (planning)
├── /sc:implement (execution)
│   ├── /sc:build
│   └── /sc:test
└── /sc:document (finalization)

/sc:improve
├── /sc:analyze (assessment)
├── /sc:troubleshoot (issues)
└── /sc:test (validation)

/sc:business-panel
├── /sc:spec-panel (requirements)
├── /sc:estimate (planning)
└── /sc:design (architecture)
```

### Mode Activation Cascade
```
Complex Task Request
├── Task Management (>3 steps detected)
│   ├── Orchestration (multi-tool needed)
│   └── Token Efficiency (context pressure)
└── Introspection (complexity requires meta-analysis)

Vague Request
├── Brainstorming (exploration needed)
│   ├── Business Panel (if strategic)
│   └── Task Management (once clarified)
```

## Tool Selection Matrix

### Task Type → Optimal Tool Chain
| Task Type | Primary Tool | Secondary Tools | Agent Support | MCP Usage |
|-----------|-------------|-----------------|---------------|-----------|
| **UI Development** | Magic MCP | Context7 | frontend-architect | Magic + Context7 |
| **API Design** | Design cmd | Sequential | backend-architect | Sequential + Context7 |
| **Bug Fixing** | Troubleshoot | Analyze | root-cause-analyst | Sequential |
| **Refactoring** | Improve | MultiEdit | refactoring-expert | Morphllm |
| **Documentation** | Document | Index | technical-writer | Context7 |
| **Testing** | Test cmd | Playwright | quality-engineer | Playwright |
| **Architecture** | Design cmd | Sequential | system-architect | Sequential |
| **Performance** | Analyze | Improve | performance-engineer | Sequential |

## Integration Points

### Critical Integration Paths
```
1. Session Persistence
   Serena MCP ← → /sc:load + /sc:save ← → Task Management Mode

2. Business Analysis
   Business Panel Mode ← → Sequential MCP ← → Business Experts

3. Code Quality
   Refactoring Expert ← → Morphllm MCP ← → Token Efficiency Mode

4. UI Components
   Frontend Architect ← → Magic MCP ← → Context7 MCP

5. Testing Pipeline
   Quality Engineer ← → Playwright MCP ← → Test Command
```

### Cross-Component Communication
| Component A | Component B | Communication Method | Data Flow |
|------------|------------|---------------------|-----------|
| Commands | Agents | YAML frontmatter | Dependencies |
| Commands | Modes | Trigger patterns | Activation |
| Commands | MCP | Direct invocation | Tool usage |
| Agents | Modes | Context analysis | Behavior |
| Modes | MCP | Preference matrix | Selection |
| MCP | MCP | Orchestration | Coordination |

## Conflict Resolution

### Priority Rules
1. **Command Override**: Explicit command flags override auto-detection
2. **Safety First**: Security/quality agents override speed optimizations
3. **Mode Hierarchy**: Task Management > Orchestration > Token Efficiency
4. **MCP Fallback**: Native tools if MCP unavailable
5. **Agent Precedence**: Domain expert > generalist for specific tasks

### Incompatible Combinations
| Component 1 | Component 2 | Reason | Resolution |
|------------|-------------|---------|------------|
| Token Efficiency | Introspection | Opposing goals | Introspection wins |
| Brainstorming | Token Efficiency | Discovery needs space | Brainstorming wins |
| Multiple primary agents | Single task | Role conflict | First declared wins |
| Serena + Morphllm | Same operation | Different approaches | Task-specific choice |

## Performance Optimization

### Parallel Execution Opportunities
| Scenario | Parallel Operations | Coordination |
|----------|-------------------|--------------|
| Multi-file analysis | Read operations | Batch with Glob |
| Cross-component docs | Multiple Writes | TodoWrite tracking |
| Test suite | Independent tests | Playwright parallel |
| Bulk refactoring | Pattern applications | Morphllm batch |
| Documentation | Section generation | Task agent delegation |

### Token Budget Allocation
| Operation Type | Token Range | Optimization Strategy |
|---------------|-------------|----------------------|
| Simple command | 1-3K | Direct execution |
| Analysis | 4-10K | Sequential for depth |
| Business Panel | 15-30K | Phase-based control |
| Complex workflow | 30-50K | Task delegation |
| Ultrathink | 50K+ | Multi-agent parallel |

---

*This cross-reference matrix maps the relationships and dependencies between all SuperClaude Framework components, enabling efficient navigation and understanding of the system's interconnected architecture.*