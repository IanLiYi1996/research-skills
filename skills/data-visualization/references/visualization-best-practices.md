# Data Visualization Best Practices

## Chart Selection Guide

### By Data Type

| Data Type | Best Chart Types |
|-----------|-----------------|
| One continuous variable | Histogram, Density plot, Box plot |
| Two continuous variables | Scatter plot, Line chart, Hexbin plot |
| One categorical, one continuous | Bar chart, Box plot, Violin plot |
| Two categorical variables | Grouped bar, Heat map, Mosaic plot |
| Time series | Line chart, Area chart, Candlestick |
| Part-to-whole | Stacked bar, Tree map (avoid pie charts) |
| Distribution comparison | Box plot, Violin plot, Ridge plot |
| Correlation matrix | Heat map, Correlogram |

### Decision Tree

```
What do you want to show?
│
├─ Distribution of one variable?
│  ├─ Continuous → Histogram, Density plot
│  └─ Categorical → Bar chart
│
├─ Relationship between two variables?
│  ├─ Both continuous → Scatter plot, Line chart
│  ├─ One categorical, one continuous → Box plot, Violin plot
│  └─ Both categorical → Grouped bar, Heat map
│
├─ Comparison across groups?
│  └─ Box plot, Violin plot, Bar chart with error bars
│
├─ Change over time?
│  └─ Line chart, Area chart
│
└─ Part of a whole?
   └─ Stacked bar, Tree map
```

## Color Guidelines

### Color-Blind Safe Palettes

**Qualitative (categorical data)**:
- Okabe-Ito palette (8 colors, optimized for color blindness)
- ColorBrewer qualitative schemes
- Tableau 10 (modified for accessibility)

**Sequential (continuous low-to-high)**:
- Blues, Greens, Oranges (single hue)
- YlOrRd, YlGnBu (multi-hue)

**Diverging (data with meaningful midpoint)**:
- RdBu (red-blue)
- BrBG (brown-green)
- PiYG (pink-green)

### Color Usage Rules

1. **Limit colors**: 5-7 maximum per chart
2. **Meaningful use**: Color should encode information, not just decorate
3. **Sufficient contrast**: 4.5:1 ratio for text, 3:1 for graphical objects
4. **Consistent mapping**: Same color = same meaning across figures
5. **Test in grayscale**: Ensure information preserved without color

### Tools for Testing
- Color Oracle (free color blindness simulator)
- Coblis (Color Blindness Simulator)
- WebAIM Contrast Checker

## Typography and Labeling

### Font Sizes (for print at standard size)
- Title: 16-18 pt
- Axis labels: 12-14 pt
- Tick labels: 10-12 pt
- Legend: 10-12 pt
- Annotations: 10-12 pt

### Font Choices
- **Sans-serif**: Arial, Helvetica, Calibri (cleaner for screens)
- **Serif**: Times New Roman, Georgia (traditional for print)
- **Consistency**: Use same font family throughout

### Label Best Practices
- Clear, descriptive axis labels with units
- Concise but informative title
- Legend only when necessary (direct labels preferred)
- Horizontal text preferred over rotated

## Common Mistakes to Avoid

### 1. Misleading Scales
❌ **Bad**: Y-axis doesn't start at zero for bar charts
✓ **Good**: Start at zero for bar charts (not required for line charts)

### 2. Chart Junk
❌ **Bad**: 3D effects, excessive gridlines, decorative elements
✓ **Good**: Minimal, clean design focusing on data

### 3. Too Much Information
❌ **Bad**: Cramming multiple messages into one figure
✓ **Good**: One clear message per figure

### 4. Poor Color Choices
❌ **Bad**: Red/green combinations, rainbow scales, too many colors
✓ **Good**: Color-blind safe palettes, purposeful color use

### 5. Missing Context
❌ **Bad**: No error bars, no sample sizes, no units
✓ **Good**: Complete information for interpretation

## Publication-Specific Requirements

### General Scientific Journals
- Resolution: 300-600 DPI
- Format: TIFF, EPS, or PDF (vector preferred)
- Width: 3.5" (single column) or 7" (double column)
- Font: Embed all fonts
- Color: CMYK for print, RGB for online

### Nature Family
- Min resolution: 300 DPI (600 for line art)
- Max file size: 10 MB
- Format: PDF, EPS, TIFF
- Color: RGB

### Science
- Resolution: 300 DPI minimum
- Format: PDF, EPS, TIFF
- Dimensions: Fit within page width

### PLOS
- Resolution: 300-600 DPI
- Format: TIFF, EPS, PDF
- Max 10 MB per file

## Figure Composition

### Multi-Panel Figures

**Layout strategies**:
- **A, B, C panels**: Related but distinct analyses
- **Rows**: Different conditions or time points
- **Columns**: Different variables or measurements

**Best practices**:
- Consistent sizing across panels
- Clear panel labels (A, B, C, etc.)
- Aligned axes where possible
- Shared legends when applicable
- White space between panels

### Figure Legends

Include in legends:
- Brief title describing main finding
- Explanation of all symbols, colors, abbreviations
- Sample sizes (n = ...)
- Statistical test results (p-values, effect sizes)
- Error bar definition (SD, SEM, CI)

## Software-Specific Tips

### Matplotlib (Python)
```python
# Publication style
plt.style.use('seaborn-paper')
plt.rcParams['font.size'] = 12
plt.rcParams['figure.dpi'] = 300

# Color-blind safe
from seaborn import color_palette
colors = color_palette("colorblind")
```

### ggplot2 (R)
```r
# Publication theme
theme_set(theme_bw())
theme_update(text = element_text(size = 12))

# Color-blind safe
scale_color_viridis_d()  # discrete
scale_color_viridis_c()  # continuous
```

## Quick Checklist

Before finalizing any figure:

- [ ] Message is clear and unambiguous
- [ ] Appropriate chart type for data
- [ ] All axes labeled with units
- [ ] Legend present (if needed) and clear
- [ ] Color-blind safe palette
- [ ] Sufficient contrast for all elements
- [ ] Text readable at publication size
- [ ] High resolution (300+ DPI)
- [ ] Vector format for line art
- [ ] Error bars included where appropriate
- [ ] Sample sizes indicated
- [ ] Statistical significance marked clearly
- [ ] Consistent with other figures in manuscript
- [ ] Source data available
- [ ] Figure legend written

## Resources

- **Books**:
  - "The Visual Display of Quantitative Information" by Edward Tufte
  - "Fundamentals of Data Visualization" by Claus Wilke

- **Online**:
  - ColorBrewer: https://colorbrewer2.org/
  - Data-to-Viz: https://www.data-to-viz.com/

- **Tools**:
  - Matplotlib documentation
  - Seaborn gallery
  - ggplot2 examples
