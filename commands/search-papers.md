# Literature Search Command

Search, discover, and filter academic papers across multiple sources.

## Purpose

Find relevant research papers and academic literature:
- Search across academic databases and repositories
- Filter by publication date, citations, venue
- Assess paper relevance and quality
- Export search results in organized format
- Save searches for ongoing literature reviews

## Usage

```
/search-papers [query] [options]
```

**Parameters:**
- `query`: Search terms and keywords (use quotes for exact phrases)
- `options` (optional): Filters for year, venue, author, field

## Workflow

1. **Query Construction**: Build effective search query with boolean operators
2. **Source Selection**: Choose academic databases to search
3. **Search Execution**: Run query across selected sources
4. **Result Filtering**: Apply filters for date, citations, relevance
5. **Relevance Ranking**: Sort by relevance, recency, or citation count
6. **Export Results**: Save to bibliography file or database

## Output

The search generates:

### Search Results List
For each paper:
- Title and authors
- Publication venue and date
- Abstract (first 200 words)
- Citation count
- DOI and access links
- Relevance score

### Summary Statistics
- Total results found
- Results per source
- Date range coverage
- Top cited papers
- Publication venue distribution

### Filtered Results
- Papers matching all criteria
- Relevance-ranked list
- Papers grouped by theme/topic
- Recommendations for related work

### Export Options
- BibTeX format for reference managers
- CSV for spreadsheet analysis
- Markdown for documentation
- JSON for programmatic processing

## Examples

### Basic Search
```
/search-papers "machine learning interpretability"
```
Searches for papers on ML interpretability.

### Advanced Boolean Search
```
/search-papers "(deep learning OR neural networks) AND (explainability OR interpretability)"
```
Uses boolean operators for complex queries.

### Filtered Search
```
/search-papers "climate change mitigation" --year 2020-2024 --min-citations 50
```
Finds recent, highly-cited papers on climate change.

### Author Search
```
/search-papers --author "Hinton, G" --year 2015-2024
```
Finds recent papers by specific author.

### Venue-Specific Search
```
/search-papers "computer vision" --venue "CVPR,ICCV,ECCV" --year 2023-2024
```
Searches specific conferences.

### Save Search
```
/search-papers "quantum computing applications" --save "quantum-review" --limit 100
```
Saves search results for ongoing review.

## Search Sources

Integrated sources:
- **arXiv**: Preprints in physics, math, CS, quantitative biology
- **Semantic Scholar**: Cross-disciplinary AI-powered search
- **Google Scholar**: Comprehensive academic search
- **PubMed**: Biomedical and life sciences
- **IEEE Xplore**: Engineering and computer science
- **ACM Digital Library**: Computing literature

## Search Operators

### Boolean Operators
- `AND`: Both terms must appear
- `OR`: Either term can appear
- `NOT`: Exclude term
- `"exact phrase"`: Exact match

### Field-Specific
- `author:"Name"`: Search by author
- `title:"keywords"`: Search in title only
- `abstract:"term"`: Search in abstract
- `venue:"Journal Name"`: Specific publication venue

### Wildcards
- `comput*`: Matches computer, computing, computation
- `neural netw?rk`: Matches network or networks

## Best Practices

1. **Start Broad**: Begin with general terms, then refine
2. **Use Quotes**: Exact phrases for specific concepts
3. **Check Spelling**: Typos affect results significantly
4. **Multiple Sources**: Search across databases for completeness
5. **Save Queries**: Document searches for reproducibility
6. **Citation Tracking**: Follow citation trails for relevant papers
7. **Set Alerts**: Create alerts for ongoing research areas
