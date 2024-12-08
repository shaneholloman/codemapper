# CodeMapper

[![Pylint](https://github.com/shaneholloman/codemapper/actions/workflows/pylint.yml/badge.svg)](https://github.com/shaneholloman/codemapper/actions/workflows/pylint.yml)
[![PyTest](https://github.com/shaneholloman/codemapper/actions/workflows/pytest.yml/badge.svg)](https://github.com/shaneholloman/codemapper/actions/workflows/pytest.yml)
[![TODO](https://img.shields.io/badge/✔%20Todo-45-purple)](docs/todo.md)
[![TODO](https://img.shields.io/badge/✔%20Done-7-purple)](docs/todo.md)

![logo](codemapper-outlined.webp)

<!-- TOC -->

- [CodeMapper](#codemapper)
  - [Overview](#overview)
  - [Key Features](#key-features)
  - [AI Chat Integration](#ai-chat-integration)
  - [Use Cases](#use-cases)
    - [For AI Engineers](#for-ai-engineers)
    - [For Hobbyists](#for-hobbyists)
  - [Getting Started](#getting-started)
  - [Example Output](#example-output)
  - [Future Development](#future-development)
  - [Target Audiences](#target-audiences)
    - [AI Engineers Will Appreciate](#ai-engineers-will-appreciate)
    - [Hobbyists Will Value](#hobbyists-will-value)
  - [Installation Options](#installation-options)
  - [Contributing](#contributing)
  - [Resources](#resources)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)
  - [Version History](#version-history)

<!-- /TOC -->

## Overview

> [!IMPORTANT]
> CodeMapper: Bridging Code Understanding for AI and Human Analysis
>
> Install: `pip install codemapper`

CodeMapper is a powerful Python tool that transforms complex codebases into navigable, single-file Markdown artifacts, with a unique ability to bootstrap AI chat prompts for code analysis. Designed with both AI engineers and hobbyist developers in mind, it serves as a bridge between traditional code exploration and modern AI-assisted development workflows. Whether you're training large language models, conducting interactive AI-assisted code reviews, or simply trying to understand a new project, CodeMapper provides a unified, accessible view of your codebase that's optimized for both human readability and AI consumption.

## Key Features

- **Unified Code Visualization**: Automatically generates a comprehensive Markdown representation of your entire codebase, including:
  - Complete directory structure visualization
  - Syntax-highlighted code content
  - Intelligent file categorization
  - Documentation aggregation

- **AI Integration Optimizations**:
  - Structured output format ideal for LLM training and analysis
  - Consistent formatting for improved token efficiency
  - Built-in support for common documentation patterns
  - Metadata preservation for enhanced context

- **Git-Aware Processing**:
  - Respects `.gitignore` rules by default
  - Direct GitHub repository URL support
  - Handles large repositories efficiently
  - Smart binary file detection

- **Documentation Focus**:
  - Dedicated DocMap generation for documentation-heavy projects
  - README file prioritization
  - Support for multiple documentation directory conventions
  - Markdown-native output for universal compatibility

## AI Chat Integration

CodeMapper excels at bootstrapping AI chat interactions for code analysis. When you need to understand, debug, or enhance your code with AI assistance:

1. Generate a codemap of your project
2. Copy the generated markdown into your AI chat
3. Start asking detailed questions about your codebase

The AI assistant receives:

- Complete project structure
- All file contents with proper syntax highlighting
- Documentation in context
- Clear navigation structure

This enables the AI to provide more accurate, contextual responses about your code without manual file copying or context limitations.

## Use Cases

### For AI Engineers

- **AI Chat Prompt Bootstrapping**: Instantly generate context-rich prompts for AI chat interactions about your code
- **Interactive Code Analysis**: Seamlessly feed comprehensive codebase context to AI assistants
- **Training Data Preparation**: Generate consistently formatted codebase representations for model training
- **Documentation Generation**: Train models on well-structured documentation patterns
- **Code Understanding**: Feed entire codebases to LLMs for comprehensive analysis

> [!TIP]
> Example AI Chat Workflow:

```bash
# Generate a codemap for your project
codemapper /path/to/project_or_repo

# The generated codemap can be directly used in AI chat prompts:
"Here's my project structure and code, help me understand the dependency flow:
[paste or add to you project knowledge *_codemap.md content]"
```

### For Hobbyists

- **Project Exploration**: Quickly understand new codebases without complex IDE setup
- **Documentation Creation**: Generate comprehensive project documentation automatically
- **Code Reviews**: Facilitate easier code reviews with a unified view
- **Learning Tool**: Study and understand how different projects are structured

## Getting Started

```bash
# Install from PyPI
pip install codemapper

# Basic usage
codemapper /path/to/project

# Generate documentation map
codemapper --docs /path/to/project

# Process GitHub repository
codemapper https://github.com/username/repo
```

## Example Output

CodeMapper generates two main types of outputs:

1. **CodeMap** (`project_codemap.md`):
   - Complete directory tree
   - File contents with syntax highlighting
   - Smart handling of binary and large files
   - Navigation-optimized structure

2. **DocMap** (`project_docmap.md`):
   - Documentation-focused view
   - README files
   - Documentation directory contents
   - Structured for easy consumption

## Future Development

> [!NOTE]
> CodeMapper welcomes help while actively focused on:

[ToDos](docs/todo.md)

- Expanded format support (XML, JSON, YAML, RST)
- Enhanced AI integration capabilities
- Real-time code change tracking
- Collaborative annotation features
- Intelligent code pattern recognition
- API access for programmatic integration

## Target Audiences

### AI Engineers Will Appreciate

- Consistent, clean output format for training data
- Efficient handling of large repositories
- Structured metadata preservation
- Integration-ready design

### Hobbyists Will Value

- Simple, straightforward installation
- Clear, readable output
- No complex configuration required
- Immediate utility for project understanding

## Installation Options

```bash
# For basic installation
pip install codemapper

# For development installation
git clone https://github.com/shaneholloman/codemapper
cd codemapper
pip install -e .
```

## Contributing

CodeMapper welcomes contributions from both AI engineers and hobbyist developers. The project maintains a balance between sophisticated features for AI integration and accessibility for general use.

Visit the [GitHub repository](https://github.com/shaneholloman/codemapper) to:

- Report issues
- Submit feature requests
- Contribute code
- Join the discussion

## Resources

- [GitHub Repository](https://github.com/shaneholloman/codemapper)
- [PyPI Package](https://pypi.org/project/codemapper/)
- [Issue Tracker](https://github.com/shaneholloman/codemapper/issues)
- [Changelog](https://github.com/shaneholloman/codemapper/blob/main/changelog.md)

CodeMapper represents a bridge between traditional code exploration and modern AI-assisted development, making codebases more accessible and understandable for everyone from AI researchers to hobbyist developers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the `pathspec` and `chardet` libraries for enhancing CodeMapper's functionality.

## Version History

For a detailed version history, please refer to the [changelog.md](changelog.md).

---

If you find CodeMapper useful, don't forget to star this repository!
