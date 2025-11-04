"""Codemap document assembly for CodeMapper."""

import os

from ..readers.detect_types import determine_code_fence
from ..readers.read_files import read_file_content
from ..readers.scan_paths import collect_file_paths
from ..types import CodeMapConfig
from .build_markdown import generate_file_tree, generate_toc


def generate_markdown_document(config: CodeMapConfig) -> str:
    """
    Generate a markdown document from the directory structure.

    Args:
        config (CodeMapConfig): Configuration object containing all parameters

    Returns:
        str: Generated markdown content for code mapping
    """
    md_content = f"# {config.base_name}\n\n"
    md_content += f"> CodeMap Source: {config.source}\n\n"
    md_content += (
        "This markdown document provides a comprehensive overview of the "
        "directory structure and file contents. It aims to give viewers "
        "(human or AI) a complete view of the codebase in a single file "
        "for easy analysis.\n\n"
    )
    md_content += "## Document Table of Contents\n\n"
    md_content += (
        "The table of contents below is for navigational convenience and "
        "reflects this document's structure, not the actual file structure "
        "of the repository.\n\n"
    )

    file_paths = collect_file_paths(
        config.directory_path, config.gitignore_spec, config.include_ignored, config.exclude_dirs
    )

    # Generate TOC
    toc = generate_toc(file_paths, config.base_name)
    md_content += toc + "\n\n"

    md_content += "## Repo File Tree\n\n"
    md_content += (
        "This file tree represents the actual structure of the repository. "
        "It's crucial for understanding the organization of the codebase.\n\n"
    )
    md_content += "```tree\n"
    md_content += generate_file_tree(
        config.directory_path, config.gitignore_spec, config.include_ignored, config.exclude_dirs
    )
    md_content += "\n```\n\n"

    md_content += "## Repo File Contents\n\n"
    md_content += (
        "The following sections present the content of each file in the repository. "
        "Large and binary files are acknowledged but their contents are not displayed.\n\n"
    )

    # Generate code blocks for each file
    for i, path in enumerate(file_paths):
        md_content += f"### `{path}`\n\n"
        full_path = os.path.join(config.directory_path, path)

        code_fence_lang = determine_code_fence(path)
        # Update to include all doc types
        fence = "````" if path.endswith((".md", ".mdx", ".rst", ".adoc")) else "```"
        md_content += f"{fence}{code_fence_lang}\n"
        file_content = read_file_content(full_path)
        md_content += file_content + "\n"
        md_content += f"{fence}\n"

        if i < len(file_paths) - 1:
            md_content += "\n"
        else:
            md_content += (
                "\n> This concludes the repository's file contents. "
                "Please review thoroughly for a comprehensive "
                "understanding of the codebase.\n"
            )

    return md_content
