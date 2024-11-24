"""
Documentation Mapping Module for CodeMapper.

This module provides functionality to generate comprehensive documentation maps
from repositories, focusing on README files and documentation directories. It works
in conjunction with the main CodeMapper functionality but specifically targets
documentation content.

The module supports scanning for common documentation directories and processing
README.md files to create a complete documentation overview.
"""

import os
import logging
from typing import Optional

import pathspec  # Import pathspec library explicitly

from .config import DOC_DIRECTORIES
from .utils import (
    read_file_content,
    generate_file_tree,
    collect_file_paths,
)

logger = logging.getLogger(__name__)

def find_documentation_directory(base_path: str, custom_dir: Optional[str] = None) -> Optional[str]:
    """
    Find the documentation directory in the given base path.

    Args:
        base_path (str): Base directory path to search in
        custom_dir (Optional[str]): Custom documentation directory path if specified

    Returns:
        Optional[str]: Path to documentation directory if found, None otherwise
    """
    if custom_dir:
        custom_path = os.path.join(base_path, custom_dir)
        return custom_path if os.path.isdir(custom_path) else None

    for doc_dir in DOC_DIRECTORIES:
        doc_path = os.path.join(base_path, doc_dir)
        if os.path.isdir(doc_path):
            logger.info("Found documentation directory: %s", doc_path)
            return doc_path

    logger.info("No standard documentation directory found")
    return None

def process_readme(base_path: str) -> Optional[str]:
    """
    Process the root README.md file.

    Args:
        base_path (str): Base directory path containing the README

    Returns:
        Optional[str]: Content of README.md if found, None otherwise
    """
    readme_path = os.path.join(base_path, "README.md")
    if os.path.isfile(readme_path):
        logger.info("Found README.md file")
        return read_file_content(readme_path)

    logger.info("No README.md file found")
    return None

def generate_docmap_content(
    directory_path: str,
    gitignore_spec: pathspec.PathSpec,
    include_ignored: bool = False,
    source: str = "",
    base_name: str = "",
    doc_dir: Optional[str] = None
) -> str:
    """
    Generate documentation mapping markdown content.

    Args:
        directory_path (str): Base directory path
        gitignore_spec (pathspec.PathSpec): Gitignore specifications
        include_ignored (bool, optional): Whether to include ignored files. Defaults to False.
        source (str, optional): Source information string. Defaults to "".
        base_name (str, optional): Base name for the documentation. Defaults to "".
        doc_dir (Optional[str], optional): Custom documentation directory. Defaults to None.

    Returns:
        str: Generated markdown content for documentation mapping
    """
    md_content = [f"# {base_name} Documentation", ""]
    md_content.append(f"> DocMap Source: {source}\n")
    md_content.append(
        "This markdown document provides a comprehensive overview of the documentation "
        "files and structure. It aims to give viewers (human or AI) a complete view "
        "of the project's documentation in a single file for easy analysis.\n"
    )

    # Process README first
    readme_content = process_readme(directory_path)
    if readme_content:
        md_content.extend([
            "## Project README\n",
            "The following section contains the main project README content:\n",
            "````markdown",
            readme_content,
            "````\n"
        ])

    # Find and process documentation directory
    doc_path = find_documentation_directory(directory_path, doc_dir)
    if doc_path:
        relative_doc_path = os.path.relpath(doc_path, directory_path)
        md_content.extend([
            f"## Documentation Directory: {relative_doc_path}\n",
            "### Directory Structure\n",
            "```tree"
        ])

        tree_content = generate_file_tree(doc_path, gitignore_spec, include_ignored)
        md_content.extend([tree_content, "```\n"])

        # Collect and process documentation files
        file_paths = collect_file_paths(doc_path, gitignore_spec, include_ignored)
        if file_paths:
            md_content.append("### Documentation Contents\n")
            for path in file_paths:
                full_path = os.path.join(doc_path, path)
                content = read_file_content(full_path)
                is_markdown = path.endswith('.md')
                md_content.extend([
                    f"#### {path}\n",
                    "````markdown" if is_markdown else "```",
                    content,
                    "````\n" if is_markdown else "```\n"
                ])

    # If neither README nor doc directory found, include a note
    if not readme_content and not doc_path:
        md_content.append(
            "> Note: No README.md or standard documentation directory found in this repository.\n"
        )

    md_content.append(
        "> This concludes the documentation mapping. Please review thoroughly for a "
        "comprehensive understanding of the project's documentation.\n"
    )

    return "\n".join(md_content)
