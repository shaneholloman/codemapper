# Changelog

## Version History

- 3.8.0 (2024-11-23):
  - refactor: Split codebase into modular structure
    - Split main functionality into separate modules:
      - main.py: Entry point and CLI handling
      - utils.py: Core functionality and helper functions
      - config.py: Configuration constants and settings
    - Improved code organization and maintainability
    - Fixed linting issues and long lines
  - [View Full Changelog](https://github.com/shaneholloman/codemapper/compare/v3.7.0...v3.8.0)

- 3.7.0 (2024-10-02):
  - Added setuptools to dependencies in pylint workflow
  - Updated pylint workflow trigger to include manual dispatch
  - Updated Python versions in pylint workflow to support 3.10, 3.11, and 3.12
  - [View Full Changelog](https://github.com/shaneholloman/codemapper/compare/v3.6.0...v3.7.0)

- 3.6.0 (2024-10-01):
  - Added MIT License to the repository
  - Updated README to include upcoming output formats for CodeMapper
  - Added requirements.txt and updated README for CodeMapper enhancements
  - Rigorously reconciled our readme and function docstrings with each other and with the code itself
  - [View Full Changelog](https://github.com/shaneholloman/codemapper/compare/v3.5.3...v3.6.0)

- 3.5.3 (2024-10-01):
  - Improved large file handling and simplified command-line options
  - [View Full Changelog](https://github.com/shaneholloman/codemapper/compare/v3.5.0...v3.5.3)

- 3.5.0 (2024-09-27):
  - Enhanced Table of Contents (TOC) generation and path normalization
  - Improved handling of large and binary files
  - Simplified command-line options
  - Added PyPI installation support
  - [View Full Changelog](https://github.com/shaneholloman/codemapper/compare/v3.4.5...v3.5.0)

- 3.3.0 (2024-09-24):
  - Improved Table of Contents (TOC) generation:
    - Fixed issue with double dots appearing for hidden files and directories
    - Standardized path separators to forward slashes for cross-platform consistency
    - Corrected handling of file paths with backslashes on Windows systems
  - Enhanced path normalization in file collection process:
    - Ensured consistent use of forward slashes in file paths across all platforms
  - Refined TOC link generation:
    - Removed unwanted '%' characters from TOC links
    - Improved handling of special characters in file and directory names
  - Updated `generate_toc` function for better accuracy and readability:
    - Preserved original path structure, including single leading dots for hidden items
    - Eliminated redundant dot addition for already dot-prefixed paths
  - Optimized `collect_file_paths` function:
    - Implemented consistent path normalization to forward slashes
    - Improved cross-platform compatibility in file path handling

- 3.2.0 (2024-09-23):
  - Improved handling of large and binary files:
    - Large and binary files are now always acknowledged without attempting to print their contents
    - File type and size information is displayed for large and binary files
  - Removed option to include large file contents as it's not practical for binary files
  - Simplified command-line options by removing flags related to large file handling
  - Added PyPI installation support

- 3.1.2 (2024-09-23):
  - Restored important formatting functionality in generate_markdown_document function
  - Ensures proper spacing between file contents and correct placement of the concluding message

- 3.1.1 (2024-09-23):
  - Fixed unused variable issue in generate_markdown_document function
  - Improved code quality without changing functionality

- 3.1.0 (2024-09-23):
  - Added support for GitHub repositories
  - Implemented large file handling (now default in 3.2.0)

- 3.0.0 (2024-09-23):
  - Major refactor
  - Added '_codemaps' output directory for generated markdown files
  - Improved error handling and user feedback

- 2.5.0 (2024-09-10):
  - Initial version
  - Basic functionality for local directory mapping
<!-- TOC -->

- [Changelog](#changelog)
  - [Version History](#version-history)

<!-- /TOC -->
