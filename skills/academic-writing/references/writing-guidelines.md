# Academic Writing Guidelines

Comprehensive guidelines for writing research papers, based on best practices from top conferences.

## Paper Structure (IMRAD)

### Abstract (150-250 words)

Structure:
1. **Background** (1-2 sentences): Context and importance
2. **Problem/Gap** (1 sentence): What's missing
3. **Objective** (1 sentence): What you do
4. **Methods** (2-3 sentences): How you do it
5. **Results** (2-3 sentences): Key findings with numbers
6. **Conclusion** (1-2 sentences): Significance and implications

Tips:
- Write last, after completing the paper
- Include specific numbers for key results
- Avoid undefined acronyms
- Make it self-contained

### Introduction

Structure (Funnel approach):
1. **Broad context**: Why this area matters
2. **Current state**: What's been done
3. **Gap/Problem**: What's missing or wrong
4. **This paper**: What you contribute
5. **Contributions list**: 3-5 bullet points
6. **Paper organization** (optional): Brief roadmap

Tips:
- Start broad, narrow to specific
- End with clear contributions
- Don't oversell or undersell
- Keep it concise (1-2 pages typically)

### Related Work

Organization options:
- **Chronological**: Evolution of the field
- **Thematic**: By topic/approach
- **Problem-based**: By challenge addressed

Tips:
- Show you know the field
- Position your work relative to others
- Be fair to prior work
- Highlight what's different about your approach
- Avoid extensive summaries; focus on relevance

### Methods

Structure:
1. **Overview**: High-level description
2. **Problem formulation**: Formal definitions
3. **Approach details**: Step-by-step methodology
4. **Implementation**: Technical details

Tips:
- Use notation consistently
- Define terms before using them
- Include enough detail for reproducibility
- Use figures to illustrate architecture
- Separate core method from implementation details

### Experiments

Structure:
1. **Setup**: Datasets, baselines, metrics, implementation
2. **Main results**: Primary comparison tables
3. **Analysis**: Ablations, case studies, visualizations
4. **Discussion**: Interpretation of results

Tips:
- Clearly state experimental setup
- Use consistent formatting for tables
- Include error bars/significance tests where applicable
- Explain surprising results
- Be honest about limitations

### Conclusion

Structure:
1. **Summary**: What you did and found
2. **Significance**: Why it matters
3. **Limitations**: Honest assessment
4. **Future work**: What comes next

Tips:
- Don't introduce new information
- Don't repeat the abstract verbatim
- Be concise (half to one page)
- End on a forward-looking note

---

## Section-Specific Tips

### Writing the Introduction

**Opening Hook:**
```
# Weak
Machine learning is important.

# Strong
Every day, millions of users interact with recommendation systems
that determine what content they see online.
```

**Stating the Problem:**
```
# Vague
Previous methods have limitations.

# Specific
Previous methods require O(n^2) memory, making them impractical
for sequences longer than 512 tokens.
```

**Listing Contributions:**
```
Our main contributions are:
- We propose X, a novel framework for...
- We introduce Y, a new technique that...
- We conduct extensive experiments showing...
- We release our code and data at [URL].
```

### Writing Methods

**Notation Introduction:**
```
Let X = {x_1, ..., x_n} denote the input sequence, where x_i ∈ R^d.
We define the attention mechanism as follows:
```

**Algorithm Description:**
```
Our method consists of three stages:
1. Encoding: We first encode the input using...
2. Processing: The encoded representation is then...
3. Decoding: Finally, we decode the output by...
```

### Writing Results

**Introducing Tables:**
```
# Don't repeat the caption
Wrong: Table 1 shows the accuracy of different methods.
       As shown, our method achieves 85.3% accuracy.

# Interpret and explain
Right: Table 1 compares our method against baselines.
       Our method outperforms the strongest baseline by 3.2%,
       demonstrating the effectiveness of the proposed attention mechanism.
```

**Describing Trends:**
```
# Vague
Our method is better.

# Specific
Our method consistently outperforms baselines across all datasets,
with improvements ranging from 2.1% to 5.4% in F1 score.
```

---

## Figure and Table Guidelines

### Figures

**Placement:**
- Top of page preferred, then middle
- Avoid bottom of page
- Place near first reference

**Quality:**
- Vector graphics (PDF) for diagrams
- High resolution for photos/screenshots
- Consistent font sizes across figures
- Readable when printed in black and white

**Captions:**
- Self-contained: Explain without reading text
- Format: "Figure X: [What it shows]. [Key observation/interpretation]."

### Tables

**Format:**
- Use booktabs (three-line tables)
- No vertical lines
- Align numbers by decimal point
- Bold best results
- Include uncertainty (std dev) if available

**Captions:**
- Place above the table
- Explain column meanings if not obvious
- Note any special formatting (bold = best, etc.)

**Example:**
```latex
\begin{table}[t]
\centering
\caption{Performance comparison on benchmark datasets.
         Bold indicates best results.}
\begin{tabular}{lcc}
\toprule
Method & Accuracy & F1 \\
\midrule
Baseline & 82.1 ± 0.3 & 81.5 ± 0.4 \\
Previous SOTA & 84.5 ± 0.2 & 83.9 ± 0.3 \\
Ours & \textbf{87.2 ± 0.2} & \textbf{86.8 ± 0.3} \\
\bottomrule
\end{tabular}
\end{table}
```

---

## Common Writing Mistakes

### 1. Vague Claims

```
# Bad
Our method is better.
The results are good.
This approach works well.

# Good
Our method improves accuracy by 5.2%.
The F1 score reaches 89.3%, surpassing all baselines.
This approach reduces inference time by 40%.
```

### 2. Missing Context

```
# Bad
We use BERT for encoding.

# Good
We use BERT-base (Devlin et al., 2019) for encoding,
which provides contextualized word representations.
```

### 3. Overclaiming

```
# Bad
We solve the problem of machine translation.
Our method is optimal.

# Good
We address challenges in low-resource machine translation.
Our method achieves competitive results.
```

### 4. Inconsistent Terminology

```
# Bad
We use a neural network... The model... The architecture...
  The system... (all referring to the same thing)

# Good
We propose TransModel. TransModel consists of...
TransModel achieves... (consistently use one name)
```

### 5. Dense Writing

```
# Bad (too dense)
Our transformer-based multi-task learning framework
with hierarchical attention achieves SOTA on five
benchmark datasets.

# Good (unpacked)
We propose a transformer-based framework for multi-task
learning. The framework uses hierarchical attention to
capture both local and global dependencies. Experiments
on five benchmark datasets show state-of-the-art results.
```

---

## Review Response Tips

### Addressing Reviewer Comments

1. **Thank the reviewer**: Be polite and professional
2. **Quote the concern**: Show you understand the issue
3. **Provide response**: Address directly and specifically
4. **Show evidence**: Point to experiments, analysis, or revisions
5. **Indicate changes**: Note where in the paper changes were made

**Example:**
```
> R1: The comparison with baseline X is missing.

Thank you for this suggestion. We have added comparisons
with baseline X in Table 2 (Section 4.2). Our method
outperforms X by 3.5% on Dataset A and 2.1% on Dataset B.
```

### Common Reviewer Concerns

| Concern | Response Strategy |
|---------|-------------------|
| Missing baselines | Add experiments, explain if infeasible |
| Limited datasets | Add more, or justify selection |
| No significance tests | Add error bars, p-values |
| Unclear writing | Revise specific sections |
| Missing details | Add to paper or appendix |
| Overclaiming | Tone down language, add caveats |

---

## Pre-submission Checklist

### Content
- [ ] Abstract is self-contained and concise
- [ ] Introduction clearly states contributions
- [ ] Related work is comprehensive and fair
- [ ] Methods are reproducible
- [ ] All claims are supported by evidence
- [ ] Limitations are acknowledged

### Format
- [ ] Within page limit
- [ ] Figures are high quality and readable
- [ ] Tables use consistent formatting
- [ ] References are complete and formatted correctly
- [ ] No orphaned sections or figures

### Language
- [ ] No contractions
- [ ] No colloquial language
- [ ] Consistent terminology throughout
- [ ] Clear, concise sentences
- [ ] Proper hedging for uncertain claims

### Technical
- [ ] All symbols defined before use
- [ ] Equations numbered only if referenced
- [ ] All figures/tables referenced in text
- [ ] Hyperlinks work (if applicable)

### Anonymity (for blind review)
- [ ] No author names in text or PDF metadata
- [ ] No institutional affiliations
- [ ] No identifying URLs or acknowledgments
- [ ] Self-citations appropriately anonymized

---

## Recommended Resources

### Style Guides
- Strunk & White, "The Elements of Style"
- Williams & Bizup, "Style: Lessons in Clarity and Grace"

### Academic Writing
- [How to Write a Great Research Paper (Simon Peyton Jones)](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/)
- [Writing Tips for PhD Students (Karl Whelan)](https://www.karlwhelan.com/Teaching/PhD/phd-writing-talk.pdf)

### Field-Specific
- [ACL Paper Writing Tips](http://www.phontron.com/paper-guide.php)
- [CVPR Author Guidelines](https://cvpr.thecvf.com/Conferences/2024/AuthorGuidelines)

### Tools
- [Grammarly](https://grammarly.com) - Grammar and style checking
- [Writefull](https://writefull.com) - Academic language checking
- [Hemingway Editor](https://hemingwayapp.com) - Readability checking
