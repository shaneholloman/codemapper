# CodeMapper XML Export Feature Implementation Brief

[[toc]]

## Overview

This brief outlines the implementation plan for adding XML export capability to CodeMapper, allowing the tool to generate structured XML representations of codebases. The feature will complement existing Markdown output, providing a more machine-readable format for automated processing and integration with other tools.

## Core Requirements

### Command Line Interface

- Add new flag `--xml` to generate XML output
- Optional flag `--xml-output=<filename>` to specify custom output filename
- Usage examples:

    ```bash
    codemapper --xml repo-url           # Generate standard XML output
    codemapper --xml --xml-output=custom.xml repo-url  # Custom filename
    ```

### XML Content Scope

1. Repository Metadata
   - Repository name and description
   - Fetch date and time
   - Branch information
   - Source (local/GitHub)

2. Directory Structure
   - Complete tree representation
   - File and directory attributes
   - Gitignore rules applied

3. File Contents
   - Original file content with CDATA sections
   - File metadata (size, permissions, type)
   - Content encoding information

### Output Format

```xml
<?xml version="1.0" encoding="UTF-8"?>
<codemap>
    <!-- This XML document provides a comprehensive overview of the directory structure
         and file contents. It aims to give machines and automation tools a complete,
         structured view of the codebase in a single XML file for easy parsing
         and analysis. -->
    <repository>
        <metadata>
            <name>repository-name</name>
            <source>dir-path-or-url</source>
            <description>Repository contents for LLM context</description>
            <fetch_date>YYYY-MM-DDThh:mm:ss.SSSZ</fetch_date>
            <branch>main</branch>
        </metadata>
        <tree_structure>
            <![CDATA[
            .
            ├── dir1/
            │   ├── file1.py
            │   └── file2.py
            └── dir2/
                └── file3.py
            ]]>
        </tree_structure>
        <contents>
            <directory name="dir1" path="dir1">
                <file name="file1.py" path="dir1/file1.py">
                    <content><![CDATA[
                        # File content here
                    ]]></content>
                </file>
                <!-- Additional files -->
            </directory>
            <!-- Additional directories -->
        </contents>
    </repository>
</codemap>
```

## Technical Implementation

### New Module (xml_export.py)

```python
"""Pseudo-code for XML export functionality."""

from dataclasses import dataclass
from typing import Optional
import xml.etree.ElementTree as ET

@dataclass
class XMLExportConfig:
    """Configuration class for XML export generation."""
    directory_path: str
    gitignore_spec: pathspec.PathSpec
    include_ignored: bool = False
    output_path: Optional[str] = None

def generate_xml_content(config: XMLExportConfig) -> ET.Element:
    """Generate XML representation of repository."""
    root = ET.Element("llm_context")
    repo = ET.SubElement(root, "repository")

    # Add metadata
    add_metadata(repo, config)

    # Add tree structure
    add_tree_structure(repo, config)

    # Add contents
    add_contents(repo, config)

    return root

def write_xml_output(xml_content: ET.Element, output_path: str) -> None:
    """Write formatted XML to file."""
    tree = ET.ElementTree(xml_content)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
```

### Required Updates to Existing Files

1. main.py:
   - Add XML command line arguments
   - Integrate XML export logic
   - Update output file handling

2. utils.py:
   - Add XML-specific utility functions
   - Update tree generation for XML format

3. config.py:
   - Add XML-related constants
   - Define XML output configurations

## Implementation Order

1. Create XMLExportConfig class and basic structure
2. Implement tree structure generation
3. Add file content processing with CDATA
4. Integrate metadata collection
5. Add CLI options
6. Implement output formatting and writing
7. Add tests and documentation

## Future Extensibility

- Support for custom XML schemas
- Additional metadata fields
- Alternative XML formats
- XML validation options
- XML compression options

## Error Handling

1. XML Escaping:

    ```python
    def escape_xml_content(content: str) -> str:
        """Escape special characters in XML content."""
        # Implement proper XML escaping while preserving format
    ```

2. File Encoding:

    ```python
    def handle_file_encoding(file_path: str) -> Tuple[str, str]:
        """Detect and handle file encoding for XML output."""
        # Implement encoding detection and conversion
    ```

## Testing Strategy

1. Unit Tests:

    ```python
    def test_xml_generation():
        """Test XML content generation."""
        config = XMLExportConfig(...)
        xml_content = generate_xml_content(config)
        assert validate_xml_structure(xml_content)

    def test_edge_cases():
        """Test handling of special characters and encodings."""
        # Test various edge cases
    ```

2. Integration Tests:

    ```python
    def test_complete_export():
        """Test complete XML export process."""
        # Test end-to-end functionality
    ```

## Validation

1. Schema Validation:

    ```xml
    <!-- XML Schema for output validation -->
    <xs:schema>
        <xs:element name="llm_context">
            <!-- Define schema structure -->
        </xs:element>
    </xs:schema>
    ```

## Success Criteria

1. Generates valid XML adhering to specified schema
2. Preserves all codebase information
3. Handles special characters and encodings correctly
4. Maintains consistent formatting
5. No degradation in performance for large codebases
6. Clear documentation and examples

## Notes

- Use CDATA sections for code content to preserve formatting
- Ensure proper encoding handling for all file types
- Maintain efficient memory usage for large repositories
- Follow XML best practices for structure and naming
- Consider compression for large outputs

This feature enhancement will provide a robust XML export capability while maintaining CodeMapper's existing functionality and performance characteristics.
