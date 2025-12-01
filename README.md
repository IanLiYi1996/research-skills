# Research Skills - Claude Code Plugin

Comprehensive research and analysis toolkit for academic workflows. This Claude Code plugin provides specialized commands, agents, skills, and automation for literature review, data analysis, paper writing, and experiment tracking.

## Features

### 🔧 Commands

Custom slash commands for common research tasks:

- **`/analyze`** - Data analysis and visualization with statistical summaries
- **`/summarize`** - Research paper summarization and key findings extraction
- **`/search-papers`** - Literature search across academic databases
- **`/track-experiment`** - Experiment tracking and result management

### 🤖 Agents

Specialized AI agents for research workflows:

- **`research-assistant`** - Academic research specialist for literature review and citation management
- **`data-analyst`** - Statistical analysis and data visualization expert
- **`experiment-manager`** - Experiment tracking and reproducibility specialist
- **`writing-assistant`** - Academic writing and manuscript preparation expert

### 🎓 Skills

Advanced capabilities with bundled resources:

- **`academic-research`** - Literature review, citation generation, research synthesis
- **`data-visualization`** - Publication-quality charts and statistical analysis
- **`academic-writing`** - Manuscript drafting and scholarly writing
- **`experiment-tracking`** - Reproducible research and data management

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

# Set environment variable (for web search)
export BRAVE_API_KEY=<your-api-key>
```

## Quick Start

### Using Commands

```bash
/analyze data/experiment-results.csv
/summarize papers/smith-2024-ml-paper.pdf
/search-papers "machine learning interpretability"
/track-experiment create --title "Drug efficacy study"
```

### Using Agents

```
Help me conduct a systematic literature review
Use data-analyst to compare treatment groups
Launch experiment-manager to set up my experiment
```

### Using Skills

Skills trigger automatically based on keywords:

```
"Help me conduct a systematic literature review"
[Triggers academic-research skill]

"Create scatter plot for temperature vs pressure"
[Triggers data-visualization skill]
```

## Documentation

- [Getting Started Guide](docs/getting-started.md)
- [Commands Reference](commands/)
- [Skills Documentation](skills/)

## License

MIT License - see [LICENSE](LICENSE)

## Version

1.0.0