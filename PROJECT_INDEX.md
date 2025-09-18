# SuperClaude Framework Project Index

## Project Overview
**Name**: SuperClaude Framework
**Version**: 4.1.1
**Description**: Meta-programming configuration framework that transforms Claude Code into a structured development platform through behavioral instruction injection
**Repository**: https://github.com/SuperClaude-Org/SuperClaude_Framework
**License**: MIT

## Quick Access
- [Installation](#installation)
- [Commands Reference](#commands-reference-24)
- [Agents Directory](#agents-directory-14)
- [Behavioral Modes](#behavioral-modes-6)
- [MCP Servers](#mcp-server-integrations-6)
- [Core Components](#core-framework-components)
- [Architecture](#technical-architecture)
- [Development](#development-workflow)

## Installation

### Primary Methods
```bash
# Recommended: pipx (Linux/macOS)
pipx install SuperClaude && pipx upgrade SuperClaude && SuperClaude install

# Alternative: pip
pip install SuperClaude && pip upgrade SuperClaude && SuperClaude install

# Cross-platform: npm
npm install -g @bifrost_inc/superclaude && superclaude install
```

### Installation Target
- **Location**: `~/.claude/`
- **Preserves**: Custom commands, CLAUDE.md content, settings
- **Backs up**: Existing installation before updates

## Commands Reference (24)

### Engineering Commands
| Command | Purpose | Key Dependencies | Complexity |
|---------|---------|-----------------|------------|
| `/sc:analyze` | Deep code analysis with reasoning | sequential, context7 | Advanced |
| `/sc:build` | Orchestrated build workflows | task-management | Intermediate |
| `/sc:design` | System design with patterns | sequential, architect | Advanced |
| `/sc:document` | Documentation generation | technical-writer | Intermediate |
| `/sc:git` | Git workflow orchestration | - | Basic |
| `/sc:implement` | Feature implementation | backend-architect | Intermediate |
| `/sc:improve` | Code enhancement | refactoring-expert | Intermediate |
| `/sc:test` | Testing strategy and execution | quality-engineer | Intermediate |
| `/sc:troubleshoot` | Problem investigation | root-cause-analyst | Advanced |
| `/sc:workflow` | Custom workflow definition | - | Advanced |

### Utility Commands
| Command | Purpose | Key Dependencies | Complexity |
|---------|---------|-----------------|------------|
| `/sc:brainstorm` | Requirements discovery | - | Basic |
| `/sc:cleanup` | Workspace hygiene | - | Basic |
| `/sc:estimate` | Effort estimation | - | Basic |
| `/sc:help` | Command reference | - | Basic |
| `/sc:index` | Project documentation | sequential, context7 | Intermediate |
| `/sc:load` | Session context loading | serena | Basic |
| `/sc:reflect` | Meta-cognitive analysis | introspection | Advanced |
| `/sc:research` | Technical investigation | - | Intermediate |
| `/sc:save` | Session persistence | serena | Basic |
| `/sc:select-tool` | Tool optimization | orchestration | Intermediate |
| `/sc:spawn` | Sub-agent creation | - | Advanced |
| `/sc:task` | Task orchestration | task-management | Intermediate |

### Business Commands
| Command | Purpose | Key Dependencies | Complexity |
|---------|---------|-----------------|------------|
| `/sc:business-panel` | Multi-expert analysis | sequential, business-experts | Advanced |
| `/sc:spec-panel` | Specification analysis | requirements-analyst | Intermediate |

### Educational Commands
| Command | Purpose | Key Dependencies | Complexity |
|---------|---------|-----------------|------------|
| `/sc:explain` | Code explanation | learning-guide | Basic |

## Agents Directory (14)

### Architecture Specialists
- **[backend-architect](SuperClaude/Agents/backend-architect.md)**: Backend systems, data integrity, fault tolerance
- **[frontend-architect](SuperClaude/Agents/frontend-architect.md)**: UI/UX, accessibility, performance
- **[system-architect](SuperClaude/Agents/system-architect.md)**: Scalability, maintainability, architecture
- **[devops-architect](SuperClaude/Agents/devops-architect.md)**: Infrastructure, deployment, observability

### Quality & Security
- **[security-engineer](SuperClaude/Agents/security-engineer.md)**: Vulnerability identification, compliance
- **[quality-engineer](SuperClaude/Agents/quality-engineer.md)**: Testing strategies, edge cases
- **[performance-engineer](SuperClaude/Agents/performance-engineer.md)**: Optimization, bottlenecks

### Analysis & Investigation
- **[root-cause-analyst](SuperClaude/Agents/root-cause-analyst.md)**: Problem investigation, hypothesis testing
- **[requirements-analyst](SuperClaude/Agents/requirements-analyst.md)**: Requirements discovery, structured analysis

### Development & Code Quality
- **[python-expert](SuperClaude/Agents/python-expert.md)**: SOLID principles, production-ready Python
- **[refactoring-expert](SuperClaude/Agents/refactoring-expert.md)**: Technical debt, clean code

### Education & Documentation
- **[socratic-mentor](SuperClaude/Agents/socratic-mentor.md)**: Discovery learning, strategic questioning
- **[learning-guide](SuperClaude/Agents/learning-guide.md)**: Progressive learning, practical examples
- **[technical-writer](SuperClaude/Agents/technical-writer.md)**: Clear documentation, audience tailoring

### Business Strategy
- **[business-panel-experts](SuperClaude/Agents/business-panel-experts.md)**: 9 thought leaders for strategic analysis

## Behavioral Modes (6)

| Mode | Activation Triggers | Key Behaviors | Token Impact |
|------|-------------------|---------------|--------------|
| **[Brainstorming](SuperClaude/Modes/MODE_Brainstorming.md)** | Vague requests, "maybe", "explore" | Socratic dialogue, requirement elicitation | Normal |
| **[Business Panel](SuperClaude/Modes/MODE_Business_Panel.md)** | `/sc:business-panel`, strategic docs | 9-expert analysis, three-phase interaction | 15-30K tokens |
| **[Introspection](SuperClaude/Modes/MODE_Introspection.md)** | Self-analysis, error recovery | Meta-cognitive transparency (🤔 🎯 ⚡ 📊 💡) | Normal |
| **[Orchestration](SuperClaude/Modes/MODE_Orchestration.md)** | Multi-tool operations, >75% resources | Optimal tool routing, parallel execution | Reduced |
| **[Task Management](SuperClaude/Modes/MODE_Task_Management.md)** | >3 steps, complex scope | Hierarchical organization, TodoWrite + memory | Normal |
| **[Token Efficiency](SuperClaude/Modes/MODE_Token_Efficiency.md)** | Context >75%, `--uc` flag | Symbol communication, 30-50% reduction | -30-50% |

## MCP Server Integrations (6)

### Documentation & Analysis
| Server | Purpose | Best For | Config |
|--------|---------|----------|---------|
| **[Context7](SuperClaude/MCP/MCP_Context7.md)** | Library documentation | Official patterns, version-specific docs | [context7.json](SuperClaude/MCP/configs/context7.json) |
| **[Sequential](SuperClaude/MCP/MCP_Sequential.md)** | Complex reasoning | Multi-step analysis, hypothesis testing | [sequential.json](SuperClaude/MCP/configs/sequential.json) |

### Development Tools
| Server | Purpose | Best For | Config |
|--------|---------|----------|---------|
| **[Magic](SuperClaude/MCP/MCP_Magic.md)** | UI generation | Modern components from 21st.dev | [magic.json](SuperClaude/MCP/configs/magic.json) |
| **[Morphllm](SuperClaude/MCP/MCP_Morphllm.md)** | Pattern editing | Bulk transformations, refactoring | [morphllm.json](SuperClaude/MCP/configs/morphllm.json) |

### Testing & Persistence
| Server | Purpose | Best For | Config |
|--------|---------|----------|---------|
| **[Playwright](SuperClaude/MCP/MCP_Playwright.md)** | Browser automation | E2E testing, accessibility | [playwright.json](SuperClaude/MCP/configs/playwright.json) |
| **[Serena](SuperClaude/MCP/MCP_Serena.md)** | Project memory | Session persistence, symbol operations | [serena.json](SuperClaude/MCP/configs/serena.json) |

### Additional Servers (Experimental)
- **[Exa](SuperClaude/MCP/MCP_Exa.md)**: Advanced search capabilities
- **[Crawl4ai](SuperClaude/MCP/MCP_Crawl4ai.md)**: Web crawling and data extraction

## Core Framework Components

### Behavioral Rules & Principles
| Component | Type | Purpose | Key Concepts |
|-----------|------|---------|--------------|
| **[PRINCIPLES.md](SuperClaude/Core/PRINCIPLES.md)** | Philosophy | Engineering mindset | SOLID, DRY, KISS, YAGNI |
| **[RULES.md](SuperClaude/Core/RULES.md)** | Rules | Behavioral standards | Priority system (🔴🟡🟢) |
| **[FLAGS.md](SuperClaude/Core/FLAGS.md)** | Flags | Execution control | Mode activation, tool selection |

### Business Analysis System
| Component | Type | Purpose | Key Elements |
|-----------|------|---------|--------------|
| **[BUSINESS_SYMBOLS.md](SuperClaude/Core/BUSINESS_SYMBOLS.md)** | Symbols | Visual notation | Strategic (🎯), Financial (💰), Risk (📉) |
| **[BUSINESS_PANEL_EXAMPLES.md](SuperClaude/Core/BUSINESS_PANEL_EXAMPLES.md)** | Examples | Usage patterns | Integration workflows, expert selection |

### Business Panel Experts (9)
- **Strategic**: Porter (⚔️), Kim/Mauborgne (🌊)
- **Innovation**: Christensen (🔨), Drucker (🧭), Godin (🎪)
- **Excellence**: Collins (🚀), Taleb (🛡️), Meadows (🕸️)
- **Communication**: Doumont (💬)

## Technical Architecture

### Three-Layer Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    Distribution Layer                       │
│         Python Package (PyPI) + Node.js Wrapper (npm)       │
└─────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Framework Layer                          │
│    Commands • Agents • Modes • MCP • Core Components        │
└─────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Installation Layer                        │
│         CLI • Core • Services • Utils • Components          │
└─────────────────────────────────────────────────────────────┘
```

### Component Dependencies
```yaml
# Commands declare dependencies via frontmatter
---
name: command-name
mcp-servers: [context7, sequential]
personas: [backend-architect, security-engineer]
modes: [orchestration, task-management]
---
```

### Installation Flow
1. **Validation**: Environment, dependencies, existing installation
2. **Backup**: Automatic backup creation
3. **Resolution**: Dependency graph construction
4. **Installation**: File operations, configuration merge
5. **Verification**: Component validation

## Development Workflow

### Project Structure
```
SuperClaude_Framework/
├── SuperClaude/          # Framework components
│   ├── Commands/         # 24 slash commands
│   ├── Agents/          # 14 AI personas
│   ├── Modes/           # 6 behavioral modes
│   ├── MCP/             # Server integrations
│   └── Core/            # Framework utilities
├── setup/               # Installation system
│   ├── cli/             # Command interface
│   ├── core/            # Installation logic
│   ├── services/        # Support services
│   └── utils/           # Utilities
├── tests/               # Test suite
├── Docs/                # Documentation
│   ├── Getting-Started/
│   ├── User-Guide/
│   ├── Developer-Guide/
│   └── Reference/
└── scripts/             # Utility scripts
```

### Development Commands
```bash
# Python Development
pip install -e .                    # Development install
pytest tests/                       # Run tests
black SuperClaude/ setup/           # Format code
flake8 SuperClaude/ setup/          # Lint
mypy SuperClaude/ setup/            # Type check

# Node.js Wrapper
npm install                         # Install dependencies
npm run lint                        # Run ESLint
npm publish                         # Publish to npm

# SuperClaude CLI
SuperClaude install                 # Fresh installation
SuperClaude install --force         # Force reinstall
SuperClaude update                  # Update to latest
SuperClaude backup                  # Create backup
SuperClaude uninstall              # Remove framework
```

### Key Files
| File | Purpose | Format |
|------|---------|--------|
| **[pyproject.toml](pyproject.toml)** | Python package config | TOML |
| **[package.json](package.json)** | Node.js wrapper | JSON |
| **[CLAUDE.md](CLAUDE.md)** | Project instructions | Markdown |
| **[setup.py](setup.py)** | Python setup | Python |
| **[VERSION](VERSION)** | Version tracking | Text |

## Testing & Quality

### Test Structure
```
tests/
├── test_installation.py    # Installation tests
├── test_components.py       # Component tests
├── test_dependencies.py     # Dependency resolution
└── test_cli.py             # CLI interface tests
```

### Quality Standards
- **Component Consistency**: Standard structure for all components
- **Dependency Validation**: No circular dependencies
- **Installation Safety**: Automatic backup before updates
- **Settings Preservation**: User customizations protected
- **Cross-Platform Support**: Python 3.9+ and Node.js

## Documentation

### User Documentation
- **[Quick Start Guide](Docs/Getting-Started/quick-start.md)**: Get up and running
- **[Installation Guide](Docs/Getting-Started/installation.md)**: Detailed setup
- **[Commands Reference](Docs/User-Guide/commands.md)**: All 24 commands
- **[Agents Guide](Docs/User-Guide/agents.md)**: 14 specialized agents
- **[Behavioral Modes](Docs/User-Guide/modes.md)**: 6 adaptive modes
- **[MCP Servers](Docs/User-Guide/mcp-servers.md)**: Server integrations
- **[Session Management](Docs/User-Guide/session-management.md)**: Save & restore

### Developer Documentation
- **[Technical Architecture](Docs/Developer-Guide/technical-architecture.md)**: System design
- **[Contributing Code](Docs/Developer-Guide/contributing-code.md)**: Development workflow
- **[Testing & Debugging](Docs/Developer-Guide/testing-debugging.md)**: Quality assurance

### Reference Documentation
- **[Examples Cookbook](Docs/Reference/examples-cookbook.md)**: Real-world recipes
- **[Troubleshooting](Docs/Reference/troubleshooting.md)**: Common issues
- **[Basic Examples](Docs/Reference/basic-examples.md)**: Simple patterns

## Contributing

### Priority Areas
| Priority | Area | Description |
|:--------:|------|-------------|
| 📝 **High** | Documentation | Improve guides, add examples |
| 🔧 **High** | MCP Integration | Add server configs, test integrations |
| 🎯 **Medium** | Workflows | Create command patterns & recipes |
| 🧪 **Medium** | Testing | Add tests, validate features |
| 🌐 **Low** | i18n | Translate docs to other languages |

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

## Support & Resources

### Project Links
- **Website**: https://superclaude.netlify.app/
- **GitHub**: https://github.com/SuperClaude-Org/SuperClaude_Framework
- **PyPI**: https://pypi.org/project/SuperClaude/
- **npm**: https://www.npmjs.com/package/@bifrost_inc/superclaude

### Support Options
- **Ko-fi**: https://ko-fi.com/superclaude (One-time)
- **Patreon**: https://patreon.com/superclaude (Monthly)
- **GitHub Sponsors**: https://github.com/sponsors/SuperClaude-Org (Flexible)

### Community
- Report issues: [GitHub Issues](https://github.com/SuperClaude-Org/SuperClaude_Framework/issues)
- Discussions: [GitHub Discussions](https://github.com/SuperClaude-Org/SuperClaude_Framework/discussions)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)

---

*Generated with SuperClaude Framework v4.1.1 - Last updated: 2025*