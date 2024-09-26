"""
CodeMapper

Date: 2024-09-23
Author: AI Assistant (based on original by Shane Holloman)

This Python script generates a Markdown artifact that provides
a comprehensive overview of a directory structure
and file contents. It can process local directories or clone and analyze GitHub repositories.

Key features:
• Generates a hierarchical table of contents based on heading levels
• Creates an accurate file tree representation of the directory structure
• Produces code blocks for each file's contents
• Respects .gitignore rules when processing files and directories
• Excludes .git directories by default
• Supports various file types with appropriate code fence highlighting
• Handles file encoding detection for accurate content reading
• Provides an option to include files normally ignored by .gitignore
• Can clone and analyze GitHub repositories
• Saves output in a '_codemaps' directory
• Acknowledges large and binary files without printing their contents

Usage:
    python codemapper.py <path_to_directory_or_github_url> [--include-ignored]

Output:
    Creates a markdown file named '<directory_name>_structure.md' in the '_codemaps' directory

Requirements:
    • Python 3.6+ (for f-strings and type hinting)
    • pathspec library (for handling .gitignore rules)
    • chardet library (for file encoding detection)

Note: This script is designed to provide a comprehensive overview of a codebase,
      making it easier for developers, AI systems, or other analysts to quickly
      understand the structure and contents of a project.
"""

import argparse
import mimetypes
import os
import re
import subprocess
import sys
from typing import Dict, List, Tuple

import chardet
import pathspec

from . import __version__

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

LARGE_FILE_EXTENSIONS = {
    ".db",
    ".sqlite",
    ".sqlite3",  # Database files
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",  # Image files
    ".mp4",
    ".avi",
    ".mov",
    ".wmv",
    ".flv",
    ".mkv",  # Video files
    ".mp3",
    ".wav",
    ".ogg",
    ".flac",  # Audio files
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",  # Document files
    ".zip",
    ".tar",
    ".gz",
    ".rar",
    ".7z",  # Archive files
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
    return dir_name in {".git", ".gitignore"}


def determine_code_fence(file_path: str) -> str:
    """
    Determine the appropriate code fence language based on the file path.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: The code fence language identifier.
    """
    _, ext = os.path.splitext(file_path)
    file_name = os.path.basename(file_path)

    # Check for specific file names first
    if file_name in CODE_FENCE_MAP:
        return CODE_FENCE_MAP[file_name]

    # Then check for extensions
    return CODE_FENCE_MAP.get(ext.lower(), "txt")


def load_gitignore_specs(base_path: str) -> pathspec.PathSpec:
    """
    Load .gitignore specifications from the given base path.

    Args:
        base_path (str): The base directory path to search for .gitignore.

    Returns:
        pathspec.PathSpec: The gitignore specifications.
    """
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
    """
    Collect file paths, respecting .gitignore rules unless include_ignored is True.

    Args:
        directory_path (str): The path to the directory to process.
        gitignore_spec (pathspec.PathSpec): The gitignore specifications.
        include_ignored (bool): Whether to include files ignored by .gitignore.

    Returns:
        List[str]: A list of file paths relative to the directory_path.
    """
    file_paths = []

    for root, dirs, files in os.walk(directory_path):
        dirs[:] = [
            d
            for d in dirs
            if not should_exclude_directory(d, include_ignored)
            and (include_ignored or not gitignore_spec.match_file(os.path.join(root, d)))
        ]

        for filename in files:
            _, ext = os.path.splitext(filename)
            if ext.lower() in ARCHIVE_EXTENSIONS:
                continue
            file_path = os.path.join(root, filename)
            if include_ignored or not gitignore_spec.match_file(file_path):
                rel_path = os.path.relpath(file_path, start=directory_path)
                # Normalize path separators to forward slashes
                normalized_path = rel_path.replace(os.sep, "/")
                file_paths.append(normalized_path)

    return file_paths


def generate_toc(file_paths: List[str], base_name: str) -> str:
    """
    Generate a table of contents based on heading levels.

    Args:
        file_paths (List[str]): List of file paths to include in the TOC.
        base_name (str): The name of the base directory or repository.

    Returns:
        str: A formatted table of contents as a string.
    """
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
        # Normalize path separators to forward slashes
        normalized_path = path.replace(os.sep, "/")

        # Handle __init__.py files specially
        if normalized_path.endswith("__init__.py"):
            link = (
                normalized_path.lower()
                .replace("__init__.py", "init.py")
                .replace(".", "")
                .replace("/", "")
            )
            heading = normalized_path.replace("__init__.py", "init.py")
        else:
            # Create the link by removing dots and slashes, but keep underscores
            link = normalized_path.lower().replace(".", "").replace("/", "")

            # Replace double underscores with a single underscore in the link
            while "__" in link:
                link = link.replace("__", "_")

            # Escape underscores in the heading
            heading = normalized_path.replace("_", "\\_")

        toc.append(f"    - [{heading}](#{link})")

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
        regular_files = [f for f in contents if os.path.isfile(os.path.join(dir_path, f))]

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


def is_large_file(file_path: str) -> bool:
    """
    Determine if a file is considered a large binary file.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is considered large or binary, False otherwise.
    """
    _, ext = os.path.splitext(file_path.lower())
    if ext in LARGE_FILE_EXTENSIONS:
        return True

    mime_type, _ = mimetypes.guess_type(file_path)
    return bool(mime_type) and not mime_type.startswith("text")


def get_file_info(file_path: str) -> str:
    """
    Get information about a file without reading its contents.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: A string containing file information.
    """
    size = os.path.getsize(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)
    return f"File Type: {mime_type or 'Unknown'}, Size: {size} bytes"


def read_file_content(file_path: str) -> str:
    """
    Read file content with encoding detection and large file handling.

    Args:
        file_path (str): Path to the file to read.

    Returns:
        str: The content of the file or information about the file if it's large or binary.
    """
    if is_large_file(file_path):
        return f"[Large or binary file detected. {get_file_info(file_path)}]"

    try:
        with open(file_path, "rb") as file:
            raw_data = file.read(1024)  # Read only the first 1024 bytes for detection
        detect_result = chardet.detect(raw_data)
        detected_encoding = detect_result["encoding"] if detect_result else None

        encoding_to_use = detected_encoding or "utf-8"
        with open(file_path, "r", encoding=encoding_to_use) as file:
            return file.read().rstrip()
    except (IOError, UnicodeDecodeError) as e:
        return f"[Error reading file: {str(e)}]"


def capture_source(input_path: str) -> str:
    """
    Capture the source of the pulled repo, whether it's a local directory or a GitHub URL.

    Args:
        input_path (str): The input path or URL provided by the user.

    Returns:
        str: A string describing the source of the repo, encapsulated appropriately.
    """
    if os.path.isdir(input_path):
        return f"Local directory: `{os.path.abspath(input_path)}`"
    return f"GitHub repository: <{input_path}>"


def generate_markdown_document(
    directory_path: str,
    gitignore_spec: pathspec.PathSpec,
    include_ignored: bool = False,
    source: str = "",
) -> str:
    """
    Generate a markdown document from the directory structure.

    Args:
        directory_path (str): The path to the directory to process.
        gitignore_spec (pathspec.PathSpec): The gitignore specifications to apply.
        include_ignored (bool): Whether to include files ignored by .gitignore.
        source (str): The source of the repo (local directory or GitHub URL).

    Returns:
        str: The generated markdown content as a string.
    """
    base_name = os.path.basename(directory_path)
    md_content = f"# {base_name}\n\n"
    md_content += f"> CodeMap Source: {source}\n\n"
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

    file_paths = collect_file_paths(directory_path, gitignore_spec, include_ignored)

    # Generate TOC
    toc = generate_toc(file_paths, base_name)
    md_content += toc + "\n\n"

    md_content += "## Repo File Tree\n\n"
    md_content += (
        "This file tree represents the actual structure of the repository. "
        "It's crucial for understanding the organization of the codebase.\n\n"
    )
    md_content += "```tree\n"
    md_content += generate_file_tree(directory_path, gitignore_spec, include_ignored)
    md_content += "\n```\n\n"

    md_content += "## Repo File Contents\n\n"
    md_content += (
        "The following sections present the content of each file in the repository. "
        "Large and binary files are acknowledged but their contents are not displayed.\n\n"
    )

    # Generate code blocks for each file
    for i, path in enumerate(file_paths):
        md_content += f"### {path}\n\n"
        full_path = os.path.join(directory_path, path)

        code_fence_lang = determine_code_fence(path)
        fence = "````" if path.endswith(".md") else "```"
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


def detect_input_type(input_path: str) -> Tuple[str, str]:
    """
    Detect whether the input is a local directory or a GitHub URL.

    Args:
        input_path (str): The input provided by the user.

    Returns:
        Tuple[str, str]: A tuple containing input type ('local' or 'github') and the path or URL.

    Raises:
        ValueError: If the input is neither a valid local directory nor a valid GitHub URL.
    """
    # Check if it's a valid local directory
    if os.path.isdir(input_path):
        return "local", input_path

    # Check if it's a valid GitHub URL
    github_pattern = r"^https?://github\.com/[\w-]+/[\w.-]+(?:\.git)?$"
    if re.match(github_pattern, input_path):
        return "github", input_path

    raise ValueError("Invalid input. Please provide a valid local directory path or GitHub URL.")


def clone_github_repo(repo_url: str) -> str:
    """
    Clone a GitHub repository into a '_github' directory.

    Args:
        repo_url (str): The URL of the GitHub repository to clone.

    Returns:
        str: The path to the cloned repository.

    Raises:
        subprocess.CalledProcessError: If the git clone command fails.
        OSError: If there's an issue creating the directory.
    """
    github_dir = os.path.join(".", "_github")
    os.makedirs(github_dir, exist_ok=True)

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(github_dir, repo_name)

    if os.path.exists(repo_path):
        print(f"Repository '{repo_name}' already exists. Updating...")
        subprocess.run(["git", "-C", repo_path, "pull"], check=True)
        return repo_path

    print(f"Cloning repository '{repo_name}'...")
    subprocess.run(["git", "clone", repo_url, repo_path], check=True)
    return repo_path


def manage_output_directory(base_name: str) -> str:
    """
    Manage the output directory for the markdown output.

    Args:
        base_name (str): The base name for the output file
        (usually the repository or directory name).

    Returns:
        str: The full path for the output markdown file.
    """
    output_dir = os.path.join(".", "_codemaps")
    os.makedirs(output_dir, exist_ok=True)

    file_name = f"{base_name}_codemap.md"
    return os.path.join(output_dir, file_name)


def main():
    """Main function to orchestrate the markdown document generation process."""
    parser = argparse.ArgumentParser(
        description=("Generate markdown document from directory structure " "or GitHub repository.")
    )
    parser.add_argument(
        "input_path",
        nargs="?",  # Make input_path optional
        help="Path to the directory to process or GitHub repository URL",
    )
    parser.add_argument(
        "--include-ignored",
        action="store_true",
        help="Include files normally ignored by .gitignore",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"CodeMapper version {__version__}",
        help="Show the version number and exit",
    )
    args = parser.parse_args()

    # If no input_path is provided and --version wasn't used, show help and exit
    if not args.input_path:
        parser.print_help()
        sys.exit(1)

    try:
        input_type, path = detect_input_type(args.input_path)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    source = capture_source(args.input_path)

    if input_type == "github":
        try:
            directory_path = clone_github_repo(path)
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
            sys.exit(1)
        except OSError as e:
            print(f"Error creating directory: {e}")
            sys.exit(1)
    else:
        directory_path = path

    gitignore_spec = load_gitignore_specs(directory_path)
    markdown_content = generate_markdown_document(
        directory_path, gitignore_spec, args.include_ignored, source
    )

    base_name = os.path.basename(directory_path)
    output_file_path = manage_output_directory(base_name)

    with open(output_file_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file has been created: {output_file_path}")


if __name__ == "__main__":
    main()
