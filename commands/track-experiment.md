# Experiment Tracking Command

Record, organize, and manage research experiments with comprehensive tracking.

## Purpose

Track experimental research activities:
- Log experiment parameters and configurations
- Record observations and results
- Track data files and outputs
- Manage experiment metadata
- Generate experiment reports
- Compare results across experiments

## Usage

```
/track-experiment [action] [experiment-id] [options]
```

**Actions:**
- `create`: Start new experiment
- `update`: Add data to existing experiment
- `log`: Record observation or result
- `complete`: Mark experiment as finished
- `report`: Generate experiment report
- `compare`: Compare multiple experiments
- `list`: Show all tracked experiments

## Workflow

### Creating New Experiment
1. **Initialize**: Create experiment with unique ID
2. **Configure**: Record parameters, hypothesis, methodology
3. **Setup**: Document equipment, materials, conditions
4. **Link Data**: Associate data files and code

### During Experiment
1. **Log Observations**: Record real-time observations
2. **Update Status**: Track progress and milestones
3. **Save Checkpoints**: Periodic state snapshots
4. **Document Issues**: Note problems and solutions

### After Experiment
1. **Record Results**: Final measurements and outcomes
2. **Statistical Analysis**: Calculate significance
3. **Generate Report**: Comprehensive experiment summary
4. **Archive Data**: Save all associated files

## Output

### Experiment Record
```
Experiment ID: EXP-2024-001
Title: Effect of Temperature on Reaction Rate
Status: Completed
Date: 2024-01-15 to 2024-01-20

Parameters:
- Temperature: 20°C, 40°C, 60°C, 80°C
- Catalyst: Type A (5mg/L)
- Reaction Time: 60 minutes
- Replications: 3 per condition

Results:
- Reaction rates measured
- Statistical significance: p < 0.05
- Optimal temperature: 60°C

Data Files:
- data/exp-001/raw-measurements.csv
- data/exp-001/processed-results.csv
- figures/exp-001-temperature-curve.png

Notes:
- Temperature control ±0.5°C
- All samples from same batch
- See lab notebook pages 45-52
```

### Comparison Report
Side-by-side comparison of multiple experiments with:
- Parameter differences
- Result comparisons
- Statistical analysis
- Visualization overlays

## Examples

### Create New Experiment
```
/track-experiment create --title "Drug efficacy trial" --hypothesis "Drug X reduces symptoms by >30%"
```
Initializes new experiment tracking.

### Log Observation
```
/track-experiment log EXP-2024-001 --observation "Sample showing unusual color change at 45min mark"
```
Adds timestamped observation to experiment.

### Update Results
```
/track-experiment update EXP-2024-001 --results data/trial-1-results.csv --notes "All samples within expected range"
```
Updates experiment with result data.

### Complete Experiment
```
/track-experiment complete EXP-2024-001 --success true --summary "Hypothesis confirmed with statistical significance"
```
Marks experiment as completed.

### Generate Report
```
/track-experiment report EXP-2024-001 --format markdown --output reports/exp-001-summary.md
```
Creates comprehensive experiment report.

### Compare Experiments
```
/track-experiment compare EXP-2024-001,EXP-2024-002,EXP-2024-003 --metric reaction_rate
```
Compares results across multiple experiments.

### List All Experiments
```
/track-experiment list --status active --date-range 2024-01-01:2024-03-31
```
Shows all experiments in date range.

## Database Integration

Experiments are stored in SQLite database with:
- Full text search capabilities
- Relationship tracking
- Version history
- Data integrity checks

### Schema
- **experiments**: Core experiment metadata
- **parameters**: Experimental parameters
- **observations**: Timestamped observations
- **results**: Measured outcomes
- **files**: Associated data files
- **comparisons**: Saved comparisons

## Best Practices

1. **Unique IDs**: Use systematic naming (EXP-YYYY-NNN)
2. **Detailed Parameters**: Record all conditions and settings
3. **Regular Logging**: Document as you go, not after
4. **Version Control**: Link to code/script versions used
5. **Data Backup**: Ensure all data files are backed up
6. **Reproducibility**: Include enough detail to reproduce
7. **Failure Documentation**: Record failed experiments too
8. **Statistical Analysis**: Calculate significance for all results

## Integration with Git

Track experiment code and scripts:
```
/track-experiment create --title "ML model training" --git-commit abc123 --code scripts/train_model.py
```

Links experiment to specific code version for reproducibility.
