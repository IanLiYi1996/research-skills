# ArXiv Paper Command

Search, download, and manage arXiv papers directly from Claude Code.

## Purpose

Access arXiv.org preprint repository:
- Search papers by keywords, authors, or categories
- Download papers to local storage
- Retrieve paper metadata
- Manage local paper library

## Usage

```
/arxiv [action] [arguments] [options]
```

**Actions:**
- `search` - Search for papers
- `download` - Download a paper by ID
- `info` - Get paper metadata
- `list` - List downloaded papers

## Search Examples

### Basic Keyword Search
```
/arxiv search "attention mechanism"
```
Searches for papers about attention mechanisms.

### Search with Category Filter
```
/arxiv search "neural networks" --category cs.LG
```
Searches in Machine Learning category only.

### Search by Author
```
/arxiv search --author "Yoshua Bengio"
```
Finds papers by specific author.

### Recent Papers
```
/arxiv search "large language models" --days 30
```
Searches papers from the last 30 days.

### Combined Filters
```
/arxiv search "diffusion models" --category cs.CV --days 90 --limit 20
```
Searches recent computer vision papers on diffusion models.

## Download Examples

### Download by arXiv ID
```
/arxiv download 2301.07041
```
Downloads the paper with specified arXiv ID.

### Download Multiple Papers
```
/arxiv download 2301.07041 2302.05442 2303.08774
```
Downloads multiple papers at once.

## Info Examples

### Get Paper Metadata
```
/arxiv info 2301.07041
```
Shows title, authors, abstract, categories, and dates.

## List Examples

### List All Downloaded Papers
```
/arxiv list
```
Shows all papers in local storage.

### List by Category
```
/arxiv list --category cs.AI
```
Lists downloaded papers in AI category.

### Search Local Library
```
/arxiv list --query "transformer"
```
Searches within downloaded papers.

## Search Options

| Option | Description | Example |
|--------|-------------|---------|
| `--category` | Filter by arXiv category | `--category cs.LG` |
| `--author` | Search by author name | `--author "John Smith"` |
| `--days` | Limit to recent N days | `--days 30` |
| `--limit` | Max results to return | `--limit 50` |
| `--sort` | Sort order (relevance/date) | `--sort date` |

## Common Categories

### Computer Science
- `cs.AI` - Artificial Intelligence
- `cs.CL` - Computation and Language
- `cs.CV` - Computer Vision
- `cs.LG` - Machine Learning
- `cs.NE` - Neural Computing
- `cs.RO` - Robotics

### Physics
- `quant-ph` - Quantum Physics
- `hep-th` - High Energy Physics
- `cond-mat` - Condensed Matter

### Mathematics
- `math.ST` - Statistics
- `math.OC` - Optimization

### Statistics
- `stat.ML` - Machine Learning
- `stat.TH` - Statistics Theory

## Output Format

### Search Results
For each paper found:
- arXiv ID
- Title
- Authors
- Primary category
- Submission date
- Abstract (truncated)

### Paper Info
Full metadata including:
- Complete author list
- Full abstract
- All categories
- Version history
- DOI/journal reference (if available)

### Download Confirmation
- Paper ID
- Download path
- File size
- Success/failure status

## Workflow Tips

1. **Start Broad**: Begin with general keywords, then narrow down
2. **Use Categories**: Combine keywords with categories for precision
3. **Check Dates**: Recent papers may not be peer-reviewed yet
4. **Batch Download**: Download multiple papers in one command
5. **Local Search**: Use `list --query` to search downloaded papers

## Environment Setup

Set custom storage path:
```bash
export ARXIV_STORAGE_PATH=~/Documents/arxiv_papers
```

Default: `~/Documents/arxiv_papers`

## Requirements

- `uv` tool installed
- Internet connection for search/download
- Sufficient disk space for PDFs
