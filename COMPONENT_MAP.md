# SuperClaude Framework Component Map

Comprehensive navigation and cross-reference guide for the SuperClaude Framework v4.1.1 - a meta-programming configuration framework that transforms Claude Code into a structured development platform.

## 🏗️ Architecture Overview

```
SuperClaude Framework (Three-Layer Architecture)
├── Installation Layer (setup/) - Orchestration & deployment
├── Framework Layer (SuperClaude/) - Core components & behaviors
└── Distribution Layer - Multi-platform packaging
```

### Framework Statistics
| **Commands** | **Agents** | **Modes** | **MCP Servers** |
|:------------:|:----------:|:---------:|:---------------:|
| **24** | **14** | **6** | **6** |
| Slash Commands | Specialized AI | Behavioral | Integrations |

## 📂 Directory Structure

### Installation Layer (`setup/`)
```
setup/
├── cli/           → Command-line interface and argument parsing
├── core/          → Installation orchestration and dependency resolution
├── services/      → Backup management and configuration handling
├── utils/         → UI components, logging, validation
└── data/          → Configuration templates and manifests
```

### Framework Layer (`SuperClaude/`)
```
SuperClaude/
├── Commands/      → 24 slash commands (/sc: namespace)
├── Agents/        → 14 specialized AI personas
├── Modes/         → 6 behavioral modes
├── MCP/           → 6 server integrations
└── Core/          → Framework utilities and symbols
```

## 🎯 Component Navigation

### Commands (`/sc:` namespace)
| Command | Purpose | Dependencies |
|---------|---------|--------------|
| [`/sc:analyze`](SuperClaude/Commands/analyze.md) | Deep analysis with Sequential MCP | sequential |
| [`/sc:business-panel`](SuperClaude/Commands/business-panel.md) | Multi-expert strategic analysis | business-panel-experts |
| [`/sc:implement`](SuperClaude/Commands/implement.md) | Implementation with task management | task-management |
| [`/sc:help`](SuperClaude/Commands/help.md) | Comprehensive command documentation | - |
| [`/sc:load`](SuperClaude/Commands/load.md) | Project context loading | serena |
| [`/sc:save`](SuperClaude/Commands/save.md) | Session persistence | serena |
| [`/sc:index`](SuperClaude/Commands/index.md) | Project documentation generation | sequential, context7 |

### Agents (14 Specialized Personas)
| Category | Agents | Purpose |
|----------|---------|---------|
| **Architecture** | [backend-architect](SuperClaude/Agents/backend-architect.md), [frontend-architect](SuperClaude/Agents/frontend-architect.md), [system-architect](SuperClaude/Agents/system-architect.md) | System design |
| **Quality** | [security-engineer](SuperClaude/Agents/security-engineer.md), [quality-engineer](SuperClaude/Agents/quality-engineer.md), [performance-engineer](SuperClaude/Agents/performance-engineer.md) | Quality assurance |
| **Analysis** | [root-cause-analyst](SuperClaude/Agents/root-cause-analyst.md), [requirements-analyst](SuperClaude/Agents/requirements-analyst.md), [index-analyzer](SuperClaude/Agents/index-analyzer.md) | Investigation |
| **Development** | [python-expert](SuperClaude/Agents/python-expert.md), [refactoring-expert](SuperClaude/Agents/refactoring-expert.md), [devops-architect](SuperClaude/Agents/devops-architect.md) | Implementation |
| **Guidance** | [socratic-mentor](SuperClaude/Agents/socratic-mentor.md), [learning-guide](SuperClaude/Agents/learning-guide.md), [technical-writer](SuperClaude/Agents/technical-writer.md) | Education |
| **Business** | [business-panel-experts](SuperClaude/Agents/business-panel-experts.md) | Strategic analysis |

### Modes (6 Behavioral Adaptations)
| Mode | File | Triggers | Purpose |
|------|------|----------|---------|
| **Brainstorming** | [MODE_Brainstorming](SuperClaude/Modes/MODE_Brainstorming.md) | Vague requests, exploration | Requirements discovery |
| **Business Panel** | [MODE_Business_Panel](SuperClaude/Modes/MODE_Business_Panel.md) | Strategic analysis | 9-expert business analysis |
| **Introspection** | [MODE_Introspection](SuperClaude/Modes/MODE_Introspection.md) | Self-analysis, error recovery | Meta-cognitive analysis |
| **Orchestration** | [MODE_Orchestration](SuperClaude/Modes/MODE_Orchestration.md) | Multi-tool operations | Optimal task routing |
| **Task Management** | [MODE_Task_Management](SuperClaude/Modes/MODE_Task_Management.md) | Complex multi-step tasks | Hierarchical organization |
| **Token Efficiency** | [MODE_Token_Efficiency](SuperClaude/Modes/MODE_Token_Efficiency.md) | Resource constraints | 30-50% token reduction |

### MCP Servers (6 External Integrations)
| Server | File | Purpose | Best For |
|--------|------|---------|----------|
| **Context7** | [MCP_Context7](SuperClaude/MCP/MCP_Context7.md) | Library documentation | Official patterns |
| **Sequential** | [MCP_Sequential](SuperClaude/MCP/MCP_Sequential.md) | Complex reasoning | Multi-step analysis |
| **Magic** | [MCP_Magic](SuperClaude/MCP/MCP_Magic.md) | UI components | Modern frontend |
| **Playwright** | [MCP_Playwright](SuperClaude/MCP/MCP_Playwright.md) | Browser automation | E2E testing |
| **Morphllm** | [MCP_Morphllm](SuperClaude/MCP/MCP_Morphllm.md) | Pattern editing | Bulk transformations |
| **Serena** | [MCP_Serena](SuperClaude/MCP/MCP_Serena.md) | Project memory | Session persistence |

## 🧠 Business Panel System

### Expert Personas (9 Thought Leaders)
| Category | Experts | Frameworks |
|----------|---------|------------|
| **Strategic** | Porter, Kim/Mauborgne | Competitive strategy, Blue Ocean |
| **Innovation** | Christensen, Drucker, Godin | Disruption, management, marketing |
| **Excellence** | Collins, Taleb, Meadows | Good to Great, antifragility, systems |
| **Communication** | Doumont | Clarity and structure |

### Analysis Phases
1. **Discussion** → Collaborative multi-perspective analysis
2. **Debate** → Adversarial stress-testing
3. **Socratic** → Question-driven exploration

## 🎛️ Core Framework Components

### Behavioral Rules & Principles
| File | Purpose | Key Concepts |
|------|---------|--------------|
| [PRINCIPLES](SuperClaude/Core/PRINCIPLES.md) | Software engineering philosophy | SOLID, DRY, systems thinking |
| [RULES](SuperClaude/Core/RULES.md) | Behavioral rules with priorities | Quality standards, workflow patterns |
| [FLAGS](SuperClaude/Core/FLAGS.md) | Mode activation & control | Execution flags, MCP control |
| [BUSINESS_SYMBOLS](SuperClaude/Core/BUSINESS_SYMBOLS.md) | Symbol system | Business analysis notation |

## 🔗 Cross-References & Dependencies

### Component Relationships
```
Commands ──depends on──→ Agents (personas)
Commands ──depends on──→ MCP Servers
Commands ──activates──→ Modes
Modes ──uses──→ Core Components (symbols, rules)
Business Panel ──uses──→ Business Symbols & Examples
Installation ──deploys──→ All Framework Components
```

### Key Integration Points
- **YAML Frontmatter**: Commands declare dependencies
- **Mode Triggers**: Automatic activation based on context
- **MCP Integration**: Server selection matrix
- **Symbol Systems**: Unified notation across components

## 📚 Documentation Cross-Reference

### User Documentation
- [`Docs/User-Guide/commands.md`](Docs/User-Guide/commands.md) → All 24 commands
- [`Docs/User-Guide/agents.md`](Docs/User-Guide/agents.md) → 14 agents guide
- [`Docs/User-Guide/modes.md`](Docs/User-Guide/modes.md) → 6 modes explained
- [`Docs/User-Guide/mcp-servers.md`](Docs/User-Guide/mcp-servers.md) → Server integrations

### Developer Documentation
- [`Docs/Developer-Guide/technical-architecture.md`](Docs/Developer-Guide/technical-architecture.md) → System design
- [`CONTRIBUTING.md`](CONTRIBUTING.md) → Development workflow
- [`CLAUDE.md`](CLAUDE.md) → Project-specific instructions

### Configuration Files
- [`pyproject.toml`](pyproject.toml) → Python package config
- [`package.json`](package.json) → Node.js wrapper
- [`setup/data/requirements.json`](setup/data/requirements.json) → Dependencies

## 🚀 Quick Start Navigation

### For Users
1. [`README.md`](README.md) → Installation & overview
2. [`SuperClaude/Commands/help.md`](SuperClaude/Commands/help.md) → All commands
3. [`/sc:help`] → Interactive command reference

### For Developers
1. [`CONTRIBUTING.md`](CONTRIBUTING.md) → Development setup
2. [`Docs/Developer-Guide/`](Docs/Developer-Guide/) → Technical guides
3. [`setup/`](setup/) → Installation system

### For Framework Extension
1. [`SuperClaude/Commands/`](SuperClaude/Commands/) → Command patterns
2. [`SuperClaude/Agents/`](SuperClaude/Agents/) → Agent templates
3. [`SuperClaude/Core/`](SuperClaude/Core/) → Framework utilities

---

**📍 Navigation Tip**: Use this component map to quickly locate specific framework elements and understand their relationships within the SuperClaude ecosystem.