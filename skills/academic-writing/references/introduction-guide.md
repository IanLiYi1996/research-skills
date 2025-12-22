# Introduction Section Writing Guide

A comprehensive guide to writing compelling Introduction sections using the funnel approach and structured framework.

---

## Overview and Purpose

The Introduction is your paper's opening argument—it must hook readers, establish context, identify gaps, and clearly articulate your contribution. A well-crafted Introduction answers four key questions:

1. **Why should I care?** (Broad importance)
2. **What's been done?** (Existing work)
3. **What's missing?** (Research gap)
4. **What do you do?** (Your contribution)

**Key Functions**:
- Establish the research area's importance
- Review relevant prior work and identify limitations
- Define your research questions or objectives
- Clearly state your contributions
- Provide a roadmap for the paper (optional)

**Typical Length**: 1-2 pages for conference papers, 2-4 pages for journals.

---

## The Funnel Approach

The Introduction follows an "inverted funnel" structure—starting broad and narrowing to your specific contribution:

```
┌─────────────────────────────────────┐
│   BROAD CONTEXT (Why this matters)  │
├─────────────────────────────────────┤
│     PRIOR WORK (What's been done)   │
├─────────────────────────────────────┤
│  RESEARCH GAP (What's missing/wrong)│
├─────────────────────────────────────┤
│  YOUR APPROACH (What you propose)   │
├─────────────────────────────────────┤
│ CONTRIBUTIONS (Specific achievements)│
└─────────────────────────────────────┘
```

---

## Six-Stage Framework

### Stage 1: Opening Context (Broad Importance)

**Purpose**: Hook the reader by establishing why this research area matters. Start broad to engage diverse readers, then narrow toward your specific problem.

**Key Considerations**:
- Start with a compelling statement about the field's importance
- Use concrete examples or statistics when possible
- Connect to real-world problems or societal needs
- Avoid clichés ("In recent years...")
- Be specific enough to be interesting, general enough to be accessible

**Common Phrases** (12 expressions):

1. "[Research area] has become increasingly important due to..."
2. "Understanding [phenomenon] is critical for..."
3. "Recent advances in [field] have enabled..."
4. "[Application domain] relies heavily on..."
5. "The ability to [task] has far-reaching implications for..."
6. "One of the fundamental challenges in [field] is..."
7. "With the rapid growth of [technology/data], there is an urgent need for..."
8. "[Phenomenon] plays a crucial role in..."
9. "Effective [task] is essential for..."
10. "The proliferation of [X] has created both opportunities and challenges..."
11. "[Task] remains a central problem in..."
12. "As [field] continues to evolve, [challenge] becomes increasingly important..."

**Before/After Example**:

*BEFORE (Generic, weak hook):*
> In recent years, machine learning has become very popular. Many researchers are studying this area. It has many applications.

*AFTER (Specific, compelling):*
> Machine learning models now power systems that affect billions of users daily—from personalized recommendations to medical diagnosis. However, these models typically require massive labeled datasets, limiting their applicability in specialized domains where data is scarce or expensive to annotate.

*ANALYSIS*: The "after" version provides concrete scale, specific applications, and immediately introduces the key challenge, engaging readers and setting up the research gap.

---

### Stage 2: Prior Work and Current State

**Purpose**: Demonstrate your knowledge of the field by acknowledging existing approaches. Be fair and balanced—don't dismiss prior work, but identify its boundaries.

**Key Considerations**:
- Cite 5-10 key papers (not exhaustive—that's for Related Work)
- Group approaches thematically rather than chronologically
- Acknowledge the strengths of existing work first
- Identify patterns or commonalities across approaches
- Set up the transition to limitations naturally

**Common Phrases** (12 expressions):

1. "Several approaches have been proposed to address this challenge..."
2. "Prior work has primarily focused on..."
3. "Traditional methods rely on..."
4. "Recent advances leverage [technique] to improve..."
5. "A common approach is to..."
6. "Existing research has demonstrated that..."
7. "State-of-the-art methods typically employ..."
8. "One line of work explores..."
9. "Previous studies have shown that..."
10. "The dominant paradigm involves..."
11. "Researchers have proposed various techniques, including..."
12. "Building on classical [method], recent work has..."

**Before/After Example**:

*BEFORE (Dismissive, unclear):*
> Many people have worked on this problem before, but their methods don't work very well.

*AFTER (Fair, specific):*
> Several approaches have been proposed to address low-resource translation. Transfer learning from high-resource languages has shown promise (Smith et al., 2020; Johnson et al., 2021), while unsupervised methods exploit monolingual data (Brown et al., 2019). These approaches have significantly advanced the field, achieving competitive results on standard benchmarks.

*ANALYSIS*: The "after" version acknowledges specific approaches with citations, notes their contributions, and maintains a professional tone that respects prior work.

---

### Stage 3: Research Gap Identification

**Purpose**: Identify what's missing, limited, or problematic in existing work. This is the pivot from "what exists" to "what you do"—make the gap clear and compelling.

**Key Considerations**:
- Be specific about the limitation (not just "more work needed")
- Use hedging to remain diplomatic ("less attention," "remains challenging")
- Connect the gap to a real problem or need
- Avoid dismissive language ("fails to," "ignores")
- The gap should naturally motivate your approach

**Common Phrases** (12 expressions):

1. "However, these approaches face limitations when..."
2. "Despite this progress, a key challenge remains..."
3. "Existing methods typically require [constraint], which limits..."
4. "While effective in [context], these techniques struggle with..."
5. "A significant gap exists in understanding..."
6. "Less attention has been paid to..."
7. "Current approaches do not adequately address..."
8. "One limitation of existing work is that..."
9. "These methods, however, assume [assumption], which may not hold when..."
10. "An open question is whether..."
11. "Previous work has not explored..."
12. "It remains unclear how to..."

**Before/After Example**:

*BEFORE (Vague):*
> But existing methods have some problems.

*AFTER (Specific, motivated):*
> However, these approaches face a critical limitation: they require large amounts of parallel data for each language pair, which is prohibitively expensive for most of the world's 7,000+ languages. Furthermore, transfer learning assumes linguistic similarity between source and target languages, limiting effectiveness for typologically distant languages. This gap is particularly problematic for endangered languages where documentation efforts are time-sensitive.

*ANALYSIS*: The "after" version specifies multiple interconnected limitations, quantifies the scope of the problem, and explains why it matters, creating a compelling motivation.

---

### Stage 4: Proposed Approach Overview

**Purpose**: Provide a high-level description of your solution. Give readers the intuition before diving into technical details (which belong in Methods).

**Key Considerations**:
- Start with coarse-grained description, then add detail
- Explain the key insight or intuition behind your approach
- Highlight what makes it different from prior work
- Use 2-3 paragraphs typically
- Save technical details for the Methods section
- Explain "why this should work" not just "what you do"

**Common Phrases** (12 expressions):

1. "To address these limitations, we propose..."
2. "Our key insight is that..."
3. "In this work, we present..."
4. "We introduce [name], a novel approach that..."
5. "Our method builds on the observation that..."
6. "Motivated by [insight], we develop..."
7. "The central idea behind our approach is..."
8. "We tackle this challenge by..."
9. "Our work is based on the hypothesis that..."
10. "We leverage [technique] to overcome..."
11. "This paper presents a new framework for..."
12. "Our approach differs from prior work in that..."

**Before/After Example**:

*BEFORE (Too technical, no intuition):*
> We use a transformer architecture with 12 layers and 768 hidden dimensions, trained with cross-entropy loss and Adam optimizer with learning rate 0.001.

*AFTER (Intuitive, high-level):*
> To address these challenges, we propose a meta-learning framework that learns to adapt quickly from minimal parallel examples. Our key insight is that while languages differ in surface forms, many linguistic phenomena (such as subject-verb agreement or case marking) exhibit similar structural patterns. By explicitly modeling these shared structural regularities, our approach enables rapid adaptation to new languages with as few as 100 parallel sentences—orders of magnitude less than traditional methods require.

*ANALYSIS*: The "after" version explains the core idea and why it works, deferring technical architectural details to the Methods section.

---

### Stage 5: Contributions

**Purpose**: Clearly and concisely list your specific contributions. This is often the most-read part of the Introduction—make every contribution concrete and verifiable.

**Key Considerations**:
- Use bullet points (most common and clearest format)
- List 3-5 contributions (more suggests lack of focus)
- Order by importance or logical flow
- Be specific and concrete (avoid vague claims)
- Distinguish between different types of contributions (methods, findings, resources)
- Each contribution should be independently valuable

**Common Phrases** (12 expressions):

1. "Our main contributions are:"
2. "This paper makes the following contributions:"
3. "We make three key contributions:"
4. "The contributions of this work are:"
5. "Specifically, we contribute:"
6. "Our work makes the following advances:"
7. "The key contributions of this paper include:"
8. "We advance the state of the art through:"
9. "This research contributes:"
10. "In summary, our contributions are threefold:"
11. "The primary contributions of this work are:"
12. "We make both methodological and empirical contributions:"

**Common Contribution Formats**:

- **Methodological**: "We propose [X], a novel [type] that [key feature]..."
- **Theoretical**: "We provide [analysis/proof] showing that..."
- **Empirical**: "We conduct extensive experiments demonstrating that..."
- **Resource**: "We release [dataset/code], enabling..."
- **Analysis**: "We provide insights into [phenomenon] by analyzing..."

**Before/After Example**:

*BEFORE (Vague, unverifiable):*
> We propose a better method for translation. Our experiments show good results. We provide some analysis.

*AFTER (Concrete, specific):*
> Our main contributions are:
> - We propose **MetaTranslate**, a meta-learning framework that achieves competitive translation quality with 100× less parallel data than conventional neural methods.
> - We introduce a novel **structural transfer mechanism** that explicitly models cross-lingual syntactic patterns, improving adaptation to typologically diverse languages.
> - Through experiments on 25 low-resource languages spanning 8 language families, we demonstrate 15-30% BLEU improvements over strong transfer learning baselines.
> - We release our code, trained models, and a new benchmark dataset of 100-sentence parallel corpora for 50 endangered languages.

*ANALYSIS*: Each contribution is specific, introduces something concrete, and can be verified in the paper. Different contribution types are clearly distinguished.

---

### Stage 6: Paper Organization (Optional)

**Purpose**: Provide a roadmap of the paper's structure. This is increasingly less common in conference papers (due to page limits) but can be helpful in longer journal papers or complex multi-part works.

**Key Considerations**:
- Only include if the paper structure is non-standard or complex
- Keep it brief (2-4 sentences max)
- Can be combined with a transition sentence
- Often omitted in modern conference papers

**Common Phrases** (8 expressions):

1. "The rest of this paper is organized as follows:"
2. "The remainder of the paper is structured as follows:"
3. "This paper is organized as follows:"
4. "The paper proceeds as follows:"
5. "Section [X] describes..., Section [Y] presents..., and Section [Z] concludes."
6. "We first review related work (Section 2), then describe our method (Section 3)..."
7. "The paper is structured as follows: We begin with..."
8. "In the following sections, we..."

**Example**:

> The remainder of this paper is structured as follows: Section 2 reviews related work on low-resource NLP and meta-learning. Section 3 presents our MetaTranslate framework and structural transfer mechanism. Section 4 describes our experimental setup and evaluation methodology. Section 5 presents results and analysis. Section 6 discusses implications and limitations. Section 7 concludes and outlines future directions.

---

## Complete Introduction Template

```markdown
[STAGE 1: OPENING CONTEXT - 1 paragraph]
[Specific phenomenon or application] has become increasingly important due to [concrete reason].
[Real-world impact or examples]. However, [high-level challenge] remains a fundamental problem,
limiting [practical consequence].

[STAGE 2: PRIOR WORK - 1-2 paragraphs]
Several approaches have been proposed to address this challenge. [Approach type 1] leverages
[technique] to achieve [benefit] (Author1 et al., Year; Author2 et al., Year). Recent work has
explored [approach type 2], demonstrating [achievement] (Author3 et al., Year). State-of-the-art
methods typically employ [common paradigm], which has led to significant improvements in [metric/task].

[STAGE 3: RESEARCH GAP - 1 paragraph]
Despite this progress, existing approaches face key limitations. First, [limitation 1 with
explanation]. Second, [limitation 2 with impact]. These constraints are particularly problematic
for [important scenario], where [why it matters]. Addressing these limitations would enable
[valuable outcome].

[STAGE 4: PROPOSED APPROACH - 1-2 paragraphs]
To overcome these challenges, we propose [method name], a novel [type] that [key capability].
Our key insight is that [core intuition]. Unlike prior approaches that [limitation], our method
[distinguishing feature]. Specifically, we [high-level description of approach].

The central idea is to [explain mechanism in intuitive terms]. By [approach detail], we enable
[benefit] while [additional advantage]. This allows us to [key achievement] with [resource
requirement] compared to traditional approaches.

[STAGE 5: CONTRIBUTIONS - bullet points]
Our main contributions are:
- We propose [method name], which [novel aspect] and achieves [key result].
- We introduce [technique/component], enabling [capability] through [mechanism].
- We conduct experiments on [datasets/scenarios] demonstrating [findings with numbers].
- We provide analysis revealing [insights] about [phenomenon].
- We release [resource] to facilitate [future work benefit].

[STAGE 6: ORGANIZATION (optional) - 1 sentence]
The remainder of this paper describes related work (Section 2), presents our method (Section 3),
reports experimental results (Section 4), and concludes with discussion (Section 5).
```

---

## Common Mistakes and Solutions

| Mistake | Problem | Solution |
|---------|---------|----------|
| **Starting too narrow** | Readers outside subfield lose interest | Begin with broader context, then narrow |
| **Dismissing prior work** | Appears arrogant; offends reviewers | Acknowledge contributions; frame gaps diplomatically |
| **Vague contributions** | Can't verify claims; seems untrustworthy | Be specific: methods, numbers, resources |
| **Missing gap** | Unclear why your work is needed | Explicitly state what's missing or limited |
| **Too much detail** | Buries the lead; readers lose patience | Save technical details for Methods |
| **No hook** | Fails to engage readers | Start with compelling motivation |
| **Overclaiming** | Triggers skepticism | Be precise about scope and achievements |
| **Poor organization** | Hard to follow logic | Use clear funnel structure |

---

## Writing Tips

**Opening Hooks (Choose One Pattern)**:

Pattern 1 - Scale/Impact:
> "[System type] now serves over [X] users daily..."

Pattern 2 - Challenge:
> "One of the fundamental challenges in [field] is..."

Pattern 3 - Recent Development:
> "Recent advances in [technology] have enabled [capability], but..."

Pattern 4 - Concrete Example:
> "Consider the challenge of [specific scenario]..."

**Transitioning Between Stages**:

From Context → Prior Work:
- "Several approaches have been proposed to address this..."
- "Researchers have explored various techniques..."

From Prior Work → Gap:
- "However, these approaches face limitations when..."
- "Despite this progress, a key challenge remains..."

From Gap → Your Approach:
- "To address these limitations, we propose..."
- "Motivated by this gap, we develop..."

From Approach → Contributions:
- "Our main contributions are:"
- "Specifically, we contribute:"

**Balancing Confidence**:

- Too weak: "We try to somewhat improve..."
- Just right: "We propose [X], which achieves..."
- Too strong: "We completely solve...for the first time ever..."

---

## Contribution Statement Best Practices

### Types of Contributions

**1. Methodological Contributions** (most common):
```
We propose [name], a novel [architecture/algorithm/framework] that
[key capability] by [mechanism].
```

**2. Empirical Contributions**:
```
We conduct the first large-scale study of [phenomenon], revealing
that [finding] across [scope].
```

**3. Theoretical Contributions**:
```
We provide [proof/analysis] showing that [result], establishing
[theoretical insight].
```

**4. Resource Contributions**:
```
We release [dataset/benchmark/code], which includes [scale/features]
and enables [future work].
```

**5. Analysis/Insight Contributions**:
```
We demonstrate that [surprising finding], challenging the assumption
that [prior belief].
```

### Contribution Checklist

For each contribution, ask:
- [ ] Is it specific? (Not "We improve performance" but "We achieve 15% higher F1")
- [ ] Is it novel? (Can you point to what hasn't been done before?)
- [ ] Is it verifiable? (Will experiments/analysis confirm it?)
- [ ] Is it significant? (Does it matter to the community?)
- [ ] Is it independent? (Each contribution stands on its own)

---

## Integration with Other Sections

### Consistency with Abstract
- Abstract is a compressed version of Introduction
- Key contributions should match between both
- Motivation briefly restated in Abstract

### Leading to Related Work
- Introduction cites 5-10 key papers
- Related Work provides comprehensive coverage
- Gap identified in Introduction is explored in depth in Related Work

### Setting up Methods
- Introduction provides intuition and high-level approach
- Methods provides technical details and implementation
- Terminology introduced in Introduction is used consistently

### Connecting to Conclusion
- Contributions listed in Introduction should be validated in Conclusion
- Gap identified should be addressed by results
- "We propose [X]" in Introduction becomes "We presented [X]" in Conclusion

---

## Checklist

For a detailed, actionable checklist to use while drafting your Introduction, see [introduction-checklist.md](../assets/introduction-checklist.md).

---

## Additional Resources

- See [writing-guidelines.md](./writing-guidelines.md) for overall paper structure
- See [academic-style.md](./academic-style.md) for language conventions
- See [paper-examples.md](../assets/paper-examples.md) for more Introduction examples

---

**Remember**: The Introduction is your paper's "sales pitch." Make the problem compelling, show you understand the field, clearly identify what's missing, and confidently state what you contribute. Get this right, and readers will want to learn more.
