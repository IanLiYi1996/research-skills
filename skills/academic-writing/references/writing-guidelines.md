# Academic Writing Guidelines

Comprehensive guidelines for writing research papers, based on best practices from top conferences.

## Quick Navigation

**Detailed Section-Specific Guides:**
- [Introduction Guide](./introduction-guide.md) - Funnel approach with 60+ common phrases
- [Methods Guide](./methods-guide.md) - Reproducibility-focused technical writing
- [Results Guide](./results-guide.md) - Objective presentation techniques
- [Discussion Guide](./discussion-guide.md) - 5-step framework with 70+ common phrases

**Interactive Resources:**
- [Writing Checklists](../assets/) - Section-by-section checkpoints for drafting
- [Academic Style Guide](./academic-style.md) - Language conventions and formal style

---

## Reviewer's Perspective (Self-Check)

**Write papers from a reviewer's perspective.** Before submission, ask yourself:

### 5 Key Questions

1. **Can the key points be grasped in 10 minutes?**
   - Is the logic clear and easy to follow?
   - Can a busy reviewer quickly understand your contribution?

2. **Does the logic from motivation to contribution hold?**
   - Is there a clear causal chain?
   - Does the problem naturally lead to your solution?

3. **Can the main contribution be explained in 3 sentences?**
   - What is the core novelty?
   - Why does it matter?

4. **Do experiments validate the motivation?**
   - Does each experiment serve a purpose?
   - Are claims backed by evidence?

5. **Is Abstract → Introduction → Method → Experiments logically consistent?**
   - No contradictions between sections
   - Story flows naturally throughout

---

## Writing Principles

### Presentation Hierarchy

**图 > 表 > Algorithm > 公式 > 文字**

(Figure > Table > Algorithm > Equation > Text)

- A picture is worth a thousand words
- Use the most intuitive representation
- Figures communicate faster than text

### Key Techniques

1. **Experiments should be substantial** - Often ~50% of paper length
2. **Figures and captions should be self-contained** - Understandable without reading main text
3. **Language should be clear and simple** - Prioritize clarity over complexity
4. **Use concrete examples** - In introduction and case studies, examples are crucial
5. **Make the story compelling** - Logical flow from problem to solution

---

## Paper Structure (IMRAD)

### Abstract (150-250 words)

**Core Components:**

1. **Problem & Motivation** (1-2 sentences)
   - What problem exists in prior work?
   - Tell a compelling story

2. **Proposed Solution** (1-2 sentences)
   - What do you propose?
   - Why does it work? (brief intuition)

3. **Key Results** (1-2 sentences)
   - Specific numbers and improvements
   - Main experimental findings

**Alternative Structure:**

1. **Background** (1-2 sentences): Context and importance
2. **Problem/Gap** (1 sentence): What's missing
3. **Objective** (1 sentence): What you do
4. **Methods** (2-3 sentences): How you do it
5. **Results** (2-3 sentences): Key findings with numbers
6. **Conclusion** (1-2 sentences): Significance and implications

**Tips:**

- Write last, after completing the paper
- Include specific numbers for key results
- Avoid undefined acronyms
- Make it self-contained
- Should answer: What? Why? How? Results?

### Introduction

**Detailed Structure:**

1. **Research Value** (1 paragraph)
   - Why is this problem important?
   - What is the significance of this research area?

2. **Prior Work & Limitations** (1-2 paragraphs)
   - What are the mainstream approaches?
   - Acknowledge their contributions
   - Point out existing problems/limitations

3. **Motivation & Insight** (1 paragraph)
   - Where does your inspiration come from?
   - What key observation or insight drives your approach?
   - **Use concrete examples** - Illustrative examples are crucial here

4. **Proposed Method** (1-2 paragraphs)
   - Coarse-grained description first
   - Then fine-grained explanation
   - Why does your approach address the limitations?

5. **Contributions** (bullet points)
   - List 3-5 specific contributions
   - Be concrete and measurable
   - Most common format in top venues

**Alternative Funnel Structure:**

1. **Broad context**: Why this area matters
2. **Current state**: What's been done
3. **Gap/Problem**: What's missing or wrong
4. **This paper**: What you contribute
5. **Contributions list**: 3-5 bullet points
6. **Paper organization** (optional): Brief roadmap

**Tips:**

- Start broad, narrow to specific
- End with clear contributions
- Don't oversell or undersell
- Keep it concise (1-2 pages typically)
- **Concrete examples in introduction are very important**
- Ensure motivation → method → contribution logic is airtight

### Related Work

The Related Work section establishes your scholarly context and differentiates your contribution.

#### Purpose and Goals

1. **Demonstrate expertise**: Show you understand the field deeply
2. **Position your work**: Clarify how your approach differs
3. **Acknowledge foundations**: Credit work you build upon
4. **Identify gaps**: Highlight what existing work doesn't address

#### Organization Strategies

| Strategy | Best For | Structure |
|----------|----------|-----------|
| **Chronological** | Showing field evolution | Early work → Recent advances → Your work |
| **Thematic** | Multiple related topics | Group by theme, then compare |
| **Problem-based** | Technical papers | Group by challenge addressed |
| **Methodological** | ML/AI papers | Group by approach type |

#### Critical Analysis Framework

For each related work, consider:

1. **What they did**: Brief objective summary (1-2 sentences)
2. **How it relates**: Connection to your problem
3. **Limitation or gap**: What they don't address (that you do)

**Example:**

```text
# Weak (just summarizing)
Smith et al. (2022) propose a transformer model for text classification.

# Strong (critical positioning)
Smith et al. (2022) demonstrate transformers excel at text classification.
However, their approach requires large labeled data, limiting applicability
to low-resource settings. Our method addresses this through...
```

#### Positioning Phrases

- "In contrast to [X], our approach..."
- "While [X] focuses on..., we address..."
- "Building on [X], we extend this to..."
- "Unlike previous methods that..., we propose..."
- "Our work differs from [X] in three key aspects:..."

#### Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| **Laundry list** | Lists without connection | Group thematically, explain relationships |
| **Too brief** | Seems unknowledgeable | Add depth for key papers |
| **Too comprehensive** | Wastes space | Focus on 15-25 most relevant papers |
| **Missing recent work** | Appears outdated | Check last 6 months arXiv/venues |
| **Only praising** | Doesn't justify contribution | Add critical analysis |
| **Only criticizing** | Appears arrogant | Acknowledge contributions first |

#### Depth vs Breadth

| Paper Type | Recommended |
|------------|-------------|
| Conference paper | 15-25 papers, 3-5 in depth |
| Workshop paper | 8-12 key papers |
| Journal paper | 30-50+ papers |

---

### Methods

The Methods section is the technical heart of your paper. It must be clear enough for understanding and detailed enough for reproduction.

#### Standard Structure

```text
3. Method
   3.1 Problem Formulation
   3.2 Overview / Framework (with figure)
   3.3 Component Details
       3.3.1 First component
       3.3.2 Second component
   3.4 Training / Optimization
```

#### Problem Formulation

**Define before use:**

```text
# Good
Let X = {x_1, ..., x_n} denote the input sequence where x_i ∈ R^d.
Given X, our goal is to predict y ∈ {1, ..., K}.

# Bad - undefined symbols
We compute f(X) to get the output y using our model M.
```

#### When to Use Algorithm Pseudocode

| Use Pseudocode | Don't Use |
|----------------|-----------|
| Complex multi-step procedures | Standard operations (SGD) |
| Novel algorithms | Simple 2-3 sentence procedures |
| When math would be unclear | Duplicates text exactly |

**Pseudocode best practices:**
- Number lines if referenced in text
- Use meaningful variable names
- Include input/output specifications
- Keep appropriate abstraction level

#### Mathematical Notation

| Type | Convention | Example |
|------|------------|---------|
| Scalars | Lowercase italic | x, y, α |
| Vectors | Lowercase bold | **x**, **h** |
| Matrices | Uppercase bold | **W**, **A** |
| Sets | Calligraphic | 𝒟, 𝒳 |
| Functions | Roman | softmax, ReLU |

#### Core Method vs Implementation Details

| In Main Paper | In Appendix |
|---------------|-------------|
| Key algorithmic innovations | Hardware specifications |
| Novel architectural components | Random seeds |
| Loss functions and objectives | Full hyperparameter tables |
| Essential hyperparameters | Training curves |

**Rule:** If changing it wouldn't change your scientific contribution, it's an implementation detail.

#### Reproducibility Checklist

- [ ] Model architecture fully specified
- [ ] Hyperparameters listed (or in appendix)
- [ ] Training procedure described
- [ ] Data splits specified
- [ ] Evaluation metrics defined
- [ ] Baseline implementations explained
- [ ] Code availability mentioned

#### Method Figure Guidelines

- Show overall architecture/pipeline
- Use consistent visual language
- Include legend if needed
- Reference in text: "As shown in Figure 2..."

---

### Experiments

The Experiments section validates your claims with empirical evidence.

#### Standard Structure

```text
4. Experiments
   4.1 Experimental Setup (datasets, baselines, metrics)
   4.2 Main Results (primary comparison)
   4.3 Analysis (ablations, case studies)
   4.4 Discussion (optional)
```

#### Experiment Design Principles

**Every experiment should answer a question:**

| Question | Experiment Design |
|----------|-------------------|
| "Does it work?" | Main comparison vs baselines |
| "Why does it work?" | Ablation studies |
| "When does it work?" | Breakdown by category |
| "How robust is it?" | Sensitivity analysis |
| "What does it learn?" | Qualitative analysis |

#### Dataset Description Template

```text
[Dataset] (Citation): [Brief description]. Contains [size] examples
for [task]. We use the standard train/dev/test split of [X/Y/Z].
```

#### Baseline Selection

| Type | Purpose | Example |
|------|---------|---------|
| **Classic** | Historical context | SVM, Logistic Regression |
| **Strong recent** | Current SOTA | BERT, GPT |
| **Ablated versions** | Validate components | Your method - component X |
| **Upper bound** | Show ceiling | Human performance |

**Avoid:** Only weak baselines, unfair comparisons, missing obvious competitors

#### Ablation Study Design

- Remove ONE component at a time
- Include base model (all components removed)
- Order by impact (largest drop first)
- Discuss which components matter most

**Example table:**

| Model | Accuracy | F1 |
|-------|----------|-----|
| Full model | 89.3 | 88.1 |
| w/o attention | 86.1 | 84.9 |
| w/o pre-training | 84.5 | 83.2 |
| Base only | 82.3 | 81.0 |

#### Statistical Significance

**Always include uncertainty:**

```text
# Bad
Our method achieves 89.3% accuracy.

# Good
Our method achieves 89.3 ± 0.4% accuracy (mean ± std over 5 runs).
```

**When to report significance:**
- Small improvements (<2%): Required
- Close results: Report p-values
- "Significant improvement" claims: Must be validated

**Common approaches:**
- Standard deviation over 3-5 runs
- Bootstrap confidence intervals
- Paired t-test or Wilcoxon test
- McNemar's test for classification

#### Handling Negative Results

```text
# Good (constructive)
While our method shows lower accuracy on small datasets (<1K examples),
it provides substantial gains on larger datasets where its advantages
are realized.

# Bad (dismissive)
Our method doesn't work on Dataset-C.
```

**Remember:** Reviewers respect honesty more than cherry-picked results.

#### Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| **Weak baselines only** | Inflated improvements | Add current SOTA |
| **No error bars** | Results may be noise | Report std over multiple runs |
| **Unfair comparison** | Misleading claims | Same data, preprocessing, tuning |
| **Missing ablations** | Can't assess components | Ablate each novel component |
| **No analysis** | Just tables, no insight | Explain why results make sense |
| **Cherry-picked** | Reviewer distrust | Report all metrics |

---

### Discussion

The Discussion interprets your results, connects them to the literature, and addresses their implications. This is where you move from "what we found" (Results) to "what it means" and "why it matters."

**For comprehensive guidance on writing Discussion sections, see [discussion-guide.md](./discussion-guide.md).**

#### Quick 5-Step Framework

Use this proven structure to ensure comprehensive discussion coverage:

1. **Summarize Current Research** - Briefly restate key findings (2-4 sentences) without repeating Results verbatim
2. **Relate to Literature** - Position findings within existing research, noting agreements and divergences
3. **Address Unexpected Findings** - Explain surprising results constructively (if applicable)
4. **Connect to Broader Implications** - Elevate specific findings to theoretical principles and practical applications
5. **Acknowledge Limitations** - Frame methodological boundaries constructively, connecting to future work

#### Essential Components

**Interpretation in Context**:
- Explain what findings mean, not just restate them
- Connect each major result to research questions/hypotheses
- Use appropriate hedging (suggests, indicates) rather than absolute claims

**Literature Integration**:
- Compare with 3-5 highly relevant studies
- Acknowledge consistent findings and explain divergences
- Show how your work extends or complements prior research

**Implications**:
- Theoretical: How findings advance understanding of the phenomenon
- Practical: Real-world applications and impact
- Methodological: Insights about approaches or techniques (if applicable)

**Constructive Limitation Framing**:
- 3-5 genuine limitations (methodological boundaries, not minor flaws)
- Explain potential impact on interpretation
- Connect each to specific future research directions
- Maintain confidence in core contributions

#### Common Patterns and Examples

**Strong Opening**:
```
Our results demonstrate that [main finding], addressing [research gap].
This finding has important implications for [theoretical/practical domain].
```

**Literature Connection**:
```
These findings are consistent with [Study A], who reported [similar result].
However, unlike [Study B], we observe that [key difference], suggesting
that [theoretical insight].
```

**Unexpected Finding**:
```
Contrary to our hypothesis, we found that [unexpected result]. This
counter-intuitive pattern may be explained by [plausible mechanism],
indicating that [revised understanding].
```

**Limitation Framing**:
```
While our approach demonstrates [strength], it is subject to [limitation].
Future work could address this by [specific solution], which would
[benefit/extension].
```

#### Integration Checklist

- [ ] Addresses all research questions from Introduction
- [ ] Interprets all major Results (nothing left unaddressed)
- [ ] Integrates 3-5+ relevant citations throughout (not just at beginning)
- [ ] Balances confidence with appropriate hedging
- [ ] Discusses both theoretical and practical implications
- [ ] Frames 3-5 limitations constructively
- [ ] Suggests specific future directions
- [ ] Maintains logical flow from findings → context → implications → limits

#### What to Avoid

| Mistake | Why It's Problematic | Solution |
|---------|---------------------|----------|
| Repeating Results | Wastes space, adds no value | Synthesize and interpret instead |
| Ignoring contrary evidence | Appears unaware of field | Address explicitly with explanations |
| Overclaiming | Triggers reviewer skepticism | Use appropriate hedging language |
| Excessive self-criticism | Undermines contribution | Balance honesty with confidence |
| No future directions | Missed opportunity | Suggest 2-3 specific next steps |

#### Resources

**Detailed Guidance**: See [discussion-guide.md](./discussion-guide.md) for:
- Complete 5-step framework with 70+ common phrases
- 10+ before/after examples showing strong vs. weak discussion writing
- Detailed guidance on each step with key considerations
- Complete annotated template
- Common mistakes table with solutions

**Interactive Checklist**: Use [discussion-checklist.md](../assets/discussion-checklist.md) while drafting to ensure comprehensive coverage (49 specific checkpoints).

**Additional Examples**: See [paper-examples.md](../assets/paper-examples.md) for more Discussion examples across different scenarios.

---

### Conclusion

The Conclusion wraps up your paper and leaves a lasting impression.

#### Structure

```text
6. Conclusion
   [Summary - what you did] (2-3 sentences)
   [Key findings] (2-3 sentences)
   [Significance] (1-2 sentences)
   [Limitations] (1-2 sentences)
   [Future work] (2-3 sentences)
```

#### Connecting Back to Motivation

**Link results to opening claims:**

```text
# Introduction claimed:
"Current methods struggle with long sequences due to O(n²) complexity."

# Conclusion connects back:
"We have presented EfficientAttn, which reduces attention complexity
from O(n²) to O(n log n). Experiments confirm this enables processing
sequences 10x longer while maintaining competitive accuracy."
```

#### Framing Limitations Constructively

| Limitation | Constructive Frame |
|------------|-------------------|
| Computational cost | "Trade-off between accuracy and efficiency" |
| Limited datasets | "Validated on standard benchmarks; broader evaluation is future work" |
| Specific domain | "Focused on [domain]; generalization is promising direction" |
| Requires labeled data | "Semi-supervised extensions could reduce this requirement" |

**Example:**

```text
# Bad
Our method fails on small datasets and is computationally expensive.

# Good
While our method achieves strong results on large-scale datasets,
its performance on smaller datasets (<10K examples) suggests that
the approach benefits most from abundant training data. Future work
could explore few-shot adaptations to extend applicability.
```

#### Future Work Types

1. **Extensions**: Natural next steps
2. **Applications**: New domains
3. **Improvements**: Addressing limitations
4. **Open questions**: Research directions

**Tip:** Be specific but don't give away your next paper!

#### What NOT to Include

| Don't Include | Why | Where It Belongs |
|---------------|-----|------------------|
| New results | Unexpected | Results section |
| New methods | Confusing | Methods section |
| Excessive detail | Verbose | Main paper |
| Apologies | Undermines confidence | Frame as future work |
| Hype | Reviewer distrust | Be measured |

**Length:** Half to one column (conference), half to one page (journal)

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
