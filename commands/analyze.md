# Data Analysis Command

Perform comprehensive statistical analysis and visualization on research datasets.

## Purpose

Analyze research data with:
- Statistical summaries (mean, median, standard deviation, quartiles)
- Data quality assessment (missing values, outliers, data types)
- Trend identification and pattern recognition
- Correlation analysis between variables
- Visualization generation (charts, graphs, heatmaps)

## Usage

```
/analyze [dataset-path] [options]
```

**Parameters:**
- `dataset-path`: Path to the data file (CSV, JSON, Excel, or TSV)
- `options` (optional): Analysis preferences (e.g., specific columns, chart types)

## Workflow

1. **Load Dataset**: Read the data file using appropriate parsers
2. **Inspect Structure**: Examine columns, data types, and dimensions
3. **Data Quality Check**: Identify missing values, duplicates, and potential issues
4. **Statistical Analysis**: Calculate descriptive statistics for numerical columns
5. **Visualization**: Generate relevant charts based on data characteristics
6. **Report Generation**: Create a comprehensive markdown report with findings

## Output

The analysis generates:

### Summary Statistics Table
- Count, mean, median, mode, standard deviation
- Min, max, quartiles (Q1, Q2, Q3)
- Unique values and frequency distributions

### Data Quality Report
- Missing value counts and percentages
- Data type distribution
- Outlier detection results
- Duplicate row identification

### Visualizations
- Distribution plots for numerical data
- Bar charts for categorical data
- Correlation heatmaps for multivariate analysis
- Time series plots (if temporal data present)

### Analysis Report
- Key findings and insights
- Data anomalies and recommendations
- Export-ready charts (PNG/SVG format)

## Examples

### Basic Analysis
```
/analyze data/survey-results.csv
```
Performs complete analysis on survey data with default settings.

### Analyze Specific Columns
```
/analyze experiments/trial-001.json --columns temperature,pressure,outcome
```
Focuses analysis on specified columns.

### Generate Specific Visualizations
```
/analyze datasets/user-study.xlsx --charts scatter,histogram,box
```
Creates specific chart types for the dataset.

### Time Series Analysis
```
/analyze logs/sensor-data.csv --timeseries --datetime-column timestamp
```
Analyzes temporal patterns in sensor data.

## Requirements

- **File Format**: Supports CSV, JSON, Excel (.xlsx, .xls), and TSV
- **Minimum Data**: At least 10 data points recommended for statistical validity
- **CSV Files**: Must include header row with column names
- **JSON Files**: Should be array of objects or have consistent structure

## Best Practices

1. **Clean Data First**: Remove obvious errors before analysis
2. **Document Context**: Keep metadata about data collection methods
3. **Multiple Visualizations**: Use different chart types to reveal patterns
4. **Statistical Significance**: Consider sample size for valid conclusions
5. **Save Results**: Export analysis reports and charts for reproducibility
