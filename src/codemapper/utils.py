"""Utility functions for CodeMapper."""

import os
import re
import subprocess
import mimetypes
from typing import List, Tuple, Optional  # Add Optional for optional parameters

import chardet
import pathspec

from .config import CODEMAP_SUFFIX  # At top level import

from .config import (
    ARCHIVE_EXTENSIONS,
    CODE_FENCE_MAP,
    LARGE_FILE_EXTENSIONS,
)


# Move all functions from codemapper.py
def should_exclude_directory(
    dir_name: str, include_ignored: bool = False, exclude_dirs: Optional[List[str]] = None
) -> bool:
    """
    Determine if a directory should be excluded from processing.

    Args:
        dir_name: Name of the directory to check
        include_ignored: Whether to include git-ignored files
        exclude_dirs: List of additional directories to exclude
    """
    # Default exclusions
    default_exclusions = {".git", ".venv", ".conda", "node_modules"}

    if include_ignored:
        return dir_name in default_exclusions

    # Combine default exclusions with user-specified ones
    exclusions = default_exclusions | {".gitignore"}
    if exclude_dirs:
        exclusions.update(exclude_dirs)

    return dir_name in exclusions


def determine_code_fence(file_path: str) -> str:
    """Determine the appropriate code fence language based on the file path."""
    _, ext = os.path.splitext(file_path)
    file_name = os.path.basename(file_path)

    # Check for specific file names first
    if file_name in CODE_FENCE_MAP:  # Removed unnecessary parentheses
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
    exclude_dirs: Optional[List[str]] = None,
) -> List[str]:
    """Collect file paths, respecting .gitignore rules unless include_ignored is True."""
    file_paths = []

    for root, dirs, files in os.walk(directory_path):
        dirs[:] = [
            d
            for d in dirs
            if not should_exclude_directory(d, include_ignored, exclude_dirs)
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
    exclude_dirs: Optional[List[str]] = None,
) -> str:
    """Generate an accurate file tree representation of the given directory."""

    def walk_directory(dir_path: str, prefix: str = "") -> List[str]:
        files = []
        contents = sorted(os.listdir(dir_path))
        dirs = [
            d
            for d in contents
            if os.path.isdir(os.path.join(dir_path, d))
            and not should_exclude_directory(d, include_ignored, exclude_dirs)
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
    """Determine if a file is considered a large binary file."""
    _, ext = os.path.splitext(file_path.lower())
    file_name = os.path.basename(file_path)

    # Check if it's in LARGE_FILE_EXTENSIONS
    if ext in LARGE_FILE_EXTENSIONS:
        return True

    # Check if it's in CODE_FENCE_MAP
    if ext in CODE_FENCE_MAP or file_name in CODE_FENCE_MAP:
        return False

    # Fallback to MIME type check
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        # List of MIME types that are considered text-based
        text_mime_types = [
            "text/",
            "application/json",
            "application/javascript",
            "application/xml",
            "application/x-httpd-php",
            "application/x-sh",
            "application/x-csh",
        ]
        return not any(mime_type.startswith(text_type) for text_type in text_mime_types)

    # If MIME type couldn't be determined, assume it's not a large file
    return False


def get_file_info(file_path: str) -> str:
    """Get information about a file without reading its contents."""
    size = os.path.getsize(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)
    return f"File Type: {mime_type or 'Unknown'}, Size: {size} bytes"


def read_file_content(file_path: str) -> str:
    """Read file content with encoding detection and large file handling."""
    if is_large_file(file_path):
        return f"[Large or binary file detected. {get_file_info(file_path)}]"

    try:
        with open(file_path, "rb") as file:
            raw_data = file.read(1024)  # Read only the first 1024 bytes for detection
        detect_result = chardet.detect(raw_data)
        detected_encoding = detect_result["encoding"] if detect_result else None

        encodings_to_try = [detected_encoding, "utf-8", "latin-1"]

        for encoding in encodings_to_try:
            if encoding:
                try:
                    with open(file_path, "r", encoding=encoding) as file:
                        return file.read().rstrip()
                except UnicodeDecodeError:
                    continue

        return (
            f"[Error: Unable to decode file with detected encoding "
            f"({detected_encoding}), UTF-8, or Latin-1]"
        )
    except IOError as e:
        return f"[Error reading file: {str(e)}]"


def capture_source(input_path: str) -> str:
    """Capture the source of the pulled repo."""
    if os.path.isdir(input_path):
        return f"Local directory: `{os.path.abspath(input_path)}`"
    return f"GitHub repository: <{input_path}>"


def generate_markdown_document(
    directory_path: str,
    gitignore_spec: pathspec.PathSpec,
    include_ignored: bool = False,
    source: str = "",
    base_name: str = "",
    exclude_dirs: Optional[List[str]] = None,
) -> str:
    """Generate a markdown document from the directory structure."""
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

    file_paths = collect_file_paths(directory_path, gitignore_spec, include_ignored, exclude_dirs)

    # Generate TOC
    toc = generate_toc(file_paths, base_name)
    md_content += toc + "\n\n"

    md_content += "## Repo File Tree\n\n"
    md_content += (
        "This file tree represents the actual structure of the repository. "
        "It's crucial for understanding the organization of the codebase.\n\n"
    )
    md_content += "```tree\n"
    md_content += generate_file_tree(directory_path, gitignore_spec, include_ignored, exclude_dirs)
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


def detect_input_type(input_path: str) -> Tuple[str, str]:
    """Detect whether the input is a local directory or a GitHub URL."""
    # Check if it's a valid local directory
    if os.path.isdir(input_path):
        return "local", input_path

    # Check if it's a valid GitHub URL
    github_pattern = r"^https?://github\.com/[\w-]+/[\w.-]+(?:\.git)?$"
    if re.match(github_pattern, input_path):
        return "github", input_path

    raise ValueError("Invalid input. Please provide a valid local directory path or GitHub URL.")


def clone_github_repo(repo_url: str) -> str:
    """Clone a GitHub repository into a '_github' directory."""
    github_dir = os.path.join(".", "_github")
    os.makedirs(github_dir, exist_ok=True)

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(github_dir, repo_name)

    if os.path.exists(repo_path):
        print(f"Repository '{repo_name}' already exists. Updating...")
        subprocess.run(["git", "-C", repo_path, "pull", "--depth", "1"], check=True)
        return repo_path

    print(f"Cloning repository '{repo_name}'...")
    subprocess.run(["git", "clone", "--depth", "1", repo_url, repo_path], check=True)
    return repo_path


def manage_output_directory(base_name: str, input_path: str, suffix: str = CODEMAP_SUFFIX) -> str:
    """
    Manage the output directory for the markdown output.

    Args:
        base_name (str): Base name for the output file
        input_path (str): Original input path (used for relative path handling)
        suffix (str): Suffix for the output file. Defaults to CODEMAP_SUFFIX.

    Returns:
        str: Path to the output file
    """
    output_dir = os.path.join(".", "_codemaps")
    os.makedirs(output_dir, exist_ok=True)

    # If input_path is a relative path, use its basename
    if not os.path.isabs(input_path) and not input_path.startswith(("http://", "https://")):
        base_name = os.path.basename(os.path.abspath(input_path))

    file_name = f"{base_name}{suffix}"
    return os.path.join(output_dir, file_name)
