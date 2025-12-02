# Research Skills - Claude Code Plugin

Comprehensive research and analysis toolkit for academic workflows. This Claude Code plugin provides specialized commands, agents, skills, and automation for literature review, data analysis, paper writing, and experiment tracking.

## Features

### 🔧 Commands

Custom slash commands for common research tasks:

- **`/analyze`** - Data analysis and visualization with statistical summaries
- **`/summarize`** - Research paper summarization and key findings extraction
- **`/search-papers`** - Literature search across academic databases
- **`/track-experiment`** - Experiment tracking and result management
- **`/arxiv`** - Search, download, and manage arXiv papers
- **`/latex`** - Create and format LaTeX documents, equations, tables, and figures
- **`/huggingface`** - Search HuggingFace Hub for models and datasets
- **`/fetch`** - Fetch and retrieve content from web URLs
- **`/git`** - Git version control for research projects
- **`/slides`** - Create and export presentations (Slidev and python-pptx)

### 🤖 Agents

Specialized AI agents for research workflows:

- **`research-assistant`** - Academic research specialist for literature review and citation management
- **`data-analyst`** - Statistical analysis and data visualization expert
- **`experiment-manager`** - Experiment tracking and reproducibility specialist
- **`writing-assistant`** - Academic writing and manuscript preparation expert
- **`latex-expert`** - LaTeX typesetting and journal paper formatting specialist
- **`presentation-creator`** - Presentation design specialist for slides and talks

### 🎓 Skills

Advanced capabilities with bundled resources:

- **`academic-research`** - Literature review, citation generation, research synthesis
- **`data-visualization`** - Publication-quality charts and statistical analysis
- **`academic-writing`** - Manuscript drafting and scholarly writing
- **`experiment-tracking`** - Reproducible research and data management
- **`arxiv-search`** - arXiv paper search, download, and metadata retrieval
- **`latex-writing`** - LaTeX templates, cheatsheet, and paper formatting
- **`huggingface`** - HuggingFace Hub model and dataset search
- **`web-fetch`** - Web content fetching and resource retrieval
- **`git-research`** - Git version control for research reproducibility
- **`context7-docs`** - Real-time code documentation retrieval
- **`slidev-presentation`** - Markdown-based presentations with Slidev
- **`pptx-generation`** - Programmatic PowerPoint generation with python-pptx

### ⚡ Automation (Hooks)

Event-driven automation for research workflows:

- **`auto-formatter`** - Format code and documents on save
- **`research-validator`** - Validate research files before git commits
- **`data-backup`** - Automatic data backup and versioning
- **`result-archiver`** - Archive analysis results and update records

## Installation

### Quick Install

```bash
# Add marketplace
/plugin marketplace add IanLiYi1996/research-skills

# Install plugin
/plugin install research-toolkit@research-skills

# Set environment variables (required)
export TAVILY_API_KEY=<your-api-key>          # For web search (Tavily)
export CONTEXT7_API_KEY=<your-api-key>        # For code documentation (Context7)

# HuggingFace uses OAuth authentication - follow the browser prompt on first use

# Optional environment variables (with defaults)
export ARXIV_STORAGE_PATH=~/Documents/arxiv_papers  # Default: ./arxiv_papers
export RESEARCH_FS_PATH=.                     # Filesystem access path, default: current directory
export RESEARCH_GIT_PATH=.                    # Git repository path, default: current directory
```

### Prerequisites

- **uv** - Required for arXiv, fetch, and git MCP servers. Install via:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

## Quick Start

### Using Commands

```bash
/analyze data/experiment-results.csv
/summarize papers/smith-2024-ml-paper.pdf
/search-papers "machine learning interpretability"
/track-experiment create --title "Drug efficacy study"
/arxiv search "transformer architecture" --category cs.LG
/huggingface search-models --task text-generation --limit 10
/fetch https://arxiv.org/abs/2301.07041
/git status
/slides new presentation.md --format slidev --topic "My Research"
```

### Using Agents

```
Help me conduct a systematic literature review
Use data-analyst to compare treatment groups
Launch experiment-manager to set up my experiment
Create a presentation for my thesis defense using presentation-creator
```

### Using Skills

Skills trigger automatically based on keywords:

```
"Help me conduct a systematic literature review"
[Triggers academic-research skill]

"Create scatter plot for temperature vs pressure"
[Triggers data-visualization skill]

"Search arXiv for recent papers on diffusion models"
[Triggers arxiv-search skill]

"Find a good model for sentiment analysis on HuggingFace"
[Triggers huggingface skill]

"Create slides for my conference presentation"
[Triggers slidev-presentation skill]

"use context7 - How do I use React hooks?"
[Triggers context7-docs skill]
```

## Documentation

- [Getting Started Guide](docs/getting-started.md)
- [Commands Reference](commands/)
- [Skills Documentation](skills/)

## License

MIT License - see [LICENSE](LICENSE)

## Version

1.0.0