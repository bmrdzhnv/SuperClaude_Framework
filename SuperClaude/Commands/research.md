---
name: research
description: Deep web research with adaptive planning and intelligent search
category: command
complexity: advanced
mcp-servers: [tavily, exa, crawl4ai, sequential, playwright, serena]
personas: [deep-research-agent]
---

# /sc:research - Deep Research Command

> **Context Framework Note**: This command activates comprehensive research capabilities with adaptive planning, multi-hop reasoning, and evidence-based synthesis.

## Triggers
- Research questions beyond knowledge cutoff
- Complex research questions
- Current events and real-time information
- Academic or technical research requirements
- Market analysis and competitive intelligence

## Context Trigger Pattern
```
/sc:research "[query]" [--depth quick|standard|deep|exhaustive] [--strategy planning|intent|unified] [--semantic] [--extract] [--pipeline]
```

## Behavioral Flow

### 1. Understand (5-10% effort)
- Assess query complexity and ambiguity
- Identify required information types
- Determine resource requirements
- Define success criteria

### 2. Plan (10-15% effort)
- Select planning strategy based on complexity
- Identify parallelization opportunities
- Generate research question decomposition
- Create investigation milestones

### 3. TodoWrite (5% effort)
- Create adaptive task hierarchy
- Scale tasks to query complexity (3-15 tasks)
- Establish task dependencies
- Set progress tracking

### 4. Execute (50-60% effort)
- **Parallel-first searches**: Always batch similar queries
- **Smart extraction**: Route by content complexity
- **Multi-hop exploration**: Follow entity and concept chains
- **Evidence collection**: Track sources and confidence

#### Enhanced Execution with Additional MCPs
When enhanced flags are used, the execution phase adapts:

- **--semantic**: Activates Exa for semantic discovery phase
  - Finds high-quality, domain-specific sources
  - Prioritizes authority and relevance over quantity
  - Ideal for technical documentation, research papers

- **--extract**: Activates Crawl4ai for efficient extraction
  - Reduces token usage by 88.5% through intelligent extraction
  - Handles PDFs, Office docs, YouTube transcripts
  - Parallel processing for multiple URLs

- **--pipeline**: Full integration pipeline
  1. **Exa Discovery**: Semantic search for quality sources
  2. **Crawl4ai Extraction**: Efficient content extraction with token optimization
  3. **Tavily Analysis**: Deep research and synthesis
  4. **Sequential Reasoning**: Complex multi-hop analysis

### 5. Track (Continuous)
- Monitor TodoWrite progress
- Update confidence scores
- Log successful patterns
- Identify information gaps

### 6. Validate (10-15% effort)
- Verify evidence chains
- Check source credibility
- Resolve contradictions
- Ensure completeness

## Key Patterns

### Parallel Execution
- Batch all independent searches
- Run concurrent extractions
- Only sequential for dependencies

### Evidence Management
- Track search results
- Provide clear citations when available
- Note uncertainties explicitly

### Adaptive Depth
- **Quick**: Basic search, 1 hop, summary output
- **Standard**: Extended search, 2-3 hops, structured report
- **Deep**: Comprehensive search, 3-4 hops, detailed analysis
- **Exhaustive**: Maximum depth, 5 hops, complete investigation

## MCP Integration

### Core MCPs (Always Active)
- **Tavily**: Primary search and extraction engine
- **Sequential**: Complex reasoning and synthesis
- **Playwright**: JavaScript-heavy content extraction
- **Serena**: Research session persistence

### Enhanced MCPs (Flag-Activated)
- **Exa** (--semantic): Neural semantic search for high-quality sources
  - Academic papers and technical documentation
  - Domain-specific expertise content
  - Authority-based filtering

- **Crawl4ai** (--extract): Token-optimized content extraction
  - 88.5% token reduction through intelligent extraction
  - Multi-format support (PDF, Office, YouTube)
  - Parallel URL processing capabilities

## Enhanced Research Patterns

### Semantic Research Pipeline (--semantic)
```
Exa Discovery → Quality Source Identification → Tavily Deep Dive → Synthesis
```
Best for: Technical research, academic papers, domain expertise

### Efficient Extraction Pipeline (--extract)
```
Search → Crawl4ai Extraction → Token Optimization → Analysis
```
Best for: Large-scale content processing, multi-format sources

### Complete Pipeline (--pipeline)
```
Exa Semantic Search → Crawl4ai Extraction → Tavily Analysis → Sequential Reasoning
```
Best for: Comprehensive research requiring both quality and efficiency

## Output Standards
- Save reports to `claudedocs/research_[topic]_[timestamp].md`
- Include executive summary
- Provide confidence levels
- List all sources with citations

## Examples

### Standard Deep Research (Default)
```
/sc:research "latest developments in quantum computing 2024"
/sc:research "competitive analysis of AI coding assistants" --depth deep
/sc:research "best practices for distributed systems" --strategy unified
```

### Enhanced Semantic Research
```
/sc:research "transformer architecture improvements" --semantic --depth deep
# Uses Exa to find high-quality technical papers and authoritative sources
```

### Token-Efficient Research
```
/sc:research "comprehensive React patterns guide" --extract --depth exhaustive
# Uses Crawl4ai for 88.5% token reduction on large documentation sites
```

### Full Pipeline Research
```
/sc:research "AI safety research landscape 2024" --pipeline --depth deep
# Combines Exa discovery + Crawl4ai extraction + Tavily analysis
```

### Multi-Format Research
```
/sc:research "machine learning deployment strategies" --extract --depth standard
# Processes PDFs, YouTube tutorials, and documentation with Crawl4ai
```

## Boundaries
**Will**: Current information, intelligent search, evidence-based analysis, multi-MCP orchestration
**Won't**: Make claims without sources, skip validation, access restricted content