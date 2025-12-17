---
name: reference-management
description: Reference and citation management using DBLP database for computer science literature. Use when searching for academic papers, building bibliographies, managing BibTeX entries, tracking citations, or creating reference lists for publications. Keywords include bibliography, BibTeX, references, citations, DBLP, literature search, academic papers, computer science publications, bibliography management, citation tracking.
---

# Reference Management Skill

This skill provides comprehensive bibliography and citation management through the DBLP (Digital Bibliography & Library Project) database, enabling researchers to efficiently search for papers, collect citations, and generate BibTeX files.

## Core Capabilities

### 1. Paper Search

Search DBLP's comprehensive computer science bibliography:

- **Keyword Search**: Search by keywords with boolean operators (AND, OR)
- **Author Search**: Find publications by specific authors with fuzzy matching
- **Title Search**: Fuzzy title matching for finding papers by approximate title
- **Venue Search**: Search by conference or journal venue
- **Date Filtering**: Filter by publication year ranges

### 2. BibTeX Management

Collect and organize citations:

- **Add Entries**: Add papers to bibliography collection using DBLP keys
- **Custom Citation Keys**: Define your own citation keys for LaTeX
- **Batch Collection**: Collect multiple papers in one session
- **Export to .bib**: Export collected entries to BibTeX files

### 3. Batch Operations

Handle multiple papers efficiently:

- **Parallel Search**: Search multiple queries simultaneously
- **Bulk Export**: Export many citations at once
- **Batch Statistics**: Analyze collections of papers
- **Multi-author Tracking**: Follow multiple researchers

### 4. Citation Statistics

Analyze publication trends and metrics:

- **Author Analysis**: Publication counts and collaboration networks
- **Venue Analysis**: Top venues and publication patterns
- **Time Analysis**: Publication trends over years
- **Topic Analysis**: Research area distributions

### 5. arXiv Integration

Seamless workflow with arXiv papers:

- **Link DBLP to arXiv**: Extract arXiv IDs from DBLP entries
- **Download Workflow**: Search DBLP, then download from arXiv
- **Unified Bibliography**: Combine DBLP metadata with arXiv PDFs
- **Cross-reference**: Verify papers across both databases

## MCP Server Integration

This skill uses the `dblp` MCP server configured in the plugin. The server provides direct access to DBLP database.

### Available MCP Tools

- **search**: Boolean query search across DBLP
- **fuzzy_title_search**: Find papers by approximate title matching
- **get_author_publications**: Retrieve all publications by an author
- **get_venue_info**: Get information about conferences/journals
- **calculate_statistics**: Generate statistics from search results
- **add_bibtex_entry**: Add a paper to your bibliography collection
- **export_bibtex**: Export collected entries to .bib file

### Workflow Pattern

1. Search for papers using keyword, author, or title search
2. Review results and identify relevant papers
3. Add papers to bibliography using DBLP keys
4. Repeat for all needed references
5. Export complete bibliography to .bib file
6. Use .bib file in LaTeX documents

## Common DBLP Venues

### Top-Tier Conferences

| Venue | Full Name | Area |
|-------|-----------|------|
| ICML | International Conference on Machine Learning | ML |
| NeurIPS | Neural Information Processing Systems | ML/AI |
| ICLR | International Conference on Learning Representations | DL |
| CVPR | Computer Vision and Pattern Recognition | CV |
| ACL | Association for Computational Linguistics | NLP |
| EMNLP | Empirical Methods in Natural Language Processing | NLP |
| SIGMOD | International Conference on Management of Data | DB |
| VLDB | Very Large Data Bases | DB |
| OSDI | Operating Systems Design and Implementation | Systems |
| SOSP | Symposium on Operating Systems Principles | Systems |

### Leading Journals

| Venue | Full Name | Area |
|-------|-----------|------|
| JMLR | Journal of Machine Learning Research | ML |
| TPAMI | IEEE Transactions on Pattern Analysis and Machine Intelligence | CV/ML |
| TACL | Transactions of the Association for Computational Linguistics | NLP |
| TODS | ACM Transactions on Database Systems | DB |
| TOCS | ACM Transactions on Computer Systems | Systems |

## Workflow Patterns

### Building Bibliography for Paper

Systematic approach to literature collection:

1. **Define Scope**: List key topics and required citations
2. **Keyword Search**: Search DBLP for each topic area
3. **Author Search**: Find papers by key researchers
4. **Venue Search**: Check top-tier conference proceedings
5. **Collect Citations**: Add relevant papers to bibliography
6. **Export**: Generate .bib file for LaTeX document

### Author Research Tracking

Monitor researcher publications:

1. Search by author name with fuzzy matching
2. Review publication list and statistics
3. Identify collaboration patterns
4. Track publication venues
5. Follow research evolution over time

### Venue-Specific Searches

Find papers from specific conferences/journals:

1. Get venue information to verify abbreviation
2. Search papers with venue filter
3. Filter by year range if needed
4. Review highly-cited papers from venue
5. Add selected papers to bibliography

### Literature Review Workflow

Comprehensive literature survey:

1. **Broad Search**: Start with general keywords
2. **Refine**: Add venue and date filters
3. **Author Follow-up**: Track key researchers
4. **Citation Network**: Follow references
5. **Statistics**: Analyze trends and gaps
6. **Export**: Generate complete bibliography

### Batch Export for Citation Lists

Efficient multi-paper collection:

1. Perform multiple searches in parallel
2. Collect DBLP keys from results
3. Add all papers in batch
4. Export to single .bib file
5. Import into reference manager

## Best Practices

### Search Strategies

1. **Start Broad**: Begin with general keywords, narrow down
2. **Use Boolean Operators**: Combine terms with AND/OR
3. **Try Variations**: Author names may have different formats
4. **Check Multiple Venues**: Papers may appear in different forms
5. **Use Fuzzy Matching**: For uncertain titles, use similarity threshold

### BibTeX Management

1. **Consistent Citation Keys**: Use format like `Author2024Title`
2. **Meaningful Names**: Keys should indicate content
3. **Avoid Duplicates**: Check for existing entries
4. **Organize by Topic**: Group related papers
5. **Regular Export**: Save .bib files frequently

### Quality Control

1. **Verify Metadata**: Check author names and titles
2. **Confirm Venue**: Ensure venue abbreviations are correct
3. **Check Dates**: Verify publication years
4. **Cross-reference**: Compare with other sources
5. **Test Compilation**: Ensure .bib works in LaTeX

### Citation Key Conventions

Common formats for citation keys:

```
Author2024                    # Single author, year
SmithJones2024               # Two authors, year
Smith2024ML                   # Author, year, topic
Smith2024Attention           # Author, year, keyword
ICML24Smith                  # Venue, year, author
```

## Integration with Other Skills

### With academic-research Skill

**Combined Workflow for Literature Review:**

1. Use `reference-management` to search DBLP
2. Collect BibTeX entries for found papers
3. Use `academic-research` for deeper analysis
4. Synthesize findings into literature review
5. Export final bibliography with citations

**Benefits:**
- DBLP provides comprehensive CS bibliography
- academic-research helps analyze papers
- Together enable complete lit review process

### With arxiv-search Skill

**DBLP → arXiv Paper Workflow:**

1. Search DBLP for papers by topic/author
2. Identify papers with arXiv IDs
3. Use `/arxiv download` to get PDFs
4. Use `/references add` for BibTeX entries
5. Build library with both metadata and papers

**Example Flow:**
```
/references search "transformer architecture"
# Review results, note arXiv IDs (e.g., 1706.03762)
/arxiv download 1706.03762
/references add conf/nips/VaswaniSPUJGKP17 Vaswani2017
/references export references.bib
```

### With academic-writing Skill

**Bibliography for Paper Writing:**

1. Use `reference-management` to build .bib file
2. Use `academic-writing` to draft paper
3. Cite papers using citation keys
4. LaTeX automatically formats bibliography
5. Update .bib as needed during writing

**Benefits:**
- Centralized bibliography management
- Consistent citation formatting
- Easy updates and additions
- Professional reference lists

## Example Usage Scenarios

### Scenario 1: Building Bibliography for ML Paper

**Task**: Create bibliography for paper on attention mechanisms

**Process:**
1. Search DBLP: "attention mechanism AND neural networks"
2. Search authors: "Yoshua Bengio", "Geoffrey Hinton"
3. Search venue: papers from NeurIPS, ICML on attention
4. Add relevant papers (20-30 papers)
5. Export to `references.bib`
6. Use in LaTeX paper with `\cite{key}`

### Scenario 2: Tracking Researcher Output

**Task**: Monitor publications of key researcher

**Process:**
1. Search author with fuzzy matching
2. Get publication statistics
3. Identify top venues and collaborators
4. Track publication trends over years
5. Export recent papers to .bib

### Scenario 3: Conference Proceedings Review

**Task**: Review all papers from ICLR 2024

**Process:**
1. Get venue info for ICLR
2. Search papers from 2024
3. Filter by topic of interest
4. Calculate statistics on topics
5. Export selected papers

### Scenario 4: Multi-topic Literature Survey

**Task**: Survey papers across multiple topics

**Process:**
1. Search topic 1: "graph neural networks"
2. Search topic 2: "attention mechanisms"
3. Search topic 3: "few-shot learning"
4. Collect papers from all searches
5. Calculate statistics across topics
6. Export unified bibliography

### Scenario 5: Citation Network Analysis

**Task**: Map citation network for a research area

**Process:**
1. Start with seminal papers
2. Search citing/referenced papers
3. Track author collaborations
4. Identify influential venues
5. Generate statistics and visualizations

## DBLP Database Structure

### Publication Types

- **Conference Papers**: From major CS conferences
- **Journal Articles**: From CS journals
- **Workshop Papers**: From co-located workshops
- **Book Chapters**: From edited volumes
- **PhD Theses**: Doctoral dissertations
- **Technical Reports**: Preprints and reports

### Metadata Fields

Each entry includes:
- **Title**: Full paper title
- **Authors**: Complete author list
- **Venue**: Conference/journal abbreviation
- **Year**: Publication year
- **Type**: Publication type
- **DOI**: Digital Object Identifier
- **ee**: Electronic edition link
- **url**: DBLP page URL

### DBLP Keys

Format: `type/venue/AuthorsYear`

Examples:
- `conf/nips/VaswaniSPUJGKP17` - NeurIPS conference paper
- `journals/jmlr/BengioCV13` - JMLR journal article
- `phd/us/Smith2020` - PhD thesis

## Advanced Features

### Boolean Search Operators

Combine search terms effectively:

```
"neural networks" AND "attention"          # Both terms required
"transformer" OR "attention mechanism"      # Either term
"deep learning" AND (CV OR NLP)            # Nested operators
```

### Fuzzy Title Matching

Find papers with approximate titles:

- **Similarity Threshold**: 0.0-1.0 (1.0 = exact match)
- **Recommended**: Start with 0.7-0.8
- **Adjust**: Lower for more results, higher for precision

### Author Name Variations

DBLP handles different name formats:

- Full names: "Yoshua Bengio"
- Abbreviated: "Y. Bengio"
- Partial: "Bengio"
- Unicode: "François" or "Francois"

### Statistics Calculations

Available metrics:
- **Total Publications**: Count of papers
- **Time Range**: Earliest to latest
- **Top Authors**: Most prolific authors
- **Top Venues**: Most common venues
- **Year Distribution**: Papers per year

## Troubleshooting

### Paper Not Found

- Try different keyword combinations
- Use fuzzy title search with lower threshold
- Check author name spelling/format
- Verify venue abbreviation
- Search by DOI if available

### Citation Key Conflicts

- Use more specific keys (add topic/venue)
- Include middle initials for common names
- Add letters for same-author-year papers
- Check for duplicates before exporting

### BibTeX Export Issues

- Verify all papers were added successfully
- Check for invalid DBLP keys
- Ensure file path has write permissions
- Test .bib file in LaTeX before use

### Incomplete Results

- DBLP focuses on CS publications
- Recent papers may not be indexed yet
- Some venues may have delayed inclusion
- Consider using arxiv-search for preprints

## Requirements

- Internet connection for DBLP access
- `uvx` tool installed (for MCP server)
- Sufficient disk space for .bib files

## Environment Configuration

No environment variables required. The DBLP MCP server runs directly via uvx.

## Related Resources

- DBLP Website: https://dblp.org
- DBLP FAQ: https://dblp.org/faq
- BibTeX Documentation: https://www.bibtex.org
- LaTeX Bibliography Guide: https://www.latex-project.org
