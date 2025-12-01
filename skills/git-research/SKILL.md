---
name: git-research
description: Git version control skill for research project management. Use when tracking research code changes, managing experiment versions, collaborating on research projects, or maintaining reproducible research. Keywords include git, version control, commit, branch, merge, repository, code history, collaboration, reproducibility.
---

# Git Research Skill

This skill provides Git version control capabilities through the git MCP server for managing research projects and ensuring reproducibility.

## Core Capabilities

### 1. Repository Management

Manage Git repositories:

- **Status**: Check repository state
- **Log**: View commit history
- **Diff**: Compare changes
- **Branches**: List and manage branches

### 2. Version Control

Track research changes:

- **Stage Changes**: Add files to staging
- **Commit**: Create version snapshots
- **Revert**: Undo changes when needed
- **Tags**: Mark important versions

### 3. Collaboration

Work with others:

- **Pull**: Get latest changes
- **Push**: Share your work
- **Merge**: Combine branches
- **Conflicts**: Resolve merge conflicts

### 4. History Analysis

Understand project evolution:

- **Blame**: Track who changed what
- **Log Search**: Find specific commits
- **Statistics**: Code change metrics
- **Comparison**: Compare versions

## MCP Server Integration

This skill uses the `git` MCP server configured in the plugin. The server provides Git operations.

### Available Tools

- **git_status**: Check repository status
- **git_log**: View commit history
- **git_diff**: Show changes
- **git_branch**: Manage branches
- **git_show**: Show commit details

## Research Workflow Patterns

### Experiment Versioning

Track experiments systematically:

1. Create branch for each experiment
2. Commit after each significant change
3. Tag successful experiments
4. Document in commit messages

```
exp/baseline-model
exp/improved-architecture
exp/hyperparameter-tuning
```

### Paper Writing Workflow

Version control for manuscripts:

1. Main branch for stable version
2. Feature branches for sections
3. Regular commits during writing
4. Tags for submission versions

```
paper/introduction
paper/methods
paper/results
submission-v1
revision-v1
```

### Data Analysis Versioning

Track analysis code:

1. Commit analysis scripts
2. Document data transformations
3. Version visualization code
4. Tag reproducible states

## Best Practices for Research

### Commit Messages

Write clear, descriptive messages:

```
Good: "Add transformer attention visualization for Figure 3"
Bad: "Update code"
```

### Branch Strategy

Organize branches by purpose:

| Branch Type | Naming | Purpose |
|-------------|--------|---------|
| Main | `main` | Stable, reproducible |
| Feature | `feature/name` | New functionality |
| Experiment | `exp/name` | Research experiments |
| Paper | `paper/section` | Manuscript sections |

### Tagging Releases

Mark important milestones:

```
v1.0.0          - Initial release
submission-v1   - First submission
camera-ready    - Final version
```

### .gitignore for Research

Common patterns to ignore:

```
# Data files (too large)
data/raw/
*.csv
*.parquet

# Model checkpoints
checkpoints/
*.pt
*.pth

# Outputs
outputs/
results/

# Environment
.env
venv/
```

## Common Operations

### Check Status

View current repository state:

- Modified files
- Staged changes
- Untracked files
- Current branch

### View History

Explore project history:

- Recent commits
- Changes per commit
- Author information
- Commit timestamps

### Compare Versions

Understand changes:

- File differences
- Branch comparisons
- Tag comparisons
- Specific commit diffs

## Integration with Other Skills

- **experiment-tracking**: Version control for experiments
- **academic-writing**: Track manuscript versions
- **data-visualization**: Version analysis scripts

## Environment Configuration

Set the repository path:

```bash
export RESEARCH_GIT_PATH=/path/to/your/research/repo
```

Default: Current directory (`.`)

## Example Usage

When user requests: "Show me the recent changes to my analysis code"

Process:

1. Check git status
2. Show recent commits
3. Display diffs for relevant files
4. Summarize changes

## Reproducibility Benefits

Using Git for research ensures:

1. **Traceability**: Know exactly what code produced results
2. **Collaboration**: Work with team members safely
3. **Recovery**: Restore previous working states
4. **Documentation**: Commit messages explain changes
5. **Publication**: Share exact code versions
