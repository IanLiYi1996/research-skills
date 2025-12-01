---
name: experiment-tracking
description: Experiment tracking and research reproducibility skill for managing experimental procedures, recording observations, organizing data, and ensuring reproducible research. Use when designing experiments, tracking procedures, recording data, managing lab notebooks, ensuring reproducibility, or organizing experimental workflows. Keywords include experiment, tracking, lab notebook, reproducibility, data management, procedures, observations.
---

# Experiment Tracking Skill

This skill provides comprehensive tools for tracking experiments and ensuring research reproducibility.

## Core Capabilities

### 1. Experiment Design
Plan and document experimental procedures:
- Define research questions and hypotheses
- Specify independent and dependent variables
- Establish control conditions
- Plan sample sizes and replication
- Document materials and equipment
- Create standard operating procedures (SOPs)

### 2. Data Organization
Structure experimental data systematically:
- Unique experiment identifiers
- Standardized file naming conventions
- Hierarchical directory structure
- Metadata documentation
- Version control for analysis code
- Data backup strategies

### 3. Observation Recording
Capture experimental observations:
- Timestamped notes
- Quantitative measurements
- Qualitative observations
- Unexpected events or issues
- Environmental conditions
- Equipment settings and calibrations

### 4. Result Management
Track and compare experimental results:
- Store raw and processed data
- Link data to experiments
- Compare across experiments
- Track analysis versions
- Document interpretation
- Maintain audit trail

## Bundled Resources

### References

Consult `references/reproducibility-guidelines.md` for:
- Best practices for reproducible research
- Data management standards
- Documentation requirements
- Version control strategies
- Metadata standards

Consult `references/lab-notebook-standards.md` for:
- Lab notebook organization
- Entry requirements
- Dating and signing procedures
- Error correction methods
- Electronic lab notebook best practices

### Assets

Use `assets/experiment-record-template.md` for standardized experiment documentation.
Use `assets/data-organization-structure.md` for file organization guidelines.

## Workflow Patterns

### Experiment Lifecycle Workflow

1. **Planning Phase**:
   - Generate unique experiment ID
   - Document research question
   - Define hypotheses
   - Specify methodology
   - List materials and equipment
   - Plan data collection

2. **Setup Phase**:
   - Prepare materials
   - Calibrate equipment
   - Document initial conditions
   - Create data collection forms
   - Set up file structure

3. **Execution Phase**:
   - Follow protocol
   - Record observations in real-time
   - Note deviations from protocol
   - Save raw data immediately
   - Document issues or problems
   - Take photos/screenshots if relevant

4. **Analysis Phase**:
   - Process raw data
   - Run statistical analyses
   - Generate visualizations
   - Version analysis code
   - Document decisions

5. **Completion Phase**:
   - Summarize findings
   - Compare to hypotheses
   - Store all data and code
   - Archive physical samples (if applicable)
   - Update experiment database

### Data Organization Workflow

Recommended structure:
```
experiments/
├── EXP-2024-001/
│   ├── protocol.md
│   ├── raw-data/
│   │   ├── trial-1.csv
│   │   ├── trial-2.csv
│   │   └── trial-3.csv
│   ├── processed-data/
│   │   └── cleaned-data.csv
│   ├── analysis/
│   │   ├── analysis.py
│   │   └── results.txt
│   ├── figures/
│   │   └── result-plot.png
│   └── notes.md
```

### Database Integration Workflow

Store experiment metadata in SQLite database:

**Table: experiments**
- experiment_id (unique)
- title
- date_start
- date_end
- researcher
- hypothesis
- status (planned/active/completed)

**Table: observations**
- observation_id
- experiment_id (foreign key)
- timestamp
- observation_type
- value
- notes

**Table: data_files**
- file_id
- experiment_id (foreign key)
- file_path
- file_type (raw/processed/analysis)
- description

## Best Practices

### Documentation Standards
- Document in real-time (not retrospectively)
- Be specific and detailed
- Include units for all measurements
- Note any deviations from protocol
- Date and time all entries
- Sign off on critical steps

### File Naming Conventions
- Use consistent format: `EXP-YYYY-NNN_description_YYYYMMDD`
- Include experiment ID
- Use descriptive names
- Avoid spaces (use hyphens or underscores)
- Include dates for time-sensitive files

### Version Control
- Use Git for analysis code
- Track major revisions
- Meaningful commit messages
- Tag important versions
- Link commits to experiment IDs

### Reproducibility Checklist
- [ ] Protocol documented completely
- [ ] All parameters recorded
- [ ] Equipment settings noted
- [ ] Software versions documented
- [ ] Random seeds specified (if applicable)
- [ ] Raw data preserved
- [ ] Analysis code available
- [ ] Dependencies listed
- [ ] Workflow documented

## Integration with Other Tools

- **MCP Database**: Store experiment metadata
- **MCP Filesystem**: Organize data files
- **MCP Git**: Version control for code
- **Lab Equipment**: Integrate measurements automatically where possible

## Example Usage

When user requests: "Start tracking a new experiment on catalyst effectiveness"

Process:
1. Generate unique ID: EXP-2024-042
2. Create experiment record with:
   - Title: "Catalyst X effectiveness at varying temperatures"
   - Hypothesis: "Catalyst X shows increased activity at 60°C"
   - Variables: Temperature (IV), reaction rate (DV)
   - Materials: List of chemicals and equipment
   - Protocol: Step-by-step procedure
3. Set up directory structure
4. Create data collection form
5. Insert metadata into database
6. Ready for execution

When user requests: "Compare results across my last 5 experiments"

Process:
1. Query database for last 5 experiments
2. Retrieve experiment metadata
3. Load result data for each
4. Create comparison table
5. Generate visualization showing trends
6. Highlight significant differences
7. Provide statistical comparison

Always maintain detailed records and ensure all work is reproducible.
