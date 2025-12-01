---
name: data-visualization
description: Data visualization and statistical analysis skill for creating publication-quality charts, graphs, and statistical reports. Use when creating visualizations, analyzing data distributions, performing statistical tests, generating charts for papers, or interpreting research data. Keywords include visualization, chart, graph, plot, statistical analysis, data exploration, matplotlib, seaborn, statistics.
---

# Data Visualization Skill

This skill provides comprehensive tools for creating publication-quality visualizations and performing statistical analysis on research data.

## Core Capabilities

### 1. Chart Creation
Generate various chart types for different data characteristics:
- **Distribution plots**: Histograms, density plots, box plots, violin plots
- **Relationship plots**: Scatter plots, line charts, heatmaps
- **Categorical plots**: Bar charts, grouped bar charts, stacked bars
- **Time series**: Line plots with trends, seasonal decomposition
- **Statistical plots**: QQ plots, residual plots, correlation matrices

### 2. Statistical Analysis
Perform comprehensive statistical analyses:
- **Descriptive statistics**: Mean, median, mode, standard deviation, quartiles
- **Hypothesis testing**: t-tests, ANOVA, chi-square, Mann-Whitney U
- **Correlation analysis**: Pearson, Spearman correlation coefficients
- **Regression modeling**: Linear, multiple, logistic regression
- **Distribution fitting**: Normal, exponential, power-law distributions

### 3. Data Exploration
Interactive exploratory data analysis:
- Identify patterns and trends
- Detect outliers and anomalies
- Assess data quality
- Compare groups
- Visualize missing data

### 4. Publication-Ready Output
Create charts suitable for academic publication:
- High-resolution output (300+ DPI)
- Vector formats (SVG, PDF)
- Customizable themes and styles
- Proper axis labels and titles
- Color-blind friendly palettes
- Consistent formatting

## Bundled Resources

### Scripts

Use `scripts/visualize_data.py` for automated chart generation:

```bash
python skills/data-visualization/scripts/visualize_data.py \
  --input data.csv \
  --type scatter \
  --x-column temperature \
  --y-column pressure \
  --output figure.png
```

Supported chart types:
- `scatter`: Scatter plot for two continuous variables
- `line`: Line chart for time series or ordered data
- `bar`: Bar chart for categorical data
- `histogram`: Distribution histogram
- `box`: Box plot for comparing distributions
- `heatmap`: Correlation or confusion matrix
- `violin`: Violin plot showing distribution shape

Use `scripts/statistical_analysis.py` for automated statistical tests:

```bash
python skills/data-visualization/scripts/statistical_analysis.py \
  --input data.csv \
  --test ttest \
  --group-column treatment \
  --value-column outcome \
  --output results.txt
```

### References

Consult `references/visualization-best-practices.md` for:
- Chart selection guidelines (which chart for which data type)
- Color palette recommendations (including color-blind safe options)
- Typography and labeling standards
- Common visualization mistakes to avoid
- Publication-specific requirements for major journals

Consult `references/statistical-tests.md` for:
- Decision tree for selecting appropriate statistical tests
- Assumptions for each test
- Interpretation guidelines for p-values and effect sizes
- Sample size calculations
- Multiple testing corrections

### Assets

Use `assets/chart-templates/` for consistent styling:
- `publication_style.mplstyle`: Matplotlib style for publication figures
- `presentation_style.mplstyle`: Style for presentations and posters
- `color_palettes.json`: Curated color schemes

## Workflow Patterns

### Exploratory Data Analysis Workflow

1. **Load and Inspect**:
   - Read data file
   - Check dimensions, data types
   - Identify missing values

2. **Summary Statistics**:
   - Calculate descriptive statistics
   - Generate summary tables
   - Identify outliers

3. **Distribution Analysis**:
   - Plot histograms for each variable
   - Create box plots
   - Check for normality

4. **Relationship Exploration**:
   - Scatter plots for continuous pairs
   - Correlation matrix and heatmap
   - Group comparisons

5. **Initial Insights**:
   - Document patterns observed
   - Note anomalies
   - Formulate hypotheses

### Statistical Testing Workflow

1. **Define Hypotheses**:
   - Null hypothesis (H₀)
   - Alternative hypothesis (H₁)
   - Significance level (α = 0.05)

2. **Check Assumptions**:
   - Normality (Shapiro-Wilk test, QQ plot)
   - Homogeneity of variance (Levene's test)
   - Independence of observations
   - Sample size adequacy

3. **Select Appropriate Test**:
   - Compare two groups → t-test or Mann-Whitney
   - Compare 3+ groups → ANOVA or Kruskal-Wallis
   - Categorical data → Chi-square or Fisher's exact
   - Relationship strength → Correlation or regression

4. **Perform Test**:
   - Calculate test statistic
   - Determine p-value
   - Calculate effect size (Cohen's d, r², etc.)
   - Compute confidence intervals

5. **Interpret Results**:
   - Statistical significance (p < α)
   - Practical significance (effect size)
   - Consider multiple testing corrections
   - State conclusions clearly

### Publication Figure Workflow

1. **Plan Figure**:
   - Identify message to communicate
   - Select appropriate chart type
   - Sketch layout

2. **Generate Draft**:
   - Create initial visualization
   - Apply basic styling
   - Check data accuracy

3. **Refine Design**:
   - Apply publication style template
   - Use color-blind safe palette
   - Add clear labels and titles
   - Adjust font sizes for readability
   - Remove chart junk

4. **Quality Check**:
   - Verify data representation accuracy
   - Test at print size
   - Check resolution (300 DPI minimum)
   - Review with co-authors

5. **Export**:
   - Save as vector format (PDF/SVG) for print
   - Save high-res raster (PNG) for web
   - Document figure in figure legends file

## Best Practices

### Chart Selection
- **Show distribution**: Histogram, density plot, box plot
- **Compare groups**: Bar chart, box plot, violin plot
- **Show relationship**: Scatter plot, line chart
- **Show composition**: Stacked bar, pie chart (use sparingly)
- **Show change over time**: Line chart, area chart

### Design Principles
1. **Simplicity**: Remove unnecessary elements
2. **Clarity**: Clear labels, legends, and titles
3. **Accuracy**: No misleading scales or distortions
4. **Accessibility**: Color-blind friendly, high contrast
5. **Consistency**: Uniform styling across figures

### Common Mistakes to Avoid
- Starting y-axis at non-zero to exaggerate differences
- Using 3D effects unnecessarily
- Too many colors or patterns
- Illegible text (too small or low contrast)
- Missing error bars or confidence intervals
- Misleading aspect ratios

### Color Guidelines
- Use color purposefully, not decoratively
- Maximum 5-7 distinct colors per chart
- Ensure sufficient contrast (check with simulator)
- Consider grayscale printing
- Use sequential palettes for continuous data
- Use diverging palettes for data with meaningful midpoint
- Use categorical palettes for discrete categories

## Integration with Other Tools

- **MCP Filesystem**: Load data from research directory
- **MCP Database**: Query experiment results for visualization
- **Data Analysis Tools**: Integrate with pandas, numpy, scipy
- **Export Formats**: Generate figures for papers, presentations, posters

## Example Usage

When user requests: "Visualize the relationship between temperature and reaction rate from my experiment data"

Process:
1. Load data using MCP filesystem
2. Inspect data structure and quality
3. Calculate descriptive statistics for both variables
4. Create scatter plot with temperature on x-axis, reaction rate on y-axis
5. Add regression line if relationship appears linear
6. Include correlation coefficient and p-value
7. Apply publication style template
8. Export as high-resolution PNG and vector PDF
9. Generate statistical summary report

When user requests: "Compare treatment groups and test for significance"

Process:
1. Load experiment data
2. Check group sizes and distributions
3. Test assumptions (normality, homogeneity of variance)
4. Select appropriate test (t-test if 2 groups, ANOVA if 3+)
5. Perform statistical test
6. Calculate effect size
7. Create visualization (box plot or violin plot) showing:
   - Individual data points
   - Group means/medians
   - Error bars or confidence intervals
   - Significance indicators (*, **, ***)
8. Generate results table with statistics
9. Provide interpretation in plain language

Always ensure statistical rigor and clear visual communication of findings.
