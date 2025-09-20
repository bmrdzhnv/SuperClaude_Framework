---
name: research
description: "Documentation service providing current technical content for agent expertise"
category: orchestration
complexity: advanced
mcp-servers: [exa, crawl4ai, sequential, serena]
personas: [computational-strategist, backend-architect, frontend-architect, security-engineer, requirements-analyst]
---

# /sc:research - Documentation Service for Agents

Gather current documentation, APIs, and patterns that agents analyze with their expertise.

## Usage
```
/sc:research "topic" [--specialty auto|code|crypto|algorithmic|business|security] [--depth shallow|normal|deep] [--ai-analysis] [--token-efficient] [--multi-source]
```

## Purpose: Enable Agents with Current Knowledge

Agents have **timeless expertise** (how to architect, secure, teach) but lack **current content** (latest APIs, frameworks, patterns). Research bridges this gap.

## How It Works

### Phase 1: Parallel Discovery
**Simultaneous Search for Maximum Coverage**
- **Exa**: High-quality technical documentation with semantic understanding
- **Google** (via crawl4ai): Real-time comprehensive results
- **Execution**: Both run in parallel for 40-60% speed improvement

### Phase 2: Intelligent Extraction
**Content-Aware Tool Routing**
- **Single page**: `crawl_url` (simple) or `intelligent_extract` (complex)
- **Documentation sites**: `deep_crawl_site` with depth control
- **Multiple URLs**: `batch_crawl` for parallel processing
- **Mixed media**: `process_file` (PDFs), `extract_youtube_transcript` (videos)
- **Token optimization**: Auto-summarization for large content

### Phase 3: Structure for Agents
**Organize for Agent Consumption**
- Extract key sections: Installation, Configuration, Usage, API Reference
- Maintain source attribution for credibility
- Create topic indexes for quick agent lookup
- Tag with timestamps and relevance scores

### Phase 4: Store and Serve
**Persistent Documentation Layer**
- **Serena**: Session persistence for agent access
- **Structure**: Agent-consumable format with quick lookups
- **Updates**: Refresh when agents detect outdated content

## Usage Patterns

### Research-First Development
```bash
# Research current patterns, then implement
/sc:research "Next.js 14 app router patterns"
# → Stores structured docs in Serena
/sc:implement landing-page
# → Frontend-architect uses researched patterns
```

### Continuous Documentation Updates
```bash
# Keep agents current with latest docs
/sc:research "React 19 features" --depth deep
# Later in session, agents reference stored React 19 docs
```

### Multi-Source Comparison
```bash
# Research alternatives for informed decisions
/sc:research "auth providers comparison: Auth0 vs Clerk vs NextAuth"
# Security-engineer analyzes all options
# Requirements-analyst evaluates trade-offs
```

## Optimization Flags

### --token-efficient
Maximizes efficiency through intelligent extraction
- Uses `intelligent_extract` for 88.5% token reduction
- Applies `auto_summarize` for large content
- Preserves key information while reducing volume

### --depth [shallow|normal|deep]
Controls research thoroughness
- **shallow**: Quick overview, main documentation only
- **normal**: Standard depth, includes examples and patterns
- **deep**: Comprehensive, includes issues, discussions, edge cases

### --store
Explicitly store for agent access (default behavior)
- Saves to Serena memory for session persistence
- Creates structured indexes for agent lookups
- Maintains source links and timestamps

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

### **Enhanced Research with AI Analysis**
```bash
# React accessibility research with intelligent extraction
/sc:research "React accessibility patterns" --specialty code --depth deep --ai-analysis

# Crypto security analysis with token efficiency
/sc:research "DeFi yield farming risks" --specialty crypto --depth normal --token-efficient

# Algorithm optimization with multi-source processing
/sc:research "Quicksort optimization techniques" --specialty algorithmic --depth shallow --multi-source

# Market intelligence with comprehensive analysis
/sc:research "AI SaaS competitive landscape" --specialty business --depth deep --ai-analysis --multi-source

# Security vulnerability research with entity extraction
/sc:research "OAuth 2.0 security vulnerabilities" --specialty security --depth normal --ai-analysis

# YouTube + PDF documentation research
/sc:research "Machine Learning deployment best practices" --specialty code --multi-source --token-efficient

# Large-scale competitive analysis with optimization
/sc:research "Fintech API security landscape 2024" --specialty business --depth deep --ai-analysis --token-efficient
```

### **Traditional Research (Backward Compatible)**
```bash
# Standard semantic research (unchanged behavior)
/sc:research "React patterns" --specialty code --depth normal

# Quick algorithmic research
/sc:research "Binary search variants" --specialty algorithmic --depth shallow
```

## Agent-Research Integration

### How Agents Use Research

**Frontend-architect**
```yaml
needs: "Current framework patterns, component libraries, performance techniques"
uses_research_for: "Architectural decisions based on latest best practices"
example: "Researched Next.js patterns → Applies to routing architecture"
```

**Security-engineer**
```yaml
needs: "Security vulnerabilities, OWASP guidelines, auth patterns"
uses_research_for: "Security analysis with current threat landscape"
example: "Researched JWT vulnerabilities → Audits authentication system"
```

**Backend-architect**
```yaml
needs: "API patterns, database strategies, scaling techniques"
uses_research_for: "System design with current technologies"
example: "Researched microservices patterns → Designs service architecture"
```

**Learning-guide**
```yaml
needs: "Tutorial content, documentation, learning resources"
uses_research_for: "Creating learning paths with current materials"
example: "Researched React tutorials → Structures learning progression"
```

## Storage Structure

```yaml
serena_memory:
  research:
    topics:              # Organized by subject
      react_19:         # Version-specific docs
      nextauth_v5:      # Framework documentation
      stripe_webhooks:  # API patterns

    sessions:           # Temporal organization
      2024_01_20:       # Today's research

    agent_access:       # Quick lookups
      frontend:         # Frontend-relevant docs
      security:         # Security-focused content
      backend:          # Backend documentation
```