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

# Add dataclasses import for our new DocMapConfig
from dataclasses import dataclass
from typing import Optional, List

# Need pathspec for type hinting
import pathspec

from .config import DOC_DIRECTORIES
from .utils import (
    read_file_content,
    generate_file_tree,
    collect_file_paths,
)

logger = logging.getLogger(__name__)

# Documentation type mapping
doc_types = {
    ".md": "markdown",
    ".mdx": "markdown",
    ".adoc": "asciidoc",
    ".rst": "restructuredtext",
}


# This is our new configuration class
# @dataclass is a decorator that automatically adds special methods to the class
# This makes it easier to create and use classes that are mainly used to hold data
@dataclass
class DocMapConfig:
    """Configuration class for document mapping generation.

    This class holds all the parameters needed for generating a documentation map.
    Using a class like this helps us organize related data and makes the code
    easier to maintain.

    Attributes:
        directory_path (str): The path to the directory being mapped
        gitignore_spec (pathspec.PathSpec): Gitignore specifications to follow
        include_ignored (bool): Whether to include ignored files, defaults to False
        source (str): Source information string, defaults to empty string
        base_name (str): Base name for documentation, defaults to empty string
        doc_dir (Optional[str]): Custom documentation directory, defaults to None
        exclude_dirs (Optional[List[str]]): List of directories to exclude, defaults to None
    """

    directory_path: str
    gitignore_spec: pathspec.PathSpec
    include_ignored: bool = False
    source: str = ""
    base_name: str = ""
    doc_dir: Optional[str] = None
    exclude_dirs: Optional[List[str]] = None


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


# Updated to use the new DocMapConfig class
def generate_docmap_content(config: DocMapConfig) -> str:
    """
    Generate documentation mapping markdown content.

    Instead of taking multiple parameters, this function now takes a single
    DocMapConfig object that contains all the necessary configuration values.
    This makes the function cleaner and easier to maintain.

    Args:
        config (DocMapConfig): Configuration object containing all parameters

    Returns:
        str: Generated markdown content for documentation mapping
    """
    # Start building the markdown content
    md_content = [f"# {config.base_name} Documentation", ""]
    md_content.append(f"> DocMap Source: {config.source}\n")
    md_content.append(
        "This markdown document provides a comprehensive overview of the documentation "
        "files and structure. It aims to give viewers (human or AI) a complete view "
        "of the project's documentation in a single file for easy analysis.\n"
    )

    # Process README first
    readme_content = process_readme(config.directory_path)
    if readme_content:
        md_content.extend(
            [
                "## Project README\n",
                "The following section contains the main project README content:\n",
                "````markdown",
                readme_content,
                "````\n",
            ]
        )

    # Find and process documentation directory
    doc_path = find_documentation_directory(config.directory_path, config.doc_dir)
    if doc_path:
        relative_doc_path = os.path.relpath(doc_path, config.directory_path)
        md_content.extend(
            [
                f"## Documentation Directory: {relative_doc_path}\n",
                "### Directory Structure\n",
                "```tree",
            ]
        )

        tree_content = generate_file_tree(
            doc_path, config.gitignore_spec, config.include_ignored, config.exclude_dirs
        )
        md_content.extend([tree_content, "```\n"])

        # Then in the function:
        def get_fence_type(file_path: str) -> str:
            """Get the fence type based on file extension."""
            ext = os.path.splitext(file_path)[1].lower()
            return doc_types.get(ext, "")

        # Process documentation files
        file_paths = collect_file_paths(
            doc_path, config.gitignore_spec, config.include_ignored, config.exclude_dirs
        )
        if file_paths:
            md_content.append("### Documentation Contents\n")
            for path in file_paths:
                full_path = os.path.join(doc_path, path)
                content = read_file_content(full_path)
                fence_type = get_fence_type(path)
                md_content.extend(
                    [
                        f"#### {path}\n",
                        f"````{fence_type}" if fence_type else "```",
                        content,
                        "````\n" if fence_type else "```\n",
                    ]
                )

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
