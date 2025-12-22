# Methods Section Writing Guide

A comprehensive guide to writing clear, reproducible Methods sections.

---

## Overview and Purpose

The Methods section is the technical heart of your paper. It must be detailed enough for reproduction while remaining clear and organized. A well-written Methods section answers: "Could someone replicate this work?"

**Key Functions**:
- Describe experimental design and procedures
- Define all algorithms, models, and techniques
- Specify datasets, metrics, and evaluation protocols
- Enable reproduction by other researchers
- Provide technical details promised in Introduction

**Guiding Principle**: **Reproducibility** - Every decision should be documented or cited.

---

## Standard Structure

```text
3. Method / Methodology
   3.1 Problem Formulation
   3.2 Overview / Framework
   3.3 Component Details
       3.3.1 First component
       3.3.2 Second component
   3.4 Training / Optimization
   3.5 Implementation Details (optional)
```

---

## Section Components

### 1. Problem Formulation

**Purpose**: Formally define the problem, notation, and mathematical setup.

**Key Considerations**:
- Define all symbols before first use
- Use standard notation from your field when possible
- Be mathematically precise
- Keep it concise (typically ½ to 1 page)

**Common Phrases** (10 expressions):

1. "Let X = {x₁, ..., xₙ} denote..."
2. "We formulate the problem as follows..."
3. "Given [input], our goal is to [output]..."
4. "Formally, we define..."
5. "The task can be formulated as..."
6. "We model [phenomenon] as..."
7. "Let D = {(xᵢ, yᵢ)}ᵢ₌₁ⁿ represent..."
8. "We aim to learn a function f: X → Y that..."
9. "The objective is to find..."
10. "Under this formulation..."

**Example**:

> **Problem Formulation:** Let D = {(xᵢ, yᵢ)}ᵢ₌₁ⁿ denote our training dataset, where xᵢ ∈ ℝᵈ represents input features and yᵢ ∈ {1, ..., K} represents the class label. Given a new input x, our goal is to predict its label ŷ by learning a classifier f: ℝᵈ → {1, ..., K} that minimizes the expected classification error.

---

### 2. Overview / Framework

**Purpose**: Provide high-level architecture before diving into details. Usually accompanied by a figure.

**Key Considerations**:
- Start with bird's-eye view
- Reference a system diagram/figure
- Describe information flow
- Explain how components connect

**Common Phrases** (12 expressions):

1. "Figure X illustrates the overall architecture of our approach..."
2. "Our method consists of three main components:..."
3. "The framework operates in [number] stages:..."
4. "At a high level, the system..."
5. "The overall pipeline proceeds as follows:..."
6. "Our approach can be decomposed into..."
7. "The model architecture comprises..."
8. "As shown in Figure X, the framework..."
9. "The key components of our system are..."
10. "We adopt a [architecture type] architecture consisting of..."
11. "The method follows a [pattern] design, where..."
12. "The complete workflow is depicted in Figure X..."

**Before/After Example**:

*BEFORE (Too detailed upfront):*
> Our model uses 12 transformer layers with 768 hidden units each, dropout rate 0.1, and 12 attention heads per layer.

*AFTER (High-level first):*
> Figure 2 illustrates our framework, which consists of three main stages: (1) encoding input text using a transformer-based encoder, (2) fusing multi-modal features through cross-attention, and (3) generating predictions via a classification head. We now describe each component in detail.

---

### 3. Component Details

**Purpose**: Provide technical specifications for each component.

**Key Considerations**:
- One subsection per major component
- Include mathematical formulations
- Cite established techniques
- Describe novel components in detail
- Use algorithm pseudocode for complex procedures

**Common Phrases** (12 expressions):

1. "Specifically, we compute..."
2. "The [component] is defined as..."
3. "We adopt [technique] following [Citation]..."
4. "Formally, this operation can be expressed as..."
5. "We implement [component] as follows:..."
6. "Building on [prior work], we modify..."
7. "Unlike [baseline], our approach..."
8. "The computation proceeds in three steps:..."
9. "For each [element], we apply..."
10. "We parameterize [component] using..."
11. "This module takes as input... and produces..."
12. "The [component] consists of..."

**Example**:

> **3.3.1 Attention Mechanism**
> We adopt multi-head self-attention (Vaswani et al., 2017), which enables the model to attend to different representation subspaces. Specifically, given input embeddings H ∈ ℝⁿˣᵈ, we compute attention as:
>
> Attention(Q, K, V) = softmax(QKᵀ / √dₖ)V
>
> where Q, K, V are linear projections of H. We use 8 attention heads with dimension dₖ = 64.

---

### 4. Training / Optimization

**Purpose**: Describe how the model is trained.

**Key Considerations**:
- Specify loss function(s)
- Detail optimization algorithm
- List key hyperparameters
- Describe training procedure
- Mention regularization techniques

**Common Phrases** (12 expressions):

1. "We train the model by minimizing..."
2. "The loss function is defined as..."
3. "We optimize using [optimizer] with..."
4. "Training proceeds for [epochs/steps] until..."
5. "We employ [regularization] to prevent overfitting..."
6. "The model is trained end-to-end using..."
7. "We use a batch size of..."
8. "The learning rate is set to..."
9. "We apply [technique] during training..."
10. "Parameters are initialized using..."
11. "We use [schedule] learning rate decay..."
12. "Training converges after approximately..."

**Example**:

> **Training:** We train our model by minimizing the cross-entropy loss using the Adam optimizer (Kingma & Ba, 2015) with β₁ = 0.9, β₂ = 0.999. We use a learning rate of 5e-5 with linear warmup over the first 10% of training steps. Training proceeds for 10 epochs with batch size 32. We apply dropout (p = 0.1) to all layers and employ gradient clipping (max norm = 1.0) for stability.

---

## Writing Tips

### What Belongs in Methods vs. Results

| Methods | Results |
|---------|---------|
| Model architecture | Model performance |
| Loss function | Accuracy/F1 scores |
| Training procedure | Ablation outcomes |
| Dataset description | Statistical analysis |
| Evaluation metrics | Comparative results |

### Reproducibility Checklist

Essential details to include:
- [ ] Model architecture (layers, dimensions)
- [ ] Loss function(s) with equations
- [ ] Optimizer and hyperparameters
- [ ] Learning rate and schedule
- [ ] Batch size and training epochs
- [ ] Regularization techniques
- [ ] Random seeds (if applicable)
- [ ] Hardware used (if relevant)
- [ ] Dataset splits (train/dev/test)
- [ ] Evaluation metrics and protocols

### When to Use Algorithm Pseudocode

Use pseudocode when:
- Procedure involves multiple sequential steps
- Logic is complex or non-obvious
- Standard description would be verbose or unclear

Don't use pseudocode for:
- Standard operations (backpropagation, SGD)
- Simple 1-2 line computations
- Well-established algorithms with citations

**Example Algorithm**:

```
Algorithm 1: Meta-Learning Training Loop

Input: Support sets Dₛ, query sets Dᵧ, learning rates α, β
Output: Trained model parameters θ

1: Initialize θ randomly
2: for each episode do
3:    Sample task Tᵢ with support set Dₛⁱ and query set Dᵧⁱ
4:    Copy θ to θ'
5:    # Inner loop: adapt to support set
6:    for k steps do
7:       Compute loss ℒₛ on Dₛⁱ
8:       θ' ← θ' - α∇ℒₛ(θ')
9:    end for
10:   # Outer loop: update on query set
11:   Compute loss ℒᵧ on Dᵧⁱ using θ'
12:   θ ← θ - β∇ℒᵧ(θ')
13: end for
14: return θ
```

---

## Mathematical Notation Best Practices

| Element | Convention | Example |
|---------|------------|---------|
| Scalars | Lowercase italic | x, y, α, β |
| Vectors | Lowercase bold | **h**, **x** |
| Matrices | Uppercase bold | **W**, **H** |
| Sets | Calligraphic | 𝒟, 𝒳, 𝒮 |
| Functions | Roman | softmax, ReLU, sigmoid |

**Key Rules**:
- Define symbols before first use
- Use consistent notation throughout
- Follow field conventions when possible
- Use `\mathbf{}` for vectors/matrices in LaTeX
- Use `\mathcal{}` for sets
- Use `\text{}` or `\mathrm{}` for multi-letter function names

---

## Implementation Details

**What to include**:
- Programming language and framework
- Key library versions (if critical)
- Hardware specifications (if relevant for runtime)
- Code availability statement

**What to omit** (put in appendix):
- Full hyperparameter grids searched
- Minor implementation tricks
- Debugging procedures
- Development environment details

**Example**:

> **Implementation Details:** We implement our approach in PyTorch 1.12 (Paszke et al., 2019). Experiments are conducted on a server with 4× NVIDIA A100 GPUs. Training takes approximately 8 hours per model. Code and trained models are available at [URL].

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| **Undefined symbols** | Confuses readers | Define all notation before first use |
| **Insufficient detail** | Can't reproduce | Include all hyperparameters and design choices |
| **Excessive detail** | Obscures key ideas | Move minor details to appendix |
| **Missing citations** | Appears to claim others' work | Cite established techniques |
| **Results in Methods** | Wrong section | Save performance numbers for Results |
| **No figure** | Hard to grasp architecture | Include system diagram |

---

## Integration with Other Sections

**From Introduction**: Methods provides technical details for high-level approach described in Introduction

**To Results**: Methods defines what will be evaluated; Results reports outcomes

**From Related Work**: Methods can compare design choices to prior work

---

## Checklist

For a detailed, actionable checklist, see [methods-checklist.md](../assets/methods-checklist.md).

---

## Additional Resources

- See [writing-guidelines.md](./writing-guidelines.md) for general guidance
- See [academic-style.md](./academic-style.md) for notation conventions
- See [paper-examples.md](../assets/paper-examples.md) for more examples

---

**Remember**: The Methods section is where technical rigor matters most. Be precise, complete, and organized. When in doubt, include the detail—reviewers can always skip, but they can't reproduce what isn't there.
