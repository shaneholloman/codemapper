"""
Code Mapper

Version: 2.5.0
Date: 2024-09-10
Author: Shane Holloman

This python script generates a Markdown Artifact that provides a comprehensive overview of the directory structure and file contents.
It aims to give viewers (human or AI) a complete single page overview of the entire codebase in a single file to bootstrap easy analysis and informed iteration

Key features:
• Generates a hierarchical table of contents based on heading levels
• Creates an accurate file tree representation of the directory structure
• Produces code blocks for each file's contents
• Respects .gitignore (rhymes with bit dot-git-ignore) ignore rules when processing files and directories
• Excludes .git directories and archive files by default
• Supports various file types with appropriate code fence highlighting
• Handles file encoding detection for accurate content reading
• Provides an option to include files normally ignored by .gitignore

Usage:
    python directory_markdown_generator.py <path_to_directory> [--include-ignored]

Output:
    Creates a markdown file named '<directory_name>_structure.md' in the current directory

Requirements:
    • Python 3.6+ (for f-strings and type hinting)
    • pathspec library (for handling .gitignore rules)
    • chardet library (for file encoding detection)

Key components:
    • load_gitignore_specs: Loads .gitignore rules from the given directory
    • collect_file_paths: Gathers file paths while respecting .gitignore rules
    • generate_toc: Creates a table of contents for the markdown document
    • generate_file_tree: Produces an accurate file tree representation
    • read_file_content: Reads file content with encoding detection
    • generate_markdown_document: Orchestrates the creation of the full markdown document

Note: This script is designed to provide a comprehensive overview of a codebase,
      making it easier for developers, AI systems, or other analysts to quickly
      understand the structure and contents of a project.
"""

import os
import sys
import argparse
from typing import Dict, List
import pathspec
import chardet

# Constants
ARCHIVE_EXTENSIONS = {
    ".zip",
    ".tar",
    ".gz",
    ".rar",
    ".7z",
    ".bz2",
    ".xz",
    ".tgz",
    ".tbz2",
}

CODE_FENCE_MAP: Dict[str, str] = {
    ".bat": "batch",
    ".c": "c",
    ".cfg": "ini",
    ".conf": "ini",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".css": "css",
    ".csv": "csv",
    ".dart": "dart",
    ".dockerfile": "dockerfile",
    ".go": "go",
    ".groovy": "groovy",
    ".h": "cpp",
    ".hpp": "cpp",
    ".html": "html",
    ".ini": "ini",
    ".j2": "jinja2",
    ".java": "java",
    ".js": "javascript",
    ".json": "json",
    ".jsx": "jsx",
    ".kt": "kotlin",
    ".lua": "lua",
    ".log": "log",
    ".md": "markdown",
    ".php": "php",
    ".pl": "perl",
    ".ps1": "powershell",
    ".py": "python",
    ".r": "r",
    ".rb": "ruby",
    ".rs": "rust",
    ".scala": "scala",
    ".sh": "bash",
    ".sql": "sql",
    ".swift": "swift",
    ".tf": "hcl",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".txt": "text",
    ".vue": "vue",
    ".xml": "xml",
    ".yaml": "yml",
    ".yml": "yml",
    ".gitignore": "ini",
    "requirements.txt": "ini",
    "requirements.yml": "yml",
    "Dockerfile": "dockerfile",
    "Makefile": "makefile",
    "": "txt",  # Default fallback
}


def should_exclude_directory(dir_name: str, include_ignored: bool = False) -> bool:
    """
    Determine if a directory should be excluded from processing.

    Args:
        dir_name (str): Name of the directory to check.
        include_ignored (bool): If True, only excludes .git directory.
                                If False, also excludes .gitignore.

    Returns:
        bool: True if the directory should be excluded, False otherwise.
    """
    if include_ignored:
        return dir_name == ".git"
    else:
        return dir_name in {".git", ".gitignore"}


def determine_code_fence(file_path: str) -> str:
    """Determine the appropriate code fence language based on the file path."""
    _, ext = os.path.splitext(file_path)
    file_name = os.path.basename(file_path)

    # Check for specific file names first
    if file_name in CODE_FENCE_MAP:
        return CODE_FENCE_MAP[file_name]

    # Then check for extensions
    return CODE_FENCE_MAP.get(ext.lower(), "txt")


def load_gitignore_specs(base_path: str) -> pathspec.PathSpec:
    """Load .gitignore specifications from the given base path."""
    gitignore_path = os.path.join(base_path, ".gitignore")
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as file:
            return pathspec.PathSpec.from_lines("gitwildmatch", file)
    return pathspec.PathSpec.from_lines("gitwildmatch", [])


def collect_file_paths(
    directory_path: str,
    gitignore_spec: pathspec.PathSpec,
    include_ignored: bool = False,
) -> List[str]:
    """Collect file paths, respecting .gitignore rules unless include_ignored is True."""
    file_paths = []

    for root, dirs, files in os.walk(directory_path):
        dirs[:] = [
            d
            for d in dirs
            if not should_exclude_directory(d, include_ignored)
            and (
                include_ignored or not gitignore_spec.match_file(os.path.join(root, d))
            )
        ]

        for filename in files:
            _, ext = os.path.splitext(filename)
            if ext.lower() in ARCHIVE_EXTENSIONS:
                continue
            file_path = os.path.join(root, filename)
            if include_ignored or not gitignore_spec.match_file(file_path):
                rel_path = os.path.relpath(file_path, start=directory_path)
                file_paths.append(rel_path)

    return file_paths


def generate_toc(file_paths: List[str], base_name: str) -> str:
    """Generate a table of contents based on heading levels."""
    toc = ["<!-- TOC -->", ""]
    toc.append(f"- [{base_name}](#{base_name.lower().replace(' ', '-')})")
    toc.append("  - [Document Table of Contents](#document-table-of-contents)")
    toc.append("  - [Repo File Tree](#repo-file-tree)")
    toc.append("  - [Repo File Contents](#repo-file-contents)")

    # Sort file paths, placing README.md first and .gitignore second
    sorted_paths = sorted(
        file_paths, key=lambda x: (x != "README.md", x != ".gitignore", x.lower())
    )

    for path in sorted_paths:
        link = path.lower().replace(".", "").replace("/", "")
        toc.append(f"    - [{path}](#{link})")

    toc.append("")
    toc.append("<!-- /TOC -->")

    return "\n".join(toc)


def generate_file_tree(
    directory_path: str,
    gitignore_spec: pathspec.PathSpec,
    include_ignored: bool = False,
) -> str:
    """
    Generate an accurate file tree representation of the given directory.

    This function creates a hierarchical tree structure of files and directories,
    respecting .gitignore rules (unless include_ignored is True) and excluding
    specified directories. It accurately counts and distinguishes between files
    and directories.

    Args:
        directory_path (str): The path to the directory to generate the tree for.
        gitignore_spec (pathspec.PathSpec): The gitignore specifications to apply.
        include_ignored (bool): If True, include files normally ignored by .gitignore.

    Returns:
        str: A string representation of the file tree, including a count of
              directories and files at the end.

    Note:
        - Directories are represented with a trailing slash (/) in the tree.
        - The tree includes proper indentation and branch symbols (├── and └──).
        - The root directory is represented by a single dot (.).
        - Files and directories are sorted alphabetically at each level.
        - The function respects .gitignore rules when include_ignored is False.
    """

    def walk_directory(dir_path: str, prefix: str = "") -> List[str]:
        files = []
        contents = sorted(os.listdir(dir_path))
        dirs = [
            d
            for d in contents
            if os.path.isdir(os.path.join(dir_path, d))
            and not should_exclude_directory(d, include_ignored)
        ]
        regular_files = [
            f for f in contents if os.path.isfile(os.path.join(dir_path, f))
        ]

        for idx, name in enumerate(dirs + regular_files):
            full_path = os.path.join(dir_path, name)
            rel_path = os.path.relpath(full_path, directory_path)

            if not include_ignored and gitignore_spec.match_file(rel_path):
                continue

            is_last = idx == len(dirs + regular_files) - 1
            current_prefix = "└── " if is_last else "├── "

            if os.path.isdir(full_path):
                files.append(
                    f"{prefix}{current_prefix}{name}/"
                )  # Add trailing slash for directories
                extension = "    " if is_last else "│   "
                files.extend(walk_directory(full_path, prefix + extension))
            else:
                files.append(f"{prefix}{current_prefix}{name}")

        return files

    tree = [".", *walk_directory(directory_path)]

    dir_count = sum(1 for line in tree if line.endswith("/"))
    file_count = len(tree) - dir_count - 1  # -1 for the root '.'

    tree.append(f"\n{dir_count} directories, {file_count} files")
    return "\n".join(tree)


def read_file_content(file_path: str) -> str:
    """Read file content with encoding detection and fallback mechanisms."""
    try:
        with open(file_path, "rb") as file:
            raw_data = file.read()
        detect_result = chardet.detect(raw_data)
        detected_encoding = detect_result["encoding"] if detect_result else None

        encoding_to_use = detected_encoding or "utf-8"
        with open(file_path, "r", encoding=encoding_to_use) as file:
            return file.read().rstrip()
    except UnicodeDecodeError:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read().rstrip()
        except UnicodeDecodeError:
            try:
                with open(file_path, "r", encoding="latin-1") as file:
                    return file.read().rstrip()
            except Exception as e:
                return f"Error reading file: {str(e)}"
    except Exception as e:
        return f"Error reading file: {str(e)}"


def generate_markdown_document(
    directory_path: str,
    gitignore_spec: pathspec.PathSpec,
    include_ignored: bool = False,
) -> str:
    """Generate a markdown document from the directory structure."""
    base_name = os.path.basename(directory_path)
    md_content = f"# {base_name}\n\n"
    md_content += "This markdown document provides a comprehensive overview of the directory structure and file contents. It aims to give viewers (human or AI) a complete view of the codebase in a single file for easy analysis.\n\n"
    md_content += "## Document Table of Contents\n\n"
    md_content += "The table of contents below is for navigational convenience and reflects this document's structure, not the actual file structure of the repository.\n\n"

    file_paths = collect_file_paths(directory_path, gitignore_spec, include_ignored)

    # Generate TOC
    toc = generate_toc(file_paths, base_name)
    md_content += toc + "\n\n"

    md_content += "## Repo File Tree\n\n"
    md_content += "This file tree represents the actual structure of the repository. It's crucial for understanding the organization of the codebase.\n\n"
    md_content += "```tree\n"
    md_content += generate_file_tree(directory_path, gitignore_spec, include_ignored)
    md_content += "\n```\n\n"

    md_content += "## Repo File Contents\n\n"
    md_content += (
        "The following sections present the content of each file in the repository.\n\n"
    )

    # Generate code blocks for each file
    for i, path in enumerate(file_paths):
        md_content += f"### {path}\n\n"
        code_fence_lang = determine_code_fence(path)
        fence = "````" if path.endswith(".md") else "```"
        md_content += f"{fence}{code_fence_lang}\n"

        full_path = os.path.join(directory_path, path)
        file_content = read_file_content(full_path)

        # Replace "licence" with "license" in file content
        file_content = file_content.replace("licence", "license").replace(
            "Licence", "License"
        )

        md_content += file_content + "\n"

        # Add appropriate ending based on whether it's the last file
        if i < len(file_paths) - 1:
            md_content += f"{fence}\n\n"
        else:
            md_content += f"{fence}\n\n"
            md_content += "> This concludes the repository's file contents. Please review thoroughly for a comprehensive understanding of the codebase.\n"

    return md_content


def main():
    """Main function to orchestrate the markdown document generation process."""
    parser = argparse.ArgumentParser(
        description="Generate markdown document from directory structure."
    )
    parser.add_argument("directory_path", help="Path to the directory to process")
    parser.add_argument(
        "--include-ignored",
        action="store_true",
        help="Include files normally ignored by .gitignore",
    )
    args = parser.parse_args()

    if not os.path.isdir(args.directory_path):
        print(
            f"Error: '{args.directory_path}' is not a directory. Please check the path."
        )
        sys.exit(1)

    gitignore_spec = load_gitignore_specs(args.directory_path)
    markdown_content = generate_markdown_document(
        args.directory_path, gitignore_spec, args.include_ignored
    )

    markdown_filename = f"{os.path.basename(args.directory_path)}_structure.md"
    with open(markdown_filename, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file '{markdown_filename}' has been created.")


if __name__ == "__main__":
    main()
