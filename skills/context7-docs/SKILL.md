---
name: context7-docs
description: Real-time code documentation retrieval skill using Context7 MCP. Use when you need up-to-date library documentation, version-specific API references, or accurate code examples. Keywords include documentation, API reference, library docs, code examples, SDK documentation, framework documentation, package documentation.
---

# Context7 Documentation Skill

This skill provides access to real-time, up-to-date documentation for programming libraries and frameworks through the Context7 MCP server.

## Core Capabilities

### 1. Real-Time Documentation Retrieval
Get the latest documentation directly from source:
- **Library Documentation**: Access current docs for popular libraries
- **Version-Specific Info**: Get documentation for specific library versions
- **API References**: Retrieve accurate API signatures and parameters
- **Code Examples**: Get working code samples from official sources

### 2. Supported Libraries and Frameworks

Context7 supports documentation for a wide range of technologies:

#### JavaScript/TypeScript
- React, Next.js, Vue.js, Angular
- Node.js, Express, Fastify
- TypeScript, Deno, Bun
- Testing: Jest, Vitest, Playwright

#### Python
- FastAPI, Django, Flask
- NumPy, Pandas, Scikit-learn
- PyTorch, TensorFlow, JAX
- asyncio, httpx, requests

#### Other Languages
- Rust: tokio, actix, serde
- Go: standard library, popular frameworks
- Java: Spring, Quarkus
- And many more...

### 3. Key Benefits
- **Eliminates Hallucinated APIs**: Avoid outdated or non-existent method calls
- **Version Accuracy**: Get docs matching your actual library version
- **Reduced Context Switching**: No need to open browser tabs for docs
- **Always Current**: Documentation updates reflected in real-time

## MCP Server Integration

This skill uses the `context7` MCP server configured in the plugin. The server provides documentation retrieval tools.

### Usage Pattern

To use Context7 in your prompts, include "use context7" in your request:

```
use context7 - How do I create a React Server Component?
```

Or ask for specific library documentation:

```
use context7 - Show me the FastAPI dependency injection syntax
```

## Workflow Patterns

### Learning a New Library

1. Ask for library overview with "use context7"
2. Request specific API documentation
3. Get working code examples
4. Understand best practices from official docs

### Debugging API Issues

1. Describe the error or unexpected behavior
2. Use context7 to get correct API signature
3. Compare with your implementation
4. Get updated code example

### Upgrading Dependencies

1. Specify the target version
2. Request migration guide or changelog
3. Get updated API patterns for new version
4. Review breaking changes

### Writing New Features

1. Describe your goal
2. Use context7 for relevant API documentation
3. Get code examples for similar use cases
4. Implement with accurate, current APIs

## Best Practices

1. **Be Specific**: Include library name and version when known
2. **State Your Goal**: Describe what you're trying to accomplish
3. **Include Context**: Mention your runtime environment if relevant
4. **Ask for Examples**: Request working code samples when needed
5. **Verify Versions**: Confirm documentation matches your installed version

## Environment Configuration

Set your Context7 API key as an environment variable:

```bash
export CONTEXT7_API_KEY=your_api_key_here
```

## Example Usage

When user requests: "use context7 - How do I set up authentication in Next.js 14?"

Process:
1. Context7 retrieves latest Next.js 14 authentication docs
2. Returns current API patterns and middleware setup
3. Provides working code examples
4. Includes links to official documentation

## Integration with Other Skills

- **academic-writing**: Get accurate library citations and documentation references
- **latex-writing**: Include correct API signatures in technical papers
- **git-research**: Document code changes with accurate API information
- **experiment-tracking**: Record correct library versions and APIs used

## Troubleshooting

### Common Issues

1. **No Results**: Check if the library is supported by Context7
2. **Outdated Info**: Specify the exact version you need
3. **API Key Issues**: Verify CONTEXT7_API_KEY environment variable is set

### Getting Help

For Context7 support and updates, visit:
- GitHub: https://github.com/upstash/context7-mcp
- Documentation: https://context7.com
