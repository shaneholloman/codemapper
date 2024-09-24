# Changelog

## Version History

- 3.2.0 (2024-09-23):
  - Improved handling of large and binary files:
    - Large and binary files are now always acknowledged without attempting to print their contents
    - File type and size information is displayed for large and binary files
  - Removed option to include large file contents as it's not practical for binary files
  - Simplified command-line options by removing flags related to large file handling

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
  - Added '_mapped' output directory for generated markdown files
  - Improved error handling and user feedback

- 2.5.0 (2024-09-10):
  - Initial version
  - Basic functionality for local directory mapping