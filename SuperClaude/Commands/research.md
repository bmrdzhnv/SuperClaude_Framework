---
name: research
description: "Semantic web research with content extraction and expert analysis"
category: orchestration
complexity: advanced
mcp-servers: [exa, crawl4ai, sequential]
personas: [computational-strategist, backend-architect, frontend-architect, security-engineer, requirements-analyst]
---

# /sc:research - Semantic Web Research

Research topics using semantic search, extract quality content, and get expert analysis from domain specialists.

## Usage
```
/sc:research "topic" [--specialty auto|code|crypto|algorithmic|business|security] [--depth shallow|normal|deep]
```

## How it works
1. **Semantic Search**: Exa.ai finds high-quality sources
2. **Content Extraction**: crawl4ai converts web content to clean markdown
3. **Expert Analysis**: Domain experts analyze and synthesize findings
4. **Storage**: Results saved to `~/.claude/knowledge/research/` and `claudedocs/research/`

## Research Specialties

### Code/Programming
**Agents**: frontend-architect, backend-architect, python-expert
**Focus**: Technical documentation, API references, framework patterns, best practices

### Crypto/Blockchain
**Agents**: security-engineer, computational-strategist, backend-architect
**Focus**: DeFi protocols, blockchain technology, security analysis

### Algorithmic
**Agents**: computational-strategist, performance-engineer, system-architect
**Focus**: Computer science algorithms, optimization techniques, performance studies

### Business
**Agents**: requirements-analyst, meta-agent, business-panel
**Focus**: Market analysis, competitive intelligence, industry trends

### Security
**Agents**: security-engineer, root-cause-analyst
**Focus**: Vulnerability research, threat intelligence, security frameworks

## Examples

```bash
# React accessibility research
/sc:research "React accessibility patterns" --specialty code --depth deep

# Crypto security analysis
/sc:research "DeFi yield farming risks" --specialty crypto --depth normal

# Algorithm optimization
/sc:research "Quicksort optimization techniques" --specialty algorithmic --depth shallow

# Market intelligence
/sc:research "AI SaaS competitive landscape" --specialty business --depth deep

# Security vulnerability research
/sc:research "OAuth 2.0 security vulnerabilities" --specialty security --depth normal
```

## Storage Structure

```
~/.claude/knowledge/research/           # Global cross-project research
├── topics/accessibility/               # Topic-based organization
├── topics/react-patterns/
└── agents/frontend-architect/          # Agent contribution tracking

claudedocs/research/                    # Project-specific research
├── sessions/2024-01-20_accessibility/  # Research sessions
└── references/                        # Links to global research
```