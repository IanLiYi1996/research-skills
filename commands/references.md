# References Command

Search DBLP database and manage BibTeX bibliographies for academic publications.

## Purpose

Manage academic references efficiently:
- Search DBLP computer science bibliography
- Find papers by keywords, authors, or titles
- Collect citations for research papers
- Generate BibTeX files for LaTeX documents
- Analyze publication statistics

## Usage

```bash
/references [action] [arguments] [options]
```

**Actions:**
- `search` - Search by keywords with boolean operators
- `author` - Find publications by author name
- `title` - Fuzzy search by paper title
- `venue` - Get information about conference/journal
- `add` - Add paper to bibliography collection
- `export` - Export collected papers to .bib file
- `stats` - Calculate statistics from results

## Search Examples

### Basic Keyword Search

```bash
/references search "machine learning"
```

Searches for papers mentioning "machine learning".

### Boolean Search

```bash
/references search "attention AND transformer"
```

Searches for papers with both terms.

### Combined Terms

```bash
/references search "(neural OR deep) AND learning"
```

Uses boolean operators for complex queries.

### Search with Filters

```bash
/references search "computer vision" --max-results 20 --year-from 2020
```

Limits results to recent papers.

## Author Search Examples

### Basic Author Search

```bash
/references author "Yoshua Bengio"
```

Finds all publications by Yoshua Bengio.

### Author with Options

```bash
/references author "Geoffrey Hinton" --max-results 30
```

Gets author publications with result limit.

### Fuzzy Author Matching

```bash
/references author "Bengio" --similarity 0.8
```

Finds authors matching "Bengio" with 80% similarity.

## Title Search Examples

### Fuzzy Title Match

```bash
/references title "Attention Is All You Need" --similarity 0.9
```

Finds papers with titles similar to query.

### Approximate Title

```bash
/references title "transformer architecture" --similarity 0.7
```

Broader matching with lower similarity threshold.

## Venue Information Examples

### Get Venue Info

```bash
/references venue "ICML"
```

Shows information about ICML conference.

### Check Journal

```bash
/references venue "JMLR"
```

Gets details about JMLR journal.

## Add to Bibliography Examples

### Add Single Paper

```bash
/references add conf/nips/VaswaniSPUJGKP17 Vaswani2017
```

Adds paper with custom citation key "Vaswani2017".

### Add Multiple Papers

```bash
/references add conf/icml/GoodfellowPMXWOCB14 GAN2014
/references add conf/iclr/KingmaW14 VAE2014
/references add conf/nips/HoJA20 DDPM2020
```

Adds several papers in sequence.

### Batch Add

```bash
/references add \
  conf/nips/VaswaniSPUJGKP17 Vaswani2017 \
  conf/acl/DevlinCLT19 BERT2019 \
  conf/nips/BrownMRSKDNSSAA20 GPT3-2020
```

Adds multiple papers in one command.

## Export Examples

### Export Bibliography

```bash
/references export references.bib
```

Exports all collected papers to `references.bib`.

### Export with Path

```bash
/references export ~/Documents/paper/bibliography.bib
```

Exports to specific file path.

### Export After Collection

```bash
# Collect papers
/references search "attention mechanism"
/references add conf/nips/VaswaniSPUJGKP17 Vaswani2017
/references add conf/iclr/BahdanauCB15 Bahdanau2015

# Export to file
/references export attention_papers.bib
```

Complete workflow from search to export.

## Statistics Examples

### Calculate Search Statistics

```bash
/references search "deep learning" --stats
```

Shows statistics about search results.

### Author Statistics

```bash
/references author "Yann LeCun" --stats
```

Displays publication statistics for author.

## Search Options

| Option | Description | Example |
|--------|-------------|---------|
| `--max-results` | Maximum number of results | `--max-results 50` |
| `--year-from` | Start year for filtering | `--year-from 2020` |
| `--year-to` | End year for filtering | `--year-to 2024` |
| `--venue-filter` | Filter by venue substring | `--venue-filter "icml"` |
| `--similarity` | Similarity threshold (0-1) | `--similarity 0.8` |
| `--stats` | Include statistics | `--stats` |

## Common Venues

### Machine Learning Conferences

| Abbrev. | Full Name |
|---------|-----------|
| NeurIPS | Neural Information Processing Systems |
| ICML | International Conference on Machine Learning |
| ICLR | International Conference on Learning Representations |
| AISTATS | Artificial Intelligence and Statistics |

### NLP Conferences

| Abbrev. | Full Name |
|---------|-----------|
| ACL | Association for Computational Linguistics |
| EMNLP | Empirical Methods in NLP |
| NAACL | North American Chapter of ACL |
| COLING | International Conference on Computational Linguistics |

### Computer Vision

| Abbrev. | Full Name |
|---------|-----------|
| CVPR | Computer Vision and Pattern Recognition |
| ICCV | International Conference on Computer Vision |
| ECCV | European Conference on Computer Vision |

### Top Journals

| Abbrev. | Full Name |
|---------|-----------|
| JMLR | Journal of Machine Learning Research |
| TPAMI | IEEE Trans. on Pattern Analysis and Machine Intelligence |
| TACL | Transactions of the Association for Computational Linguistics |

## Output Format

### Search Results

For each paper found:
```
Title: Attention Is All You Need
Authors: Ashish Vaswani, Noam Shazeer, ...
Venue: NeurIPS 2017
Type: Conference Paper
DBLP Key: conf/nips/VaswaniSPUJGKP17
URL: https://dblp.org/rec/conf/nips/VaswaniSPUJGKP17
```

### Author Results

For author queries:
```
Author: Yoshua Bengio
Total Publications: 500+
Recent Papers:
  - Paper 1 (2024)
  - Paper 2 (2023)
  - ...
Top Venues: NeurIPS, ICML, ICLR
```

### Venue Information

For venue queries:
```
Venue: NeurIPS
Full Name: Neural Information Processing Systems
Type: Conference
Acronym: NeurIPS (formerly NIPS)
URL: https://dblp.org/db/conf/nips/
```

### Statistics Output

For stats requests:
```
Total Publications: 42
Time Range: 2018 - 2024
Top Authors:
  1. Yoshua Bengio (12 papers)
  2. Geoffrey Hinton (8 papers)
  3. Yann LeCun (6 papers)
Top Venues:
  1. NeurIPS (15 papers)
  2. ICML (12 papers)
  3. ICLR (10 papers)
```

## Complete Workflow Examples

### Workflow 1: Build Paper Bibliography

```bash
# Search for papers on topic
/references search "graph neural networks" --year-from 2020

# Add relevant papers
/references add journals/corr/abs-2005-00687 GNN-Survey-2020
/references add conf/iclr/VelickovicCCRLB18 GAT2018
/references add conf/nips/KipfW17 GCN2017

# Export to file
/references export gnn_bibliography.bib

# Verify export
cat gnn_bibliography.bib
```

### Workflow 2: Track Researcher

```bash
# Find author publications
/references author "Yann LeCun" --max-results 20

# Get statistics
/references author "Yann LeCun" --stats

# Add recent papers
/references add conf/iclr/LeCunBH15 LeCun2015
/references add journals/nature/LeCunBH15 DeepLearning2015

# Export collected works
/references export lecun_papers.bib
```

### Workflow 3: Conference Proceedings Review

```bash
# Search specific venue
/references search "ICLR 2024" --venue-filter "iclr"

# Get venue information
/references venue "ICLR"

# Add interesting papers
/references add conf/iclr/... Paper2024a
/references add conf/iclr/... Paper2024b

# Export conference selection
/references export iclr2024_selection.bib
```

### Workflow 4: Multi-topic Survey

```bash
# Search topic 1
/references search "attention mechanism" --year-from 2017

# Search topic 2
/references search "transformer architecture" --year-from 2017

# Search topic 3
/references search "self-attention" --year-from 2017

# Collect key papers from all searches
/references add conf/nips/VaswaniSPUJGKP17 Transformer2017
/references add conf/iclr/BahdanauCB15 AttentionSeq2Seq2015
/references add conf/acl/DevlinCLT19 BERT2019
/references add conf/nips/BrownMRSKDNSSAA20 GPT3-2020

# Export survey bibliography
/references export attention_survey.bib
```

### Workflow 5: Integration with arXiv

```bash
# Search DBLP for papers
/references search "diffusion models" --year-from 2020

# Note arXiv IDs from results (e.g., 2006.11239)

# Download papers from arXiv
/arxiv download 2006.11239
/arxiv download 2011.13456

# Add BibTeX entries from DBLP
/references add conf/nips/HoJA20 DDPM2020
/references add conf/iclr/SongE20 ScoreMatching2020

# Export bibliography
/references export diffusion_papers.bib
```

## Citation Key Conventions

### Recommended Formats

**Single Author:**
```
Smith2024
Smith2024ML
Smith2024Attention
```

**Two Authors:**
```
SmithJones2024
SmithJones2024Survey
```

**Three or More:**
```
Smith2024              # First author only
SmithEtAl2024         # With et al.
Transformer2017        # By paper name
```

**Venue-Based:**
```
ICML24Smith
NeurIPS23DeepLearning
ACL24BERT
```

**Disambiguation:**
```
Smith2024a            # Multiple papers same year
Smith2024b
SmithNLP2024         # By research area
SmithCV2024
```

## Integration with Other Tools

### With arXiv Command

```bash
# Search DBLP
/references search "large language models"

# Find arXiv ID in results
# Download from arXiv
/arxiv download 2303.08774

# Add DBLP entry
/references add journals/corr/abs-2303-08774 GPT4-2023

# Export
/references export llm_papers.bib
```

### With LaTeX

```latex
\documentclass{article}
\usepackage{natbib}

\begin{document}

The transformer architecture \cite{Vaswani2017}
revolutionized NLP, leading to models like
BERT \cite{BERT2019} and GPT-3 \cite{GPT3-2020}.

\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

### With Reference Managers

```bash
# Export from DBLP
/references export papers.bib

# Import into Zotero/Mendeley/EndNote
# (use software's import function)

# Continue managing in reference manager
```

## Workflow Tips

1. **Start Broad**: Begin with general keywords, then refine
2. **Use Filters**: Leverage venue and date filters for precision
3. **Batch Operations**: Collect multiple papers before exporting
4. **Consistent Keys**: Follow citation key conventions
5. **Verify Results**: Check papers before adding to bibliography
6. **Regular Backups**: Export .bib files frequently
7. **Test LaTeX**: Compile with LaTeX to verify format
8. **Track Sources**: Note where papers came from
9. **Update Regularly**: Refresh bibliography as research progresses
10. **Document Choices**: Keep notes on selection criteria

## Common Issues

### Paper Not Found

- Try different keyword combinations
- Use fuzzy title search
- Search by author instead
- Check venue abbreviation
- Verify paper is in DBLP (CS focus)

### Too Many Results

- Add more specific keywords
- Use venue filters
- Narrow year range
- Focus on top-tier venues
- Add author constraints

### Export Failures

- Check DBLP keys are valid
- Verify file path permissions
- Use absolute paths
- Retry with smaller batches
- Check disk space

### Citation Key Conflicts

- Use more specific keys
- Add topic/venue suffix
- Include year variants (a, b, c)
- Check for duplicates first
- Follow naming convention

## Requirements

- Internet connection for DBLP access
- `uvx` tool installed (for mcp-dblp)
- Sufficient disk space for .bib files
- LaTeX for testing (optional)

## Environment Setup

No environment variables required. The DBLP MCP server runs via uvx automatically.

## Best Practices

1. **Plan First**: Define scope before searching
2. **Organize**: Group papers by topic/category
3. **Name Consistently**: Follow citation key conventions
4. **Verify Quality**: Check venue reputation
5. **Document**: Keep notes on selection criteria
6. **Backup**: Save .bib files regularly
7. **Test**: Compile LaTeX to verify
8. **Version Control**: Track .bib changes with git
9. **Collaborate**: Share bibliographies with team
10. **Update**: Keep bibliography current

## Related Commands

- `/arxiv` - Download papers from arXiv
- `/summarize` - Summarize downloaded papers
- `/latex` - Create LaTeX documents
- `/git` - Version control for bibliography
