# Getting Started with Research Skills Plugin

This guide will help you set up and start using the Research Skills plugin for Claude Code.

## Prerequisites

Before installing the plugin, ensure you have:

- ✅ **Claude Code** installed and working
- ✅ **Node.js** (v16+) installed for MCP servers
- ✅ **Python 3.8+** (optional, for skill scripts)
- ✅ **Git** (for version control features)

### Verify Prerequisites

```bash
# Check Claude Code
claude --version

# Check Node.js
node --version

# Check Python (optional)
python3 --version

# Check Git
git --version
```

## Installation

### Step 1: Add Plugin Marketplace

```bash
/plugin marketplace add IanLiYi1996/research-skills
```

This adds the plugin marketplace to Claude Code.

### Step 2: Install Plugin

```bash
/plugin install research-toolkit@research-skills
```

Wait for installation to complete. You should see confirmation message.

### Step 3: Verify Installation

```bash
/help
```

Check that new commands are listed:
- `/analyze`
- `/summarize`
- `/search-papers`
- `/track-experiment`

## Configuration

### Environment Variables

For web search functionality, set up Tavily API:

1. **Get API Key**: Visit [Tavily](https://tavily.com) and sign up
2. **Set Environment Variable**:
   ```bash
   export TAVILY_API_KEY=your_api_key_here
   ```
3. **Make Permanent** (add to `~/.zshrc` or `~/.bashrc`):
   ```bash
   echo 'export TAVILY_API_KEY=your_api_key_here' >> ~/.zshrc
   source ~/.zshrc
   ```

### MCP Servers

The plugin uses four MCP servers:

1. **Filesystem** - Local file access (no config needed)
2. **Tavily Search** - AI-powered web search (requires API key above)
3. **SQLite** - Database storage (auto-configured)
4. **Git** - Version control (auto-configured)
5. **ArXiv** - Academic paper search and download (requires `uv` installed)

To verify MCP servers work:

```bash
npx @modelcontextprotocol/server-filesystem --help
```

## First Steps

### 1. Try a Command

Test the plugin with a simple command:

```bash
/analyze --help
```

This shows the analyze command documentation.

### 2. Use an Agent

Ask for help from a specialized agent:

```
Can you help me using the research-assistant agent?
```

### 3. Trigger a Skill

Skills activate based on keywords:

```
Help me conduct a literature review on climate change
```

The `academic-research` skill should activate automatically.

## Common Workflows

### Literature Review Workflow

**Goal**: Conduct a systematic literature review

**Steps**:

1. **Search for papers**:
   ```bash
   /search-papers "machine learning interpretability" --year 2020-2024
   ```

2. **Ask for review help**:
   ```
   Help me conduct a systematic review of machine learning interpretability papers
   ```

3. **The academic-research skill will guide you**:
   - Define research question
   - Develop search strategy
   - Screen papers
   - Extract data
   - Synthesize findings

4. **Generate citations**:
   The skill includes a citation generator script:
   ```bash
   python skills/academic-research/scripts/citation_generator.py \
     --input paper-metadata.json \
     --format apa
   ```

5. **Use templates**:
   - Literature review template: `skills/academic-research/assets/literature-review-template.md`
   - Annotation template: `skills/academic-research/assets/annotation-template.md`

### Data Analysis Workflow

**Goal**: Analyze experimental data and create visualizations

**Steps**:

1. **Analyze data**:
   ```bash
   /analyze data/experiment-results.csv
   ```

2. **Request specific analysis**:
   ```
   Compare treatment groups A and B and test for statistical significance
   ```

3. **The data-visualization skill provides**:
   - Descriptive statistics
   - Appropriate statistical tests
   - Publication-quality visualizations
   - Plain-language interpretation

4. **Refine visualizations**:
   ```
   Create a box plot comparing groups with p-values indicated
   ```

### Manuscript Writing Workflow

**Goal**: Write a research paper section

**Steps**:

1. **Request help**:
   ```
   Help me write the introduction for my paper on renewable energy adoption
   ```

2. **The academic-writing skill will**:
   - Structure introduction (funnel approach)
   - Maintain academic tone
   - Integrate citations properly
   - Follow journal conventions

3. **Review and refine**:
   ```
   Improve this methods section for clarity and completeness
   ```

4. **Use templates**:
   - Manuscript template: `skills/academic-writing/assets/manuscript-template.md`
   - Abstract template: `skills/academic-writing/assets/abstract-template.md`

### Experiment Tracking Workflow

**Goal**: Track an experiment with full documentation

**Steps**:

1. **Create experiment**:
   ```bash
   /track-experiment create \
     --title "Catalyst effectiveness study" \
     --hypothesis "Catalyst X increases reaction rate at 60°C"
   ```

2. **Log observations during experiment**:
   ```bash
   /track-experiment log EXP-2024-001 \
     --observation "Sample showing unusual color at 45min"
   ```

3. **Update with results**:
   ```bash
   /track-experiment update EXP-2024-001 \
     --results data/trial-results.csv
   ```

4. **Generate report**:
   ```bash
   /track-experiment report EXP-2024-001 \
     --format markdown
   ```

## Understanding Plugin Components

### Commands

Commands are invoked with `/command-name`:

- Direct, action-oriented
- Take parameters and options
- Return structured results
- Best for specific, repeatable tasks

### Agents

Agents are specialized AI personas:

- Invoked by mentioning their name
- Provide expert guidance
- Understand domain-specific context
- Best for complex, multi-step tasks

### Skills

Skills are advanced capabilities:

- Trigger automatically based on keywords
- Include bundled resources (scripts, references, templates)
- Provide comprehensive workflows
- Best for complete processes (e.g., systematic review)

### Hooks

Hooks are automated actions:

- Trigger on events (file save, git commit)
- Run in background
- Ensure quality and consistency
- Configurable per project

## Tips and Best Practices

### Using Commands

✅ **Do**:
- Use `/help` to see available commands
- Check command documentation with `--help` flag
- Provide full file paths for clarity

❌ **Don't**:
- Forget the `/` prefix
- Assume commands work without parameters
- Mix command syntax with natural language

### Using Agents

✅ **Do**:
- Be specific about what you need
- Mention agent by name when switching contexts
- Provide relevant context and files

❌ **Don't**:
- Expect agents to guess missing information
- Switch agents mid-task without context
- Assume all agents have access to external tools

### Using Skills

✅ **Do**:
- Use keywords from skill descriptions
- Be explicit about your goal
- Follow guided workflows
- Utilize bundled resources (scripts, templates)

❌ **Don't**:
- Expect skills to trigger on vague requests
- Ignore workflow guidance
- Skip documentation in references/

### Data Organization

Follow these conventions:

```
your-research-project/
├── papers/              # PDFs and paper notes
├── data/
│   ├── raw/            # Original data (never modify)
│   ├── processed/      # Cleaned data
│   └── results/        # Analysis outputs
├── experiments/        # Experiment records
│   └── EXP-YYYY-NNN/
├── code/               # Analysis scripts
├── figures/            # Visualizations
├── manuscripts/        # Paper drafts
└── references/         # Bibliography files
```

## Troubleshooting

### Plugin Not Found

**Problem**: `/plugin install` says plugin not found

**Solution**:
1. Verify marketplace added: `/plugin marketplace list`
2. Re-add marketplace: `/plugin marketplace add /path/to/research-skills`
3. Try full plugin name: `research-toolkit@research-skills`

### Commands Not Working

**Problem**: Commands not recognized

**Solution**:
1. Check plugin installed: `/plugin list`
2. Verify command exists: `/help`
3. Restart Claude Code
4. Check for typos (commands are case-sensitive)

### Skills Not Triggering

**Problem**: Skills don't activate

**Solution**:
1. Use more specific keywords from skill descriptions
2. Be explicit: "Use the academic-research skill to..."
3. Check skill is properly loaded: Look for skills in plugin info

### MCP Server Errors

**Problem**: "MCP server not available" error

**Solution**:
1. Test MCP server directly:
   ```bash
   npx @modelcontextprotocol/server-filesystem --help
   ```
2. Check Node.js installed: `node --version`
3. For Tavily Search, verify API key:
   ```bash
   echo $TAVILY_API_KEY
   ```
4. Restart Claude Code after setting environment variables

### Python Scripts Not Running

**Problem**: Skill scripts fail to execute

**Solution**:
1. Verify Python installed: `python3 --version`
2. Install dependencies if needed:
   ```bash
   pip install -r requirements.txt
   ```
3. Check script has execute permissions:
   ```bash
   chmod +x skills/*/scripts/*.py
   ```
4. Use full path to Python: `python3 script.py` instead of `./script.py`

## Next Steps

Now that you're set up:

1. **Explore Commands**: Try each `/command` to see what it does
2. **Meet the Agents**: Have conversations with each agent
3. **Try a Workflow**: Complete one of the workflows above
4. **Read Skill Docs**: Explore `skills/*/SKILL.md` for detailed capabilities
5. **Configure Hooks**: Customize automation in hooks/

## Getting Help

- **Command Help**: `/command-name --help`
- **Plugin Info**: `/plugin info research-toolkit`
- **Claude Code Docs**: https://code.claude.com/docs
- **Skill References**: See `skills/*/references/` for detailed guides

## Advanced Usage

### Custom Templates

Create your own templates by copying and modifying:

```bash
cp skills/academic-research/assets/literature-review-template.md \
   my-custom-review-template.md
```

### Multiple Experiments

Track many experiments systematically:

```bash
# List all experiments
/track-experiment list

# Compare experiments
/track-experiment compare EXP-2024-001,EXP-2024-002,EXP-2024-003
```

### Batch Processing

Analyze multiple files:

```bash
/analyze data/*.csv --batch
```

### Integration with Git

The plugin integrates with Git:

- Hooks validate before commits
- Experiments link to code versions
- Data changes tracked automatically

## Best Practices Summary

1. **Organization**: Use consistent file structure
2. **Documentation**: Document as you go, not after
3. **Version Control**: Use Git for all research files
4. **Reproducibility**: Record all parameters and settings
5. **Validation**: Let hooks catch errors before commits
6. **Templates**: Use provided templates for consistency
7. **Citation**: Always generate proper citations
8. **Backup**: Enable data backup hook

---

**You're all set!** Start with a simple workflow and gradually explore more features.

Happy researching! 🎓
