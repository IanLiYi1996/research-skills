# HuggingFace Command

Search and explore HuggingFace Hub for models, datasets, and Spaces.

## Purpose

Access HuggingFace ecosystem:

- Search for pretrained models
- Find datasets for training
- Get model and dataset documentation
- Explore ML applications in Spaces

## Usage

```bash
/huggingface [action] [arguments] [options]
```

**Actions:**

- `search-models` - Search for models
- `search-datasets` - Search for datasets
- `model-info` - Get model details
- `dataset-info` - Get dataset details

## Search Models Examples

### Basic Model Search

```bash
/huggingface search-models "text generation"
```

Searches for text generation models.

### Search by Task

```bash
/huggingface search-models --task text-classification
```

Finds all text classification models.

### Search by Library

```bash
/huggingface search-models --library transformers --task question-answering
```

Finds question-answering models using transformers.

### Combined Search

```bash
/huggingface search-models "sentiment" --task text-classification --limit 10
```

Searches sentiment analysis models, returns top 10.

## Search Datasets Examples

### Basic Dataset Search

```bash
/huggingface search-datasets "medical images"
```

Searches for medical image datasets.

### Search by Task

```bash
/huggingface search-datasets --task text-classification
```

Finds datasets for text classification.

### Search by Language

```bash
/huggingface search-datasets "news" --language zh
```

Searches Chinese news datasets.

## Model Info Examples

### Get Model Details

```bash
/huggingface model-info meta-llama/Llama-2-7b
```

Shows full model card for Llama 2.

### Get Specific Model Version

```bash
/huggingface model-info stabilityai/stable-diffusion-xl-base-1.0
```

Shows SDXL model documentation.

## Dataset Info Examples

### Get Dataset Details

```bash
/huggingface dataset-info imdb
```

Shows IMDB dataset documentation.

### Get Dataset with Config

```bash
/huggingface dataset-info squad --config squad_v2
```

Shows SQuAD v2 configuration details.

## Search Options

| Option | Description | Example |
|--------|-------------|---------|
| `--task` | Filter by ML task | `--task text-generation` |
| `--library` | Filter by framework | `--library diffusers` |
| `--language` | Filter by language | `--language en` |
| `--limit` | Max results | `--limit 20` |
| `--sort` | Sort order | `--sort downloads` |

## Common Tasks

### Text Tasks

| Task | Description |
|------|-------------|
| `text-generation` | Generate text |
| `text-classification` | Classify text |
| `question-answering` | Answer questions |
| `summarization` | Summarize text |
| `translation` | Translate text |
| `fill-mask` | Fill masked tokens |
| `text2text-generation` | Text to text |

### Vision Tasks

| Task | Description |
|------|-------------|
| `image-classification` | Classify images |
| `object-detection` | Detect objects |
| `image-segmentation` | Segment images |
| `text-to-image` | Generate images |
| `image-to-text` | Describe images |

### Audio Tasks

| Task | Description |
|------|-------------|
| `automatic-speech-recognition` | Speech to text |
| `text-to-speech` | Text to speech |
| `audio-classification` | Classify audio |

### Multimodal Tasks

| Task | Description |
|------|-------------|
| `visual-question-answering` | Answer image questions |
| `document-question-answering` | Answer document questions |

## Common Libraries

| Library | Use Case |
|---------|----------|
| `transformers` | NLP, vision, audio |
| `diffusers` | Image generation |
| `sentence-transformers` | Embeddings |
| `timm` | Vision models |
| `peft` | Fine-tuning |

## Output Format

### Model Search Results

For each model found:

- Model ID (org/name)
- Downloads count
- Likes count
- Task tags
- Library tags
- Last updated

### Model Info

Full model card including:

- Description and use cases
- Training details
- Performance benchmarks
- Usage examples
- License
- Citation

### Dataset Search Results

For each dataset found:

- Dataset ID
- Downloads count
- Size information
- Task tags
- Languages

### Dataset Info

Full dataset card including:

- Description and features
- Data splits
- Column information
- Usage examples
- License
- Citation

## Workflow Tips

1. **Start with Task**: Filter by task to narrow results
2. **Check Downloads**: Popular models are often reliable
3. **Read Model Cards**: Check requirements and limitations
4. **Verify License**: Ensure compatibility with your use case
5. **Note Size**: Consider model size for your hardware

## Authentication

HuggingFace MCP server uses OAuth authentication:

1. First command triggers authentication prompt
2. Log in to HuggingFace in browser
3. Authorize the application
4. Continue using commands

No environment variables needed - authentication is handled automatically.

## Requirements

- Internet connection
- HuggingFace account (free)
- Browser for OAuth authentication (first time only)
