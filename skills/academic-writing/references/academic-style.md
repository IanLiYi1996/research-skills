# Academic Style Guide

A comprehensive guide to academic writing style for research papers.

## Formal Language

### Avoid Contractions

| Avoid | Use |
|-------|-----|
| don't | do not |
| it's | it is |
| can't | cannot |
| won't | will not |
| we've | we have |
| they're | they are |
| isn't | is not |
| aren't | are not |

### Avoid Possessive Forms

Convert possessives to "of" phrases:

| Avoid | Use |
|-------|-----|
| the model's performance | the performance of the model |
| the method's accuracy | the accuracy of the method |
| the paper's contribution | the contribution of this paper |
| the dataset's size | the size of the dataset |

### Avoid Colloquialisms

| Avoid | Use |
|-------|-----|
| a lot of | numerous, many, substantial |
| get | obtain, acquire, achieve |
| kind of | somewhat, rather |
| things | factors, aspects, elements |
| stuff | materials, components |
| pretty good | reasonably effective |
| figure out | determine, identify |

---

## Hedging and Certainty

### Hedging Expressions

Use hedging to avoid over-claiming:

**Verbs:**
- suggest, indicate, imply
- appear to, seem to, tend to
- may, might, could

**Adverbs:**
- possibly, probably, likely
- generally, typically, often
- somewhat, relatively, partially

**Phrases:**
- It is possible that...
- This suggests that...
- The results indicate that...
- Evidence suggests...

### Certainty Expressions

Use for well-established facts:

**Strong:**
- clearly, obviously, certainly
- demonstrate, establish, prove
- always, never (use sparingly)

**Moderate:**
- show, reveal, confirm
- generally, typically, usually
- most, many, several

### Examples

```
# Too strong
This proves that our method is the best.

# Appropriately hedged
The results suggest that our method may offer improvements
in certain scenarios.

# Well-established fact (can be direct)
Neural networks consist of interconnected layers.
```

---

## Avoiding Absolute Statements

### Word Substitutions

| Absolute | Hedged Alternative |
|----------|-------------------|
| obvious | straightforward, clear |
| always | generally, typically, often |
| never | rarely, seldom |
| prove | demonstrate, show, indicate |
| best | effective, promising, competitive |
| perfect | highly accurate, near-optimal |
| unique | distinctive, novel |
| impossible | challenging, difficult |
| avoid | alleviate, mitigate |
| eliminate | reduce, minimize |
| solve | address, tackle |

### Phrase Substitutions

| Absolute | Hedged |
|----------|--------|
| This is the first... | To the best of our knowledge, this is the first... |
| Our method outperforms all... | Our method shows competitive/superior performance... |
| This problem is solved | This problem is addressed/mitigated |
| We achieve state-of-the-art | We achieve competitive/strong results |

---

## Transition Phrases

### Adding Information
- Furthermore, Moreover, Additionally
- In addition, Besides, Also
- What is more, Not only...but also

### Contrasting
- However, Nevertheless, Nonetheless
- In contrast, On the other hand
- Although, While, Whereas
- Despite, In spite of

### Cause and Effect
- Therefore, Thus, Hence, Consequently
- As a result, For this reason
- Due to, Because of, Owing to

### Exemplifying
- For example, For instance
- Specifically, In particular
- Such as, Including

### Summarizing
- In summary, To summarize
- In conclusion, Overall
- To conclude, In brief

### Sequencing
- First, Second, Third
- Initially, Subsequently, Finally
- First of all, Next, Lastly

---

## Sentence Structure

### One Idea Per Sentence

**Poor:**
```
The model achieves high accuracy on the benchmark dataset,
which was collected from multiple sources, and we also compare
it with several baselines, finding that it outperforms them
in most cases.
```

**Better:**
```
The model achieves high accuracy on the benchmark dataset.
This dataset was collected from multiple sources. We compare
our model with several baselines. The results show that our
model outperforms them in most cases.
```

### Minimize Pronouns

**Ambiguous:**
```
We compare our model with BERT. It achieves better results.
```

**Clear:**
```
We compare our model with BERT. Our model achieves better results.
```

### Separate Concerns

Don't mix observations, hypotheses, methods, and results:

**Mixed:**
```
We hypothesize that attention helps because we observe improvements
when we add it to our model which uses a transformer architecture.
```

**Separated:**
```
We hypothesize that attention mechanisms improve performance.
Our model uses a transformer architecture with attention layers.
Experimental results confirm our hypothesis, showing a 5% improvement.
```

---

## Active vs Passive Voice

### When to Use Active
- Describing your contributions
- Explaining methodology steps
- Making clear attributions

```
We propose a novel framework...
We conduct experiments on three datasets...
Our method achieves state-of-the-art results...
```

### When to Use Passive
- Describing general processes
- When the actor is unknown or unimportant
- Following field conventions

```
The data was collected from online sources...
Experiments were conducted using standard protocols...
The model was trained for 100 epochs...
```

### Consistency
Choose one style and maintain it within paragraphs. Many CS papers prefer active voice for methodology descriptions.

---

## Article Usage (a/an/the)

### A vs An
Based on **sound**, not spelling:

| Sound | Article | Examples |
|-------|---------|----------|
| Consonant | a | a model, a URL (/juː/), a unified |
| Vowel | an | an LSTM (/ɛl/), an F1 (/ɛf/), an hour |

### The (Specific)
Use for specific, identifiable items:

```
The proposed method...
The experimental results in Table 1...
The model described in Section 3...
```

### No Article (General)
Use for general concepts:

```
Neural networks are powerful... (general)
Machine learning has advanced... (general)
Pre-training improves performance... (general)
```

### Common Mistakes

```
# Wrong
The neural networks are powerful. (too specific for general statement)
A proposed method achieves... (should be specific)

# Correct
Neural networks are powerful.
The proposed method achieves...
```

---

## Numbers and Units

### Spelling Out Numbers
- Spell out numbers at sentence start: "Twenty participants..."
- Spell out small numbers (one through nine): "three experiments"
- Use numerals for 10 and above: "15 datasets"
- Use numerals with units: "5 GB", "100 epochs"

### Consistency
Pick a style and be consistent throughout the paper.

### SI Units
- Use standard abbreviations: Hz, GB, ms
- Space between number and unit: "100 ms" not "100ms"
- Use `siunitx` package in LaTeX: `\SI{100}{\milli\second}`

---

## Common Academic Phrases

### Introduction
- This paper addresses...
- We present a novel approach to...
- The main contributions of this paper are...
- To the best of our knowledge...

### Related Work
- Previous work has focused on...
- Several approaches have been proposed...
- Our work differs from prior work in that...
- Building on the work of...

### Methods
- We propose/introduce/present...
- The architecture consists of...
- Following [citation], we...
- Formally, we define...

### Results
- The results demonstrate that...
- As shown in Table X...
- We observe that...
- Compared to the baseline...

### Discussion
- These results suggest that...
- One possible explanation is...
- A limitation of our approach is...
- Future work could explore...

### Conclusion
- In this paper, we have presented...
- The experimental results demonstrate...
- We plan to extend this work by...
- Our findings have implications for...
