# Results Section Writing Guide

A comprehensive guide to presenting experimental findings objectively and effectively.

---

## Overview and Purpose

The Results section objectively presents your experimental findings without interpretation (that's for Discussion). It answers: "What did you find?"

**Key Functions**:
- Present findings clearly and objectively
- Report all relevant results (not cherry-picked)
- Reference figures and tables
- Provide statistical evidence
- Organize results logically

**Guiding Principle**: **Objectivity** - Report what you found, not what it means.

---

## Standard Structure

```text
4. Results / Experiments
   4.1 Experimental Setup (datasets, baselines, metrics)
   4.2 Main Results (primary findings)
   4.3 Ablation Studies (component analysis)
   4.4 Additional Analysis (optional: sensitivity, case studies)
```

---

## Key Components

### 1. Experimental Setup

**Purpose**: Describe datasets, baselines, and evaluation metrics.

**Common Phrases** (12 expressions):

1. "We evaluate our approach on [X] datasets..."
2. "We compare against [N] baselines..."
3. "Performance is measured using..."
4. "We use standard train/dev/test splits of..."
5. "Following prior work (Citation), we adopt..."
6. "We report results averaged over [N] runs..."
7. "All experiments are conducted on..."
8. "We implement [baseline] following..."
9. "Evaluation metrics include..."
10. "We use the publicly available..."
11. "Hyperparameters are tuned on..."
12. "Statistical significance is assessed using..."

---

### 2. Main Results

**Purpose**: Present primary experimental findings clearly.

**Key Considerations**:
- Start with most important results
- Reference tables/figures explicitly
- Report statistical significance
- Use consistent formatting
- Be objective (no interpretation here)

**Common Phrases** (12 expressions):

1. "Table X shows the performance comparison..."
2. "As shown in Figure X, our method..."
3. "Our approach achieves X% accuracy, outperforming..."
4. "Results are presented in Table X..."
5. "We observe that..."
6. "The results demonstrate that..."
7. "Performance across all metrics is reported in..."
8. "Compared to the strongest baseline, we achieve..."
9. "Figure X illustrates the trend in..."
10. "Our method consistently outperforms..."
11. "The model achieves [metric] of [value] ± [std]..."
12. "Statistical significance testing reveals..."

**Before/After Example**:

*BEFORE (Interpretive, belongs in Discussion):*
> Table 1 shows that our method is much better than baselines because it uses better attention mechanisms.

*AFTER (Objective, pure results):*
> Table 1 compares our method against five baselines across three datasets. Our approach achieves the highest F1 score on all datasets, with improvements ranging from 3.2% to 5.7% over the strongest baseline (p < 0.01 for all comparisons).

---

### 3. Ablation Studies

**Purpose**: Demonstrate contribution of individual components.

**Common Phrases** (12 expressions):

1. "To assess the contribution of each component, we..."
2. "Table X shows ablation results..."
3. "Removing [component] results in a drop of..."
4. "We observe that [component] contributes..."
5. "The full model outperforms all ablated variants..."
6. "Performance degrades by [X]% without..."
7. "Each component provides complementary benefits..."
8. "The most critical component is..."
9. "We conduct ablation studies to isolate..."
10. "Comparing rows [X] and [Y] in Table [Z], we see..."
11. "The ablation results in Table X demonstrate..."
12. "Without [component], accuracy drops from [X] to [Y]..."

---

### 4. Statistical Reporting

**Key Principles**:
- Always include error bars (std dev, confidence intervals)
- Report statistical significance for close results
- Use consistent precision (e.g., 3 decimal places)
- State number of runs

**Example**:

> Our method achieves 89.3 ± 0.4% accuracy (mean ± std over 5 runs with different random seeds). This represents a statistically significant improvement over the strongest baseline (86.1 ± 0.5%), confirmed by paired t-test (p < 0.01).

---

## Table and Figure Guidelines

### Introducing Tables

**Common Patterns**:

```
# Pattern 1: Direct reference
Table X presents the main results on [dataset]. Our method achieves...

# Pattern 2: Comparative
As shown in Table X, our approach outperforms all baselines...

# Pattern 3: Highlighting
Table X summarizes performance across datasets. Notably, we observe...
```

### Describing Trends

**Common Phrases** (12 expressions):

1. "Figure X shows that performance increases with..."
2. "We observe a positive correlation between..."
3. "The trend indicates that..."
4. "As [parameter] increases, [metric] decreases..."
5. "Performance plateaus at..."
6. "The relationship between [X] and [Y] is..."
7. "Across all conditions, we consistently observe..."
8. "The pattern suggests that..."
9. "There is a clear trade-off between..."
10. "Results vary significantly across..."
11. "Performance is relatively stable when..."
12. "The largest gains occur when..."

---

## Writing Tips

### What Belongs in Results vs. Discussion

| Results | Discussion |
|---------|-----------|
| "We achieve 89% accuracy" | "This shows our method is effective" |
| "Method A outperforms Method B by 5%" | "This is because A handles X better" |
| "Figure 2 shows performance drops with noise" | "This limitation suggests future work on..." |
| "Ablating component X reduces F1 by 3%" | "This demonstrates X's importance for..." |

### Organizing Results

Choose one organizational strategy:

1. **By Research Question**: Answer RQ1, then RQ2, etc.
2. **By Dataset**: Results on Dataset A, then Dataset B, etc.
3. **By Metric**: Accuracy results, then speed, then memory
4. **By Importance**: Main results first, then secondary analysis

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| **No error bars** | Can't assess reliability | Report mean ± std over multiple runs |
| **Cherry-picking** | Biased presentation | Report all metrics, all datasets |
| **Interpretation** | Belongs in Discussion | State facts objectively |
| **Inconsistent reporting** | Confusing | Use same precision, format throughout |
| **Missing significance** | Can't assess if differences matter | Report p-values for close results |

---

## Checklist

For detailed checklist, see [results-checklist.md](../assets/results-checklist.md).

---

## Additional Resources

- See [writing-guidelines.md](./writing-guidelines.md)
- See [paper-examples.md](../assets/paper-examples.md)

---

**Remember**: Results = Facts. Discussion = Interpretation. Keep them separate!
