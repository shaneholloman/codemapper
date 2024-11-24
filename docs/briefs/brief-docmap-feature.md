# CodeMapper DocMap Feature Implementation Brief

[[toc]]

## Feature Overview

Add documentation-specific mapping capability to CodeMapper, generating a separate `*_docmap.md` file that focuses on repository documentation.

## Core Requirements

### Command Line Interface

- Add new flag `--docs` to generate documentation-specific mapping
- Add optional flag `--docs-dir=<custom-path>` to support non-standard documentation directory names
- Usage examples:

  ```bash
  codemapper --docs repo-url           # Generate docmap with standard doc directories
  codemapper --docs --docs-dir=wiki    # Generate docmap with custom doc directory
  ```

### Documentation Content Scope

1. Main README.md file
   - Include root README.md content at the beginning of docmap
   - Do not include READMEs from subdirectories

2. Documentation Directory Content
   - Search for standard documentation directories in this order:
     - /docs
     - /doc
     - /documentation
   - Use first matching directory found
   - Process all files within the found documentation directory

### Output Format

- Generate `repository-name_docmap.md` in the _codemaps directory
- Follow same format and processing rules as codemap:
  - Respect .gitignore rules
  - Handle large files appropriately
  - Apply same markdown formatting

## Technical Implementation

### File Structure

```tree
src/codemapper/
├── __init__.py
├── config.py      # Add doc directory constants
├── main.py        # Add new CLI options
├── utils.py       # Update for suffix handling
└── docmap.py      # New file for doc mapping
```

### New Configuration (config.py)

Add constant for standard documentation directories:

```python
DOC_DIRECTORIES = {
    "docs",
    "doc",
    "documentation"
}
```

### New Module (docmap.py)

Create new module with functions:

- `find_documentation_directory()`: Locate documentation directory
- `process_readme()`: Handle README.md processing
- `generate_docmap_content()`: Generate documentation map content

### Required Updates to Existing Files

1. main.py:
   - Add --docs and --docs-dir arguments
   - Integrate docmap generation logic
   - Update output file handling for different suffixes

2. utils.py:
   - Update manage_output_directory() to handle different output suffixes
   - Any shared utility functions needed by docmap.py

### DocMap Content Structure

```markdown
# {repository_name} Documentation

> DocMap Source: {source}

This markdown document provides a comprehensive overview of the documentation
files and structure. It aims to give viewers (human or AI) a complete view
of the project's documentation in a single file for easy analysis.

## Project README

{README.md content}

## Documentation Directory: {directory_name}

### Directory Structure
{tree structure of documentation directory}

### Documentation Contents
{Contents of all documentation files}

> This concludes the documentation mapping. Please review thoroughly for a
> comprehensive understanding of the project's documentation.
```

### Error Handling

1. No Documentation Directory:
   - If README exists: Generate docmap with just README
   - If no README: Display informative message and exit gracefully

2. Invalid Custom Directory:
   - Display error message if --docs-dir path doesn't exist
   - Exit with appropriate error code

### Future Extensibility Considerations

- Config file could be extended to include additional doc directory patterns
- Additional documentation-specific processing could be added
- Support for documentation-specific file types could be enhanced

## Implementation Notes

1. Code Organization:
   - Separate docmap.py module for better maintainability
   - Keep files at reasonable sizes for easier management
   - Follow existing codebase patterns and conventions

2. Processing Rules:
   - Use same file handling logic as existing codemap
   - Maintain consistent markdown formatting
   - Follow same .gitignore rules

3. Documentation Standards:
   - Maintain Google-style docstrings
   - Include type hints
   - Add comprehensive module-level documentation

4. Testing:
   - Add tests for new functionality in existing test files
   - Test with various repository structures
   - Verify error handling

## Usage Examples

```bash
# Basic documentation mapping
codemapper --docs https://github.com/user/repo

# Custom documentation directory
codemapper --docs --docs-dir=wiki https://github.com/user/repo

# Include ignored files
codemapper --docs --include-ignored https://github.com/user/repo
```

## Implementation Order

1. Add DOC_DIRECTORIES to config.py
2. Create new docmap.py module
3. Update utils.py for output suffix handling
4. Modify main.py for new CLI options
5. Add test cases
6. Update documentation

This feature should be implemented following existing CodeMapper patterns and practices, maintaining the same level of code quality and documentation standards.
