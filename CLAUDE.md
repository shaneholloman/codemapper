# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CodeMapper is a Python CLI tool that transforms complex codebases into navigable, single-file Markdown artifacts. It generates two types of outputs:

- **CodeMap** (`*_codemap.md`): Complete directory tree + all file contents with syntax highlighting
- **DocMap** (`*_docmap.md`): Documentation-focused view (README + docs directories)

The tool is designed for AI engineers (training data, AI chat bootstrapping) and hobbyists (project exploration, documentation).

## Development Commands

### Installation and Setup

```bash
# Development installation
uv venv
uv sync

# Install dev dependencies
uv add --dev ruff ty pytest

# Build the package
uv build
```

### Testing

```bash
# Run all tests
uv run pytest -v tests/test_github_codemapper.py

# Run specific test
uv run pytest -v tests/test_github_codemapper.py::test_function_name
```

### Linting and Formatting

```bash
# Lint with ruff (as CI does)
uv run ruff check .

# Format with ruff (line-length: 100)
uv run ruff format .

# Check formatting without making changes
uv run ruff format --check .

# Type check with ty
uv run ty check src/

# Fix auto-fixable issues
uv run ruff check --fix .
```

### Running the Tool

```bash
# Basic usage
codemapper /path/to/project

# Generate documentation map
codemapper --docs /path/to/project

# Process GitHub repository (shallow clone, depth=1)
codemapper https://github.com/username/repo

# Exclude specific directories
codemapper --exclude=tests --exclude=docs /path/to/project

# Include git-ignored files
codemapper --include-ignored /path/to/project
```

## Architecture

### Core Modules

**main.py** (src/codemapper/main.py:28)

- Entry point and CLI argument parsing
- Orchestrates the entire generation process
- Routes to either codemap or docmap generation based on --docs flag
- Handles both local directories and GitHub URLs

**utils.py** (src/codemapper/utils.py)

- Core utility functions for file processing
- `generate_markdown_document()`: Main codemap generation function
- `collect_file_paths()`: Walks directory tree respecting gitignore
- `read_file_content()`: Reads files with encoding detection (chardet)
- `generate_file_tree()`: Creates ASCII tree representation
- `clone_github_repo()`: Handles GitHub shallow cloning (--depth 1)
- Always excludes: .git, .venv, .conda, node_modules

**docmap.py** (src/codemapper/docmap.py:96)

- Documentation-focused generation
- `generate_docmap_content()`: Main docmap generation function
- `find_documentation_directory()`: Searches for docs/, wiki/, documentation/
- `process_readme()`: Extracts and processes README.md

**config.py** (src/codemapper/config.py)

- Configuration dataclasses: `BaseMapConfig`, `CodeMapConfig`, `DocMapConfig`
- Constants: `CODEMAP_SUFFIX`, `DOCMAP_SUFFIX`, `DOC_DIRECTORIES`
- File type mappings: `CODE_FENCE_MAP`, `LARGE_FILE_EXTENSIONS`, `ARCHIVE_EXTENSIONS`

### Data Flow

1. **Input Detection** (main.py:71): Detect local path vs GitHub URL
2. **Repository Preparation**: Clone if GitHub, or use local path
3. **Gitignore Loading** (utils.py:69): Parse .gitignore rules with pathspec library
4. **Configuration Creation**: Build `CodeMapConfig` or `DocMapConfig` dataclass
5. **Content Generation**: Call appropriate generation function
6. **Output Management**: Write to `.codemaps/` directory

### Output Structure

CodeMap sections:

1. Table of Contents (auto-generated from file paths)
2. Repo File Tree (ASCII tree with counts)
3. Repo File Contents (syntax-highlighted code blocks)

DocMap sections:

1. Project README (if exists)
2. Documentation Directory structure and contents

## Key Patterns and Conventions

### Configuration Pattern

All generation functions accept dataclass configuration objects (not individual parameters). This pattern was introduced for maintainability:

```python
# Create config object
config = CodeMapConfig(
    directory_path=path,
    gitignore_spec=spec,
    include_ignored=False,
    source=source,
    base_name=name,
    exclude_dirs=['tests']
)

# Pass to generator
markdown = generate_markdown_document(config)
```

### File Exclusion Logic

Default exclusions are hardcoded (src/codemapper/utils.py:31-53):

- Always excluded: .git, .venv, .conda, node_modules
- Archive files are skipped: .zip, .tar, .gz, .rar, .7z, etc.
- Large/binary files show metadata only: images, videos, PDFs, executables, etc.

Gitignore is respected by default unless --include-ignored flag is used.

### Markdown Fencing

- Regular code files use triple backticks (```)
- Markdown files use quadruple backticks (````) to nest properly (src/codemapper/utils.py:335)
- Code fence language is auto-detected from file extension (src/codemapper/utils.py:56)

### Encoding Handling

Files are read with encoding detection (chardet library):

1. Detect encoding from first 1024 bytes
2. Try detected encoding, then UTF-8, then Latin-1
3. If all fail, return error message (src/codemapper/utils.py:242)

## CI/CD Pipeline

### GitHub Actions Workflows

**.github/workflows/ruff.yml:**

- Runs on: push, workflow_dispatch
- Python versions: 3.10, 3.11, 3.12
- Lints with ruff, checks formatting, and type checks with ty

**.github/workflows/pytest.yml:**

- Runs on: push to main, pull_request, workflow_dispatch
- Python versions: 3.10, 3.11, 3.12
- Runs single test file: tests/test_github_codemapper.py

**.github/workflows/update-todo-badges.yml:**

- Updates TODO badge count in README.md

## Testing Strategy

Tests use pytest with tempfile for isolated test environments. Key test areas:

- Directory exclusion logic
- Code fence determination
- Gitignore parsing and matching
- File path collection with/without gitignore
- Large file detection
- Encoding detection and content reading
- Integration test with sample repo structure

## Important Notes

- GitHub cloning is ALWAYS shallow (--depth 1) for performance
- Output directory is always `.codemaps/` in current working directory
- Output files use dot notation: `project.codemap.md`, `project.docmap.md`
- README.md is prioritized first in TOC and file listings
- Binary/large files are acknowledged but contents not displayed
- Tool supports Python 3.10, 3.11, 3.12

## Project Structure Highlights

```tree
codemapper/
├── src/codemapper/          # Main package
│   ├── main.py             # CLI entry point
│   ├── utils.py            # Core utilities (codemap generation)
│   ├── docmap.py           # Documentation mapping
│   └── config.py           # Configuration and constants
├── tests/                   # Test suite
│   └── test_github_codemapper.py
├── docs/                    # Project documentation
├── wip/                     # Work in progress features
└── pyproject.toml          # Package configuration
```

## Dependencies

Core runtime:

- chardet: Encoding detection
- pathspec: Gitignore pattern matching

Development/testing:

- pytest: Test framework
- ruff: Fast linter and formatter (line-length=100)
- ty: Astral's fast type checker (pre-alpha)
