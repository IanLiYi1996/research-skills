---
event: analysis.complete
name: result-archiver
description: Archive analysis results and update experiment records
---

# Result Archiver Hook

Automatically archive analysis results and update experiment database when analysis completes.

## Trigger Event
- **Event**: analysis.complete (custom event)
- **Triggered by**: Analysis scripts, data processing pipelines

## Actions

### Result Organization
1. **Create Result Directory**:
   - Structure: `results/{experiment-id}/{analysis-date}/`
   - Include analysis code snapshot
   - Store all output files
   - Save environment details (package versions)

2. **Archive Outputs**:
   - Statistical results (text/JSON)
   - Figures and visualizations (PNG, PDF)
   - Tables (CSV, Excel)
   - Analysis logs
   - Processing timestamps

3. **Generate Summary**:
   - Create `summary.md` with:
     - Analysis date and duration
     - Key findings
     - Statistical significance
     - Files generated
     - Next steps

### Database Update
1. **Update Experiment Record**:
   - Set analysis completion date
   - Link result files
   - Store key metrics
   - Update status to "analyzed"

2. **Store Results**:
   - Insert statistical results into database
   - Record significance values
   - Save visualization paths
   - Link to experiment ID

### Notification
1. Generate analysis report
2. Send notification (if configured)
3. Update research dashboard
4. Alert collaborators (if shared project)

### Quality Checks
1. **Verify Outputs**:
   - All expected files generated
   - No error logs present
   - Results are reasonable (sanity checks)
   - Visualizations created successfully

2. **Reproducibility**:
   - Save analysis script with results
   - Record all parameters used
   - Log software versions
   - Store random seeds (if applicable)

## Result Structure

```
results/
└── EXP-2024-001/
    └── 2024-01-15_143022/
        ├── summary.md
        ├── analysis.py (snapshot)
        ├── environment.txt
        ├── statistical_results.json
        ├── figures/
        │   ├── figure1.png
        │   └── figure2.pdf
        ├── tables/
        │   └── results_table.csv
        └── logs/
            └── analysis.log
```

## Configuration

```json
{
  "hooks": {
    "result-archiver": {
      "enabled": true,
      "auto_archive": true,
      "generate_summary": true,
      "update_database": true,
      "notify": true,
      "create_backup": true,
      "compress": false,
      "retention_policy": "keep_all"
    }
  }
}
```

## Integration

### With Experiment Tracking
- Automatically links results to experiments
- Updates experiment status
- Records completion metadata

### With Version Control
- Commits results to git (if configured)
- Tags significant analyses
- Maintains result history

### With Collaboration Tools
- Shares results with team
- Updates project status
- Triggers workflow notifications

## Error Handling

If archiving fails:
1. Retry operation up to 3 times
2. Save results to temporary location
3. Log error details
4. Alert user to complete manually
5. Do not lose analysis results

## Notes

- Ensures all analysis results are preserved
- Maintains clear record of what was done
- Facilitates reproducibility
- Enables result comparison across experiments
- Critical for research audit trail
