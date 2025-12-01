---
name: huggingface
description: HuggingFace Hub integration skill for accessing models, datasets, and Spaces. Use when searching for ML models, exploring datasets, reading model documentation, or interacting with HuggingFace ecosystem. Keywords include HuggingFace, transformers, diffusers, model hub, dataset, pretrained models, fine-tuning, machine learning models, NLP models, computer vision models.
---

# HuggingFace Skill

This skill provides direct access to HuggingFace Hub through the HuggingFace MCP server for searching models, datasets, and accessing documentation.

## Core Capabilities

### 1. Model Search

Search HuggingFace Hub for models:

- **Keyword Search**: Search by model name or description
- **Task Filter**: Filter by task (text-generation, image-classification, etc.)
- **Library Filter**: Filter by framework (transformers, diffusers, etc.)
- **Sorting**: Sort by downloads, likes, or trending

### 2. Dataset Search

Find datasets on HuggingFace:

- **Keyword Search**: Search by dataset name or description
- **Task Filter**: Filter by task type
- **Language Filter**: Filter by language
- **Size Information**: Get dataset size and statistics

### 3. Model Card Reading

Get detailed model information:

- Model description and intended use
- Training data and methodology
- Performance metrics and benchmarks
- Usage examples and code snippets
- License information
- Citation details

### 4. Dataset Card Reading

Access dataset documentation:

- Dataset description and features
- Data splits and sizes
- Collection methodology
- Usage examples
- License and citation

### 5. Spaces Interaction

Explore HuggingFace Spaces:

- Discover demo applications
- Find interactive ML tools
- Access Gradio/Streamlit apps

## MCP Server Integration

This skill uses the `huggingface` MCP server configured in the plugin. The server provides access to HuggingFace Hub API.

### Authentication

The HuggingFace MCP server uses OAuth authentication:

1. First use will prompt for authentication
2. Log in to your HuggingFace account in browser
3. Authorize the application
4. Token is saved for future sessions

## Common Tasks

### Text Generation Models

- `gpt2`, `facebook/opt-*` - Open-source language models
- `meta-llama/Llama-*` - Meta's Llama models
- `mistralai/Mistral-*` - Mistral AI models
- `google/gemma-*` - Google's Gemma models

### Image Generation Models

- `stabilityai/stable-diffusion-*` - Stable Diffusion
- `runwayml/stable-diffusion-*` - RunwayML models
- `black-forest-labs/FLUX.*` - FLUX models

### NLP Tasks

- `bert-base-uncased` - BERT for embeddings
- `sentence-transformers/*` - Sentence embeddings
- `facebook/bart-*` - BART for summarization

### Computer Vision

- `openai/clip-*` - CLIP for image-text
- `google/vit-*` - Vision Transformer
- `facebook/detr-*` - Object detection

## Workflow Patterns

### Finding a Model for a Task

1. Identify the task (e.g., text classification)
2. Search models with task filter
3. Sort by downloads or likes
4. Review model cards for top results
5. Check license compatibility
6. Note installation requirements

### Exploring Datasets for Research

1. Define data requirements
2. Search with relevant keywords
3. Filter by language if needed
4. Review dataset cards
5. Check data splits and sizes
6. Verify license for intended use

### Comparing Models

1. Search models for specific task
2. Review benchmark results
3. Compare model sizes
4. Check inference speed
5. Evaluate community feedback

## Best Practices

1. **Check Model Cards**: Always read model cards for usage instructions
2. **Verify Licenses**: Ensure license compatibility with your use case
3. **Note Requirements**: Check model size and hardware requirements
4. **Use Filters**: Combine task and library filters for better results
5. **Check Community**: Review discussions and issues
6. **Consider Size**: Balance model performance vs. resource needs

## Common Model Libraries

| Library | Use Case |
|---------|----------|
| `transformers` | NLP, vision, audio models |
| `diffusers` | Image generation models |
| `sentence-transformers` | Text embeddings |
| `timm` | Vision models |
| `peft` | Parameter-efficient fine-tuning |
| `trl` | Reinforcement learning |

## Common Tasks

| Task | Description |
|------|-------------|
| `text-generation` | Generate text |
| `text-classification` | Classify text |
| `question-answering` | Answer questions |
| `summarization` | Summarize text |
| `translation` | Translate text |
| `image-classification` | Classify images |
| `object-detection` | Detect objects |
| `text-to-image` | Generate images from text |
| `automatic-speech-recognition` | Speech to text |

## Example Usage

When user requests: "Find a good model for sentiment analysis"

Process:

1. Search models with task: text-classification
2. Add keyword: "sentiment"
3. Sort by downloads
4. Review top model cards
5. Check model sizes and requirements
6. Recommend based on user needs

## Integration with Other Skills

- **academic-research**: Find models for research projects
- **data-visualization**: Use models for data analysis
- **experiment-tracking**: Track model experiments
