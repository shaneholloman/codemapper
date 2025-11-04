# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CodeMapper converts codebases into single-file Markdown documents for LLM context and code analysis. It scans directories or GitHub repositories and generates comprehensive Markdown files with directory structure, file contents, and git metadata.

## Development Commands

### Setup

```bash
# Install with development dependencies
uv sync

# Install tool globally for testing
uv tool install .
```

### Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/codemapper --cov-report=html --cov-report=term

# Run specific test file
uv run pytest tests/unit/test_config.py

# Run specific test
uv run pytest tests/unit/test_config.py::test_function_name
```

### Linting and Formatting

```bash
# Check code with ruff
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .

# Format code
uv run ruff format .

# Type checking
uv run ty src/codemapper
```

### Building

```bash
# Build package
uv build

# Install local development version
uv pip install -e .
```

## Architecture

CodeMapper uses a modular three-stage pipeline:

### 1. Readers (`readers/`)

- **scan_paths.py**: Path scanning and .gitignore handling
- **read_files.py**: File content reading with encoding detection (chardet)
- **detect_types.py**: File type detection and syntax highlighting mapping

### 2. Processors (`processors/`)

- **process_dir.py**: Directory filtering, input type detection (local vs GitHub), source metadata capture
- **process_git.py**: Git info extraction (branch, commit, remote) and GitHub repo cloning

### 3. Builders & Writers (`builders/`, `writers/`)

- **build_codemap.py**: Full codebase mapping (all files)
- **build_docmap.py**: Documentation-only mapping (README + docs/)
- **build_markdown.py**: Markdown generation with directory trees and syntax-highlighted code blocks
- **manage_output.py**: Output directory management

### Configuration System

**Config precedence**: CLI `--output-dir` > `~/.codemapper/codemapper.toml` (`output_dir`) > Config (`prefix_style`) > Default (`.codemaps/`)

Two configuration patterns:

- **Project-level**: `.codemaps/`, `_codemaps/`, or `-codemaps/` in current directory (default)
- **System-level**: Centralized directory via `output_dir` in config file

**Type system**: Uses dataclasses (`types.py`):

- `BaseMapConfig`: Common parameters for all mapping operations
- `CodeMapConfig`: Full codebase mapping configuration
- `DocMapConfig`: Documentation-only mapping configuration (adds `doc_dir` field)

### Key Design Patterns

**Exclusion strategy**: Three-tier filtering

1. Always excluded: `.git/`, `.venv/`, `.conda/`, `node_modules/`
2. Cache/build dirs: `.ruff_cache/`, `__pycache__/`, `dist/`, `build/`
3. User-specified: `--exclude` flag additions

**File size limits**: 300k characters max (approx 75k tokens) - larger files skipped with note

**Binary detection**: Extension-based exclusion (see `LARGE_FILE_EXTENSIONS` in `config.py`)

**Gitignore handling**: Uses `pathspec` library for accurate .gitignore pattern matching

## Testing Strategy

Test suite organized as:

- `tests/unit/`: Module-level tests (69% coverage)
- `tests/integration/`: End-to-end tests
- `tests/fixtures/`: Shared test data
- `conftest.py`: Pytest fixtures and configuration

When adding features, add corresponding unit tests in `tests/unit/test_<module>.py`.

## Important Notes

**Python version**: Requires 3.12+ (uses new type syntax and tomllib)

**Dependencies**:

- `chardet`: Encoding detection for file reading
- `pathspec`: Gitignore pattern matching

**Entry point**: `codemapper.cli:main` (defined in pyproject.toml)

**Help text**: Extracted to `help.py` module (don't modify CLI parser epilog directly)
