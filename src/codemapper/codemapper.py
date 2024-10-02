"""
CodeMapper: Comprehensive Codebase Visualization for Humans and AI

Date: 2024 Oct 02
Author: Shane Holloman with AI Assistance

CodeMapper is a powerful Python tool designed to generate detailed Markdown
representations of entire codebases. It serves as an efficient bridge between
human developers and AI systems by providing a clear, structured view of
project architectures and their complete contents.

This tool excels at processing both local directories and GitHub repositories,
creating a single, navigable document that captures the full structure and
content of a project. It's a valuable asset for rapid codebase comprehension,
whether you're a developer onboarding to a new project or an AI system
analyzing code structure.

Key Features:
• Comprehensive Output: Generates content optimized for both human readers and AI analysis
• Intelligent Content Processing: Respects .gitignore rules and handles various file types
• Complete Structure Representation:
  - Creates an accurate, hierarchical file tree
  - Generates a detailed table of contents for easy navigation
• Code-Aware Analysis:
  - Applies appropriate syntax highlighting for different file types
  - Efficiently handles large or binary files without bloating the output
• Flexible Input Handling: Works with local directories and GitHub repositories
• Encoding Detection: Ensures accurate content reading across various file encodings
• Customizable Ignore Rules: Option to include files normally ignored by .gitignore
• Organized Output Management: Stores generated documents in a '_codemaps' directory

Usage:
    python codemapper.py <path_to_directory_or_github_url> [--include-ignored]

Output:
    Creates a markdown file named '<directory_name>_codemap.md' in the '_codemaps' directory

Requirements:
    • Python 3.6+ (for f-strings and type hinting)
    • pathspec library (for handling .gitignore rules)
    • chardet library (for file encoding detection)

CodeMapper aims to enhance code comprehension and analysis by providing a
complete and structured view of any codebase. It serves as an effective tool
for both human developers and AI systems to quickly grasp the full structure
and content of software projects.
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
    ".tar.gz",
    ".tar.bz2",
    # implement wildcard support for archive files, example: *.tar.*
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
    ".hbs": "handlebars",
    ".hcl": "hcl",
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
    ".pkl": "pickle",
    ".proto": "protobuf",
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
    # Database files
    ".db",
    ".sqlite",
    ".sqlite3",
    ".dbf",
    ".mdb",
    ".accdb",
    ".sql",
    ".psql",
    ".dmp",
    # Image files
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".ico",
    ".svg",
    ".webp",
    ".eps",
    ".raw",
    ".cr2",
    ".nef",
    # Video files
    ".mp4",
    ".avi",
    ".mov",
    ".wmv",
    ".flv",
    ".mkv",
    ".webm",
    ".vob",
    ".ogv",
    # Audio files
    ".mp3",
    ".wav",
    ".ogg",
    ".flac",
    # Document files
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".odt",
    # Archive files
    ".zip",
    ".tar",
    ".gz",
    ".rar",
    ".7z",
    ".bz2",
    ".xz",
    ".tgz",
    ".tbz2",
    # Executable files
    ".exe",
    ".msi",
    ".apk",
    ".app",
    ".dmg",
    ".iso",
    ".jar",
    ".deb",
    ".rpm",
    # Font files
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
    ".eot",
    ".fon",
    # Binary files
    ".bin",
    ".dll",
    ".so",
    ".dylib",
    ".dat",
    ".sav",
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

    This function reads the .gitignore file in the specified directory and creates
    a PathSpec object that can be used to match files against the gitignore rules.

    Args:
        base_path (str): The base directory path to search for .gitignore.

    Returns:
        pathspec.PathSpec: The gitignore specifications as a PathSpec object.
        If no .gitignore file is found, returns an empty PathSpec.
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

    This function walks through the directory structure, collecting file paths while
    applying gitignore rules. It excludes certain directories by default and can
    optionally include files that would normally be ignored by .gitignore.

    Args:
        directory_path (str): The path to the directory to process.
        gitignore_spec (pathspec.PathSpec): The gitignore specifications to apply.
        include_ignored (bool): Whether to include files ignored by .gitignore.

    Returns:
        List[str]: A list of file paths relative to the directory_path, normalized
        to use forward slashes.
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

    This function creates a hierarchical table of contents for the Markdown document,
    including entries for the base directory or repository, document sections, and
    all files in the project.

    Args:
        file_paths (List[str]): List of file paths to include in the TOC.
        base_name (str): The name of the base directory or repository.

    Returns:
        str: A formatted table of contents as a string, with proper Markdown syntax
        for nested lists and links.
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

    This function checks the file extension against a predefined list of large file
    extensions, known code file types, and falls back to MIME type checking if necessary.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is considered large or binary, False otherwise.
    """
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
    """
    Get information about a file without reading its contents.

    This function retrieves basic metadata about a file, including its size and
    MIME type, without actually reading the file contents.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: A string containing file information, including file type and size in bytes.
    """
    size = os.path.getsize(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)
    return f"File Type: {mime_type or 'Unknown'}, Size: {size} bytes"


def read_file_content(file_path: str) -> str:
    """
    Read file content with encoding detection and large file handling.

    This function attempts to read the content of a file, detecting its encoding
    and handling large or binary files appropriately. It uses multiple encoding
    attempts to ensure proper reading of the file content.

    Args:
        file_path (str): Path to the file to read.

    Returns:
        str: The content of the file if successfully read, or information about
        the file if it's large or binary. In case of errors, returns an error message.
    """
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
    base_name: str = "",
) -> str:
    """
    Generate a markdown document from the directory structure.

    This function creates a comprehensive Markdown document that includes a table
    of contents, file tree representation, and the contents of each file in the
    specified directory or repository. It respects .gitignore rules and handles
    large or binary files appropriately.

    Args:
        directory_path (str): The path to the directory to process.
        gitignore_spec (pathspec.PathSpec): The gitignore specifications to apply.
        include_ignored (bool): Whether to include files ignored by .gitignore.
        source (str): The source of the repo (local directory or GitHub URL).
        base_name (str): The base name to use for the title of the markdown document.

    Returns:
        str: The generated markdown content as a string, including all sections
        and file contents.
    """
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

    This function clones a GitHub repository to a local directory. If the repository
    already exists locally, it updates the existing clone instead of creating a new one.

    Args:
        repo_url (str): The URL of the GitHub repository to clone.

    Returns:
        str: The path to the cloned repository.

    Raises:
        subprocess.CalledProcessError: If the git clone or pull command fails.
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


def manage_output_directory(base_name: str, input_path: str) -> str:
    """
    Manage the output directory for the markdown output.

    This function creates a '_codemaps' directory if it doesn't exist and determines
    the appropriate output file name based on the input path or repository name.

    Args:
        base_name (str): The base name for the output file (usually the repository
                         or directory name).
        input_path (str): The original input path provided by the user.

    Returns:
        str: The full path for the output markdown file.
    """
    output_dir = os.path.join(".", "_codemaps")
    os.makedirs(output_dir, exist_ok=True)

    # If input_path is a relative path, use its basename
    if not os.path.isabs(input_path) and not input_path.startswith(("http://", "https://")):
        base_name = os.path.basename(os.path.abspath(input_path))

    file_name = f"{base_name}_codemap.md"
    return os.path.join(output_dir, file_name)


def main():
    """
    Main function to orchestrate the markdown document generation process.

    This function parses command-line arguments, detects the input type (local
    directory or GitHub repository), generates the markdown document, and saves
    it to the appropriate output file. It handles various error conditions and
    provides user feedback.
    """
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

    # Determine the base_name for the title
    if not os.path.isabs(args.input_path) and not args.input_path.startswith(
        ("http://", "https://")
    ):
        base_name = os.path.basename(os.path.abspath(args.input_path))
    else:
        base_name = os.path.basename(directory_path)

    gitignore_spec = load_gitignore_specs(directory_path)
    markdown_content = generate_markdown_document(
        directory_path, gitignore_spec, args.include_ignored, source, base_name
    )

    output_file_path = manage_output_directory(base_name, args.input_path)

    with open(output_file_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file has been created: {output_file_path}")


if __name__ == "__main__":
    main()
