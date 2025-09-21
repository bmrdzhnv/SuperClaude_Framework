---
name: research
description: Intelligent deep research with optimal tool orchestration
category: command
complexity: advanced
mcp-servers: [exa, crawl4ai, tavily, sequential, playwright, serena]
personas: [deep-research-agent]
---

# /sc:research - Intelligent Research Command

> **Context Framework Note**: This command orchestrates Exa AI and Crawl4ai as primary research tools with Tavily providing robust support, creating an optimal pipeline for discovery, extraction, and synthesis.

## Triggers
- Research questions beyond knowledge cutoff
- Complex research questions requiring multi-source analysis
- Current events and real-time information needs
- Academic, technical, or business research requirements
- Market analysis and competitive intelligence

## Context Trigger Pattern
```
/sc:research "[query]" [options]
```

### Core Options
- `--depth quick|standard|deep|exhaustive` - Research depth
- `--mode discovery|extraction|synthesis|pipeline` - Tool routing mode
- `--primary exa|crawl|tavily` - Override primary tool selection
- `--token-optimize` - Maximize token efficiency (prioritize Crawl4ai)
- `--quality-first` - Maximize source quality (prioritize Exa)

## Intelligent Tool Orchestration

### 🎯 Three-Stage Research Pipeline (Default)

#### Stage 1: Discovery (Finding Sources)
**Primary**: **Exa AI** - Neural semantic search for high-quality sources
- Finds authoritative, domain-specific content
- Superior for academic papers, technical documentation
- Semantic understanding beats keyword matching

**Support**: **Tavily** - Broader coverage when needed
- Real-time information and current events
- Fallback for comprehensive coverage
- Quick factual lookups

#### Stage 2: Extraction (Getting Content)
**Primary**: **Crawl4ai** - Token-optimized extraction
- 88.5% token reduction through intelligent processing
- Handles PDFs, Office docs, YouTube transcripts
- Parallel batch processing for multiple URLs
- Advanced extraction strategies (LLM tables, entities)

**Support**: **Tavily** - Simpler extraction needs
- Sites that resist advanced crawling
- Quick content grabs
- Built-in summarization

#### Stage 3: Synthesis (Making Sense)
**Combined Approach**:
- **Sequential**: Complex reasoning and hypothesis testing
- **Tavily**: Multi-hop exploration and evidence chains
- **Integrated insights** from all discovered content

### 🚀 Smart Query Routing

The command automatically detects query type and routes to optimal tools:

#### Academic/Technical Queries
```
Exa (semantic discovery) → Crawl4ai (efficient extraction) → Sequential (analysis)
```

#### Current Events/News
```
Tavily (real-time search) → Crawl4ai (detailed extraction) → Synthesis
```

#### Documentation/Tutorials
```
Exa (quality sources) → Crawl4ai (structured extraction) → Analysis
```

#### Multi-Source Research
```
Parallel: [Exa + Tavily] → Crawl4ai (batch extraction) → Combined synthesis
```

## Behavioral Flow

### 1. Understand & Route (5-10% effort)
- Analyze query type and complexity
- Select optimal tool combination
- Determine token budget allocation
- Define success criteria

### 2. Plan & Parallelize (10-15% effort)
- Identify parallelization opportunities
- Design multi-stage execution plan
- Allocate tools to stages
- Create investigation milestones

### 3. TodoWrite (5% effort)
- Create stage-based task hierarchy
- Track tool assignments
- Monitor pipeline progress
- Document decision points

### 4. Execute Pipeline (50-60% effort)

#### Discovery Phase
- **Parallel execution**: Run Exa + Tavily simultaneously when needed
- **Quality filtering**: Exa's semantic ranking prioritizes best sources
- **Coverage assurance**: Tavily fills gaps in specialized domains

#### Extraction Phase
- **Smart batching**: Group URLs for Crawl4ai parallel processing
- **Format handling**: Automatic routing for PDFs, videos, documents
- **Token optimization**: Intelligent extraction reduces content by 88.5%
- **Fallback cascade**: Tavily extraction if Crawl4ai fails

#### Synthesis Phase
- **Multi-hop reasoning**: Connect insights across sources
- **Evidence chains**: Track information provenance
- **Confidence scoring**: Weight sources by quality and relevance

### 5. Track (Continuous)
- Monitor pipeline stage completion
- Track token usage efficiency
- Log tool performance metrics
- Identify bottlenecks

### 6. Validate (10-15% effort)
- Cross-reference findings
- Verify source credibility
- Resolve contradictions
- Ensure completeness

## Execution Modes

### Default: Intelligent Pipeline
Automatically selects optimal tool combination based on query analysis

### Discovery Mode (`--mode discovery`)
```
Primary: Exa AI → Fallback: Tavily
```
Best for: Finding high-quality sources, academic research, technical documentation

### Extraction Mode (`--mode extraction`)
```
Primary: Crawl4ai → Fallback: Tavily
```
Best for: Known URLs, multi-format content, token-constrained scenarios

### Synthesis Mode (`--mode synthesis`)
```
Primary: Tavily + Sequential → Support: All tools
```
Best for: Complex analysis, multi-hop reasoning, connecting insights

### Full Pipeline Mode (`--mode pipeline`)
```
Exa Discovery → Crawl4ai Extraction → Combined Synthesis
```
Best for: Comprehensive research requiring maximum quality and efficiency

## Token Budget Management

### Small Budget (<10K tokens)
- Crawl4ai-only extraction for maximum efficiency
- Single-source focused research
- Quick summaries over detailed analysis

### Medium Budget (10-30K tokens)
- Exa discovery + Crawl4ai extraction
- Multi-source research with optimization
- Balanced quality and coverage

### Large Budget (30K+ tokens)
- Full pipeline with all tools
- Comprehensive multi-source analysis
- Deep synthesis and validation

## Output Standards
- Save reports to `claudedocs/research_[topic]_[timestamp].md`
- Include tool attribution (which tool found what)
- Provide extraction efficiency metrics
- List all sources with quality scores

## Examples

### Optimized Academic Research
```
/sc:research "quantum error correction advances 2024" --quality-first
# Exa finds top papers → Crawl4ai extracts with 88.5% token savings → Deep analysis
```

### Efficient Documentation Research
```
/sc:research "React Server Components patterns" --token-optimize
# Quick Exa discovery → Aggressive Crawl4ai extraction → Structured synthesis
```

### Comprehensive Market Analysis
```
/sc:research "AI coding assistant market landscape" --mode pipeline --depth deep
# Full pipeline: Exa quality sources + Tavily coverage → Crawl4ai bulk extraction → Multi-tool synthesis
```

### Multi-Format Technical Research
```
/sc:research "Kubernetes best practices" --mode extraction
# Crawl4ai processes docs, PDFs, videos → Token-optimized delivery → Practical insights
```

### Real-Time + Deep Research
```
/sc:research "OpenAI o3 model capabilities" --depth exhaustive
# Tavily real-time + Exa quality sources → Crawl4ai extraction → Comprehensive analysis
```

## Tool Selection Matrix

| Query Type | Primary Discovery | Primary Extraction | Primary Synthesis |
|------------|------------------|-------------------|-------------------|
| Academic/Technical | Exa | Crawl4ai | Sequential |
| Current Events | Tavily | Crawl4ai | Tavily |
| Documentation | Exa | Crawl4ai | Sequential |
| Multi-Source | Exa + Tavily | Crawl4ai | Combined |
| Quick Facts | Tavily | Tavily | Tavily |
| PDF/Video Heavy | Exa | Crawl4ai | Sequential |

## Performance Metrics

### Efficiency Gains
- **Token Reduction**: 88.5% average with Crawl4ai
- **Source Quality**: 3x better relevance with Exa
- **Processing Speed**: 2x faster with parallel execution
- **Coverage**: 40% more comprehensive with combined tools

## Boundaries
**Will**: Intelligently orchestrate tools, optimize token usage, maximize research quality
**Won't**: Force tool usage when inappropriate, skip validation, compromise quality for speed