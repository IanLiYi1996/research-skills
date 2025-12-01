---
name: web-fetch
description: Web content fetching skill for retrieving and processing online resources. Use when fetching web pages, downloading online content, accessing URLs for research, or extracting information from websites. Keywords include fetch, download, web page, URL, HTTP, online content, web scraping, content extraction.
---

# Web Fetch Skill

This skill provides web content fetching capabilities through the fetch MCP server for retrieving and processing online resources.

## Core Capabilities

### 1. Web Page Fetching

Retrieve content from web URLs:

- **HTML Content**: Fetch raw HTML from web pages
- **Text Extraction**: Extract readable text from pages
- **Markdown Conversion**: Convert web content to markdown
- **Metadata Retrieval**: Get page titles, descriptions, headers

### 2. Resource Download

Download various web resources:

- **Documents**: PDF, Word, Excel files
- **Data Files**: JSON, CSV, XML
- **Images**: PNG, JPG, SVG
- **Code**: Source files, scripts

### 3. API Interaction

Interact with web APIs:

- **GET Requests**: Retrieve data from REST APIs
- **Response Parsing**: Parse JSON/XML responses
- **Header Management**: Custom headers for authentication

### 4. Content Processing

Process fetched content:

- **Link Extraction**: Extract all links from a page
- **Text Cleaning**: Remove boilerplate, ads, navigation
- **Structure Analysis**: Identify main content areas

## MCP Server Integration

This skill uses the `fetch` MCP server configured in the plugin. The server provides HTTP fetching capabilities.

### Available Tools

- **fetch**: Fetch content from a URL
- **fetch_html**: Get raw HTML content
- **fetch_markdown**: Get content as markdown
- **fetch_text**: Get plain text content

## Use Cases for Research

### Literature Discovery

1. Fetch research group web pages
2. Extract publication lists
3. Download paper PDFs
4. Collect author information

### Data Collection

1. Fetch datasets from repositories
2. Download supplementary materials
3. Access online databases
4. Retrieve API data

### Reference Gathering

1. Fetch documentation pages
2. Extract code examples
3. Download technical specifications
4. Access online manuals

## Workflow Patterns

### Fetching a Research Paper Website

1. Fetch the main page URL
2. Extract links to publications
3. Filter for relevant papers
4. Download PDF links
5. Extract metadata

### Collecting Dataset Information

1. Fetch dataset repository page
2. Extract dataset descriptions
3. Download data files
4. Parse metadata files

### Monitoring Research Updates

1. Fetch conference/journal pages
2. Extract new publication listings
3. Compare with previous fetches
4. Identify new papers

## Best Practices

1. **Respect Rate Limits**: Don't overwhelm servers with requests
2. **Check Robots.txt**: Respect website crawling policies
3. **Use Caching**: Avoid re-fetching unchanged content
4. **Handle Errors**: Gracefully handle 404s, timeouts
5. **Verify Content**: Check fetched content for completeness
6. **Legal Compliance**: Respect copyright and terms of service

## Common URL Patterns

| Source | URL Pattern |
|--------|-------------|
| arXiv | `https://arxiv.org/abs/XXXX.XXXXX` |
| GitHub | `https://github.com/user/repo` |
| Google Scholar | `https://scholar.google.com/...` |
| DOI | `https://doi.org/10.XXXX/...` |
| PubMed | `https://pubmed.ncbi.nlm.nih.gov/XXXXX` |

## Example Usage

When user requests: "Fetch the content from this research page"

Process:

1. Validate the URL
2. Send fetch request
3. Process response content
4. Extract relevant information
5. Format for user consumption

## Integration with Other Skills

- **academic-research**: Fetch sources for literature reviews
- **arxiv-search**: Complement arXiv API with web fetching
- **data-visualization**: Fetch data for analysis
