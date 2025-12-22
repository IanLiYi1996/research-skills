# Methods Section Checklist

Use this checklist to ensure your Methods section is complete and reproducible. For detailed guidance, see [methods-guide.md](../references/methods-guide.md).

---

## Problem Formulation

- [ ] All mathematical notation defined before first use
- [ ] Problem formally stated (input, output, objective)
- [ ] Used standard notation from field when possible
- [ ] Notation is consistent throughout paper
- [ ] Formulation is mathematically precise

---

## Overview / Framework

- [ ] Provided high-level architecture description
- [ ] Included system diagram/figure showing overall structure
- [ ] Described information flow through system
- [ ] Explained how components connect
- [ ] Started with bird's-eye view before details

---

## Component Details

- [ ] Each major component has its own subsection
- [ ] Novel components described in sufficient detail for reproduction
- [ ] Established techniques cited appropriately
- [ ] Mathematical formulations provided where needed
- [ ] Used algorithm pseudocode for complex procedures
- [ ] Explained design choices and rationale
- [ ] Described how components interact

---

## Training / Optimization

- [ ] Loss function(s) specified with equations
- [ ] Optimizer identified (e.g., Adam, SGD)
- [ ] Learning rate specified
- [ ] Batch size stated
- [ ] Number of training epochs/steps indicated
- [ ] Regularization techniques described (dropout, weight decay, etc.)
- [ ] Learning rate schedule mentioned (if used)
- [ ] Parameter initialization described
- [ ] Convergence criteria specified
- [ ] Gradient clipping or other stabilization techniques noted (if used)

---

## Reproducibility Essentials

- [ ] Model architecture fully specified (layers, dimensions, activations)
- [ ] All hyperparameters listed or referenced in appendix
- [ ] Dataset splits clearly defined (train/val/test proportions)
- [ ] Evaluation metrics defined
- [ ] Random seeds mentioned (if results depend on initialization)
- [ ] Hardware specifications provided (if relevant for runtime)
- [ ] Software framework and versions specified
- [ ] Code availability statement included

---

## Mathematical Notation

- [ ] Scalars in lowercase italic (x, α)
- [ ] Vectors in lowercase bold (**h**, **x**)
- [ ] Matrices in uppercase bold (**W**, **H**)
- [ ] Sets in calligraphic (𝒟, 𝒳)
- [ ] Functions in roman (softmax, ReLU)
- [ ] Consistent notation throughout paper
- [ ] All symbols defined in order of appearance

---

## Figures and Algorithms

- [ ] Included system architecture figure
- [ ] Figure clearly shows component relationships
- [ ] Algorithm pseudocode for complex procedures (if applicable)
- [ ] Algorithm input/output specified
- [ ] Algorithm line numbers for reference in text (if applicable)
- [ ] All figures referenced in text

---

## Citations

- [ ] Cited established techniques and methods
- [ ] Cited datasets used
- [ ] Cited evaluation metrics (if non-standard)
- [ ] Cited baseline implementations (if using others' code)
- [ ] Acknowledged prior work your method builds on

---

## Clarity and Organization

- [ ] Logical flow from problem → framework → components → training
- [ ] Each subsection has clear purpose
- [ ] Transitions between subsections are smooth
- [ ] Technical terms defined or referenced
- [ ] Avoided excessive jargon
- [ ] Balance between clarity and precision

---

## What NOT to Include

- [ ] No performance numbers (those belong in Results)
- [ ] No interpretation of outcomes (that's for Discussion)
- [ ] No minor implementation tricks (those go in appendix)
- [ ] No subjective claims ("better," "efficient")—just describe objectively

---

## Common Pitfalls Avoided

- [ ] Not leaving symbols undefined
- [ ] Not providing insufficient detail for reproduction
- [ ] Not including results or analysis in Methods
- [ ] Not citing established techniques
- [ ] Not using consistent notation
- [ ] Not including a system diagram

---

## Final Checks

- [ ] Read through entire section for flow and clarity
- [ ] Verified all equations are correct and properly formatted
- [ ] Checked that all citations are accurate
- [ ] Ensured reproducibility: could someone implement this?
- [ ] Had colleague review for completeness
- [ ] Confirmed alignment with journal/conference requirements
- [ ] Verified consistency with Introduction (promises delivered)

---

## Quick Self-Assessment

1. **Reproducibility**: Could an expert in my field reproduce this work from my description?
2. **Clarity**: Is the architecture and methodology clear without unnecessary complexity?
3. **Completeness**: Have I specified all design choices and hyperparameters?
4. **Organization**: Does the structure flow logically from problem to solution?
5. **Precision**: Are mathematical formulations correct and unambiguous?

---

## Additional Resources

- **Detailed Guidance**: See [methods-guide.md](../references/methods-guide.md)
- **Examples**: See [paper-examples.md](./paper-examples.md) for Methods examples
- **General Guidelines**: See [writing-guidelines.md](../references/writing-guidelines.md)
- **Notation Conventions**: See [academic-style.md](../references/academic-style.md)
