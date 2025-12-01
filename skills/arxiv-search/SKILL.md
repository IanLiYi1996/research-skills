---
name: arxiv-search
description: ArXiv paper search and download skill using the arxiv-mcp-server. Use when searching for academic preprints on arXiv, downloading papers, retrieving paper metadata, or managing a local paper library. Keywords include arXiv, preprint, paper search, paper download, academic literature, research papers, scientific papers, machine learning papers, physics papers, mathematics papers.
---

# ArXiv Search Skill

This skill provides direct access to arXiv.org through the arxiv-mcp-server for searching, downloading, and managing academic papers.

## Core Capabilities

### 1. Paper Search
Search arXiv papers with various query options:
- **Keyword Search**: Search by title, abstract, or full text
- **Author Search**: Find papers by specific authors
- **Category Filter**: Filter by arXiv categories (cs.AI, physics.hep-th, math.CO, etc.)
- **Date Range**: Limit results to specific time periods
- **Sorting**: Sort by relevance, date, or citation count

### 2. Paper Download
Download papers to local storage:
- Download PDF files by arXiv ID
- Batch download multiple papers
- Automatic organization by category or date
- Resume interrupted downloads

### 3. Metadata Retrieval
Get detailed paper information:
- Title, authors, and affiliations
- Abstract and keywords
- arXiv categories and primary category
- Submission and update dates
- DOI and journal references (if available)
- Version history

### 4. Library Management
Manage downloaded papers:
- List all downloaded papers
- Search within local library
- Delete papers from storage
- Export metadata to various formats

## MCP Server Integration

This skill uses the `arxiv` MCP server configured in the plugin. The server provides the following tools:

### Available MCP Tools

- **search_papers**: Search arXiv for papers matching query
- **download_paper**: Download a paper by arXiv ID
- **get_paper_metadata**: Get detailed metadata for a paper
- **list_papers**: List papers in local storage

## ArXiv Categories

Common arXiv categories for reference:

### Computer Science (cs.*)
- `cs.AI` - Artificial Intelligence
- `cs.CL` - Computation and Language (NLP)
- `cs.CV` - Computer Vision
- `cs.LG` - Machine Learning
- `cs.NE` - Neural and Evolutionary Computing
- `cs.RO` - Robotics
- `cs.SE` - Software Engineering

### Physics (physics.*, hep-*, cond-mat.*, etc.)
- `physics.comp-ph` - Computational Physics
- `hep-th` - High Energy Physics - Theory
- `cond-mat.stat-mech` - Statistical Mechanics
- `quant-ph` - Quantum Physics

### Mathematics (math.*)
- `math.CO` - Combinatorics
- `math.ST` - Statistics Theory
- `math.OC` - Optimization and Control

### Statistics (stat.*)
- `stat.ML` - Machine Learning
- `stat.TH` - Statistics Theory
- `stat.ME` - Methodology

### Quantitative Biology (q-bio.*)
- `q-bio.NC` - Neurons and Cognition
- `q-bio.GN` - Genomics

### Economics (econ.*)
- `econ.EM` - Econometrics

## Workflow Patterns

### Finding Recent Papers in a Field

1. Use category filter to target specific area
2. Set date range to recent papers (e.g., last 30 days)
3. Sort by submission date
4. Review abstracts for relevance
5. Download promising papers

### Literature Survey

1. Define search keywords from research question
2. Search with broad query first
3. Refine with category filters
4. Download relevant papers
5. Export metadata for bibliography

### Tracking Specific Authors

1. Search by author name
2. Sort by date to see latest work
3. Set up periodic searches for updates
4. Download new papers as they appear

## Best Practices

1. **Use Specific Queries**: Combine keywords with categories for better results
2. **Check Multiple Categories**: Papers may appear in multiple arXiv categories
3. **Verify Versions**: Check for updated versions of papers
4. **Local Storage**: Organize downloaded papers systematically
5. **Metadata Export**: Keep metadata for citation management
6. **Rate Limiting**: Be respectful of arXiv API rate limits

## Environment Configuration

The storage path for downloaded papers can be configured via environment variable:

```bash
export ARXIV_STORAGE_PATH=~/Documents/arxiv_papers
```

Default path: `~/Documents/arxiv_papers`

## Example Usage

When user requests: "Find recent papers on transformer architectures in NLP"

Process:
1. Search arXiv with query: "transformer architecture"
2. Filter by categories: cs.CL, cs.LG
3. Set date range: last 6 months
4. Sort by relevance
5. Review top results
6. Download selected papers
7. Extract metadata for citations

## Integration with Other Skills

- **academic-research**: Use ArXiv papers as sources for literature reviews
- **academic-writing**: Cite downloaded papers in manuscripts
- **data-visualization**: Analyze paper metadata trends
