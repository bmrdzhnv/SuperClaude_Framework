# Crawl4ai MCP Server (walksoda/crawl-mcp)

**Purpose**: Web content extraction and processing with intelligent tool routing and token optimization

## Triggers
- Web content extraction requiring structured processing
- Multi-page crawling with depth control
- Document processing (PDF, Office, YouTube)
- Google search integration for research
- Token optimization needs (large content)
- Entity extraction from web content

## Choose When
- **Over Read tool**: When you need structured extraction or processing
- **For research workflows**: Building knowledge bases from web sources
- **For multi-format content**: PDFs, Office docs, YouTube transcripts
- **With token constraints**: Intelligent extraction reduces tokens by 88.5%
- **Not for simple reading**: Single pages without processing needs

## Tool Categories

### Web Crawling
- `crawl_url` - Single page extraction
- `deep_crawl_site` - Multi-page with depth control
- `batch_crawl` - Parallel URL processing
- `crawl_url_with_fallback` - Error-resilient crawling

### Content Analysis
- `intelligent_extract` - Token-optimized extraction (88.5% reduction)
- `auto_summarize` - Configurable summarization
- `extract_entities` - Named entity recognition

### Search Integration
- `search_google` - Web search with extraction
- `search_and_crawl` - Search + crawl pipeline
- `batch_search_google` - Bulk search operations

### Media Processing
- `process_file` - PDF/Office document handling
- `extract_youtube_transcript` - Video transcript extraction
- `batch_extract_youtube_transcripts` - Bulk video processing

## Works Best With
- **Exa**: Exa discovers sources → crawl4ai extracts content with token optimization
- **Sequential**: Sequential plans strategy → crawl4ai executes extraction pipeline
- **Serena**: crawl4ai processes content → Serena stores for project memory

## Examples
```
"extract content from documentation site" → deep_crawl_site (multi-page extraction)
"process these PDFs and web pages" → process_file + crawl_url (mixed media)
"research with token efficiency" → intelligent_extract (88.5% reduction)
"find and extract competitor data" → search_google + intelligent_extract
"YouTube tutorial knowledge base" → extract_youtube_transcript + auto_summarize
"bulk URL processing" → batch_crawl (parallel extraction)
"just read this page" → Read tool (simple viewing)
```