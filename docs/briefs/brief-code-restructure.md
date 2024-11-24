# CodeMapper Code Restructure Implementation Brief

> [!TIP]
> Advice from Claude on restructuring our CodeMapper codebase for improved modularity, maintainability, and adherence to the single responsibility principle.

[[toc]]

## Overview

This document outlines a comprehensive plan to restructure the CodeMapper codebase to improve modularity, maintainability, and adherence to the single responsibility principle. The restructuring aims to better align the code organization with its documentation while maintaining all existing functionality.

## Current Issues

### 1. Module Organization

- Utility functions are scattered across different modules
- Mixed responsibilities within modules
- Inconsistent error handling approaches
- Lack of clear separation between core functionality and utilities

### 2. Documentation-Code Alignment

- Documentation suggests a simpler structure than actual implementation
- Missing clear boundaries between components
- Inconsistent error handling patterns

### 3. Testing Challenges

- Current structure makes unit testing difficult
- Tightly coupled components
- Mixed responsibilities complicate test isolation

## Proposed Directory Structure

```tree
src/codemapper/
├── __init__.py
├── main.py                      # CLI interface and orchestration
├── config.py                    # Global configuration and constants
├── exceptions.py                # Custom exceptions
├── core/
│   ├── __init__.py
│   ├── processor.py            # Core mapping logic
│   └── docmap.py              # Documentation mapping functionality
├── utils/
│   ├── __init__.py
│   ├── fs.py                  # File system operations
│   ├── git.py                 # Git operations
│   ├── logging.py            # Logging configuration and utilities
│   ├── markdown.py           # Markdown generation utilities
│   └── path.py               # Path handling and validation
└── constants/
    ├── __init__.py
    ├── file_types.py         # File type definitions and mappings
    └── messages.py           # Error and log messages
```

## Module Responsibilities

### 1. Core Components

#### main.py

```python
"""CLI interface and orchestration for CodeMapper."""

def parse_arguments() -> argparse.Namespace:
    """Handle CLI argument parsing."""

def main() -> None:
    """Main orchestration function."""
```

#### core/processor.py

```python
"""Core mapping logic for CodeMapper."""

class CodeMapper:
    """Main class for handling codebase mapping operations."""

    def process_directory(self) -> str:
        """Process directory and generate markdown."""

    def process_github_repo(self) -> str:
        """Process GitHub repository and generate markdown."""
```

#### core/docmap.py

```python
"""Documentation mapping functionality."""

class DocMapper:
    """Documentation mapping and processing."""

    def generate_doc_map(self) -> str:
        """Generate documentation map."""
```

### 2. Utility Modules

#### utils/fs.py

```python
"""File system utilities."""

def collect_file_paths(directory: str) -> List[str]:
    """Collect file paths respecting gitignore."""

def read_file_content(path: str) -> str:
    """Read and process file content."""
```

#### utils/git.py

```python
"""Git operations utilities."""

def clone_repository(url: str) -> str:
    """Clone and manage GitHub repositories."""

def parse_gitignore(path: str) -> pathspec.PathSpec:
    """Parse gitignore specifications."""
```

#### utils/markdown.py

```python
"""Markdown generation utilities."""

def generate_toc(paths: List[str]) -> str:
    """Generate table of contents."""

def format_code_block(content: str, language: str) -> str:
    """Format code blocks with proper syntax highlighting."""
```

## Error Handling Strategy

### 1. Custom Exceptions

```python
# exceptions.py

class CodeMapperError(Exception):
    """Base exception for CodeMapper."""

class GitOperationError(CodeMapperError):
    """Git operation related errors."""

class FileSystemError(CodeMapperError):
    """File system operation errors."""

class ValidationError(CodeMapperError):
    """Input validation errors."""
```

### 2. Error Handling Pattern

```python
try:
    result = operation()
except SpecificError as e:
    logger.error("Operation failed: %s", str(e))
    raise CodeMapperError(f"Operation failed: {str(e)}") from e
```

## Implementation Plan

### Phase 1: Core Restructuring

1. Create new directory structure
2. Move existing code to appropriate modules
3. Update imports and dependencies
4. Implement custom exceptions

### Phase 2: Functionality Migration

1. Migrate file system operations
2. Migrate git operations
3. Migrate markdown generation
4. Update main orchestration logic

### Phase 3: Testing and Documentation

1. Update test structure to match new organization
2. Add unit tests for new modules
3. Update documentation to reflect new structure
4. Add inline documentation for new components

### Phase 4: Error Handling

1. Implement custom exceptions
2. Update error handling throughout codebase
3. Standardize logging approach
4. Add error recovery mechanisms

## Testing Strategy

### 1. Unit Tests

```python
# tests/test_fs.py
def test_collect_file_paths():
    """Test file path collection."""

# tests/test_git.py
def test_clone_repository():
    """Test repository cloning."""
```

### 2. Integration Tests

```python
# tests/integration/test_processor.py
def test_complete_mapping_flow():
    """Test complete mapping process."""
```

## Logging Strategy

### 1. Configuration

```python
# utils/logging.py
def configure_logging() -> None:
    """Configure logging with appropriate formatters and handlers."""
```

### 2. Usage Pattern

```python
logger = logging.getLogger(__name__)
logger.info("Processing directory: %s", directory_path)
```

## Migration Guide

1. **For Contributors:**
   - Overview of new structure
   - Guidelines for moving code
   - Testing requirements
   - Documentation requirements

2. **For Users:**
   - No breaking changes in public API
   - Improved error messages
   - Better logging for debugging
   - Enhanced documentation

## Success Metrics

1. **Code Quality:**
   - Improved pylint scores
   - Reduced cyclomatic complexity
   - Better test coverage

2. **Maintenance:**
   - Reduced time to implement new features
   - Faster bug resolution
   - Clearer error messages

3. **User Experience:**
   - More consistent error handling
   - Better debugging information
   - Improved documentation

## Timeline

1. Phase 1: 2-3 days
2. Phase 2: 3-4 days
3. Phase 3: 2-3 days
4. Phase 4: 2-3 days

Total estimated time: 9-13 days

## Risks and Mitigations

1. **Regression Risks:**
   - Comprehensive test suite before and after
   - Gradual migration with verification
   - User beta testing period

2. **Performance Impact:**
   - Benchmark key operations
   - Profile new structure
   - Optimize critical paths

3. **Migration Challenges:**
   - Clear documentation
   - Staged rollout
   - Revert plan if needed

## Future Considerations

1. **Extensibility:**
   - Plugin system
   - Custom formatters
   - Additional output formats

2. **Performance:**
   - Async file operations
   - Parallel processing
   - Caching mechanisms

3. **Integration:**
   - IDE plugins
   - CI/CD integration
   - API endpoints

## Success Criteria

1. All existing functionality maintained
2. Improved test coverage (target: 90%+)
3. Clear separation of concerns
4. Consistent error handling
5. Comprehensive documentation
6. Maintainable codebase
