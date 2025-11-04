"""Markdown structure generation for CodeMapper."""

import os

import pathspec

from ..config import LOCK_FILES, SYSTEM_FILES
from ..processors.process_dir import should_exclude_directory


def generate_toc(file_paths: list[str], base_name: str) -> str:
    """Generate a table of contents based on heading levels."""
    toc = ["<!-- TOC -->", ""]
    toc.append(f"- [{base_name}](#{base_name.lower().replace(' ', '-')})")
    toc.append("    - [Document Table of Contents](#document-table-of-contents)")
    toc.append("    - [Repo File Tree](#repo-file-tree)")
    toc.append("    - [Repo File Contents](#repo-file-contents)")

    # Sort file paths, placing README.md first and .gitignore second
    sorted_paths = sorted(file_paths, key=lambda x: (x != "README.md", x != ".gitignore", x.lower()))

    for path in sorted_paths:
        # Normalize path separators to forward slashes
        normalized_path = path.replace(os.sep, "/")

        # Create the link by removing dots and slashes, keep underscores exactly as-is
        link = normalized_path.lower().replace(".", "").replace("/", "")

        # Wrap the path in backticks for the heading display (no need to escape underscores)
        heading = f"`{normalized_path}`"

        toc.append(f"        - [{heading}](#{link})")

    toc.append("")
    toc.append("<!-- /TOC -->")

    return "\n".join(toc)


def generate_file_tree(
    directory_path: str,
    gitignore_spec: pathspec.PathSpec,
    include_ignored: bool = False,
    exclude_dirs: list[str] | None = None,
) -> str:
    """Generate an accurate file tree representation of the given directory."""

    def walk_directory(dir_path: str, prefix: str = "") -> list[str]:
        files = []
        contents = sorted(os.listdir(dir_path))
        dirs = [
            d
            for d in contents
            if os.path.isdir(os.path.join(dir_path, d))
            and not should_exclude_directory(d, include_ignored, exclude_dirs)
        ]
        regular_files = [
            f
            for f in contents
            if os.path.isfile(os.path.join(dir_path, f)) and f not in SYSTEM_FILES and f not in LOCK_FILES
        ]

        for idx, name in enumerate(dirs + regular_files):
            full_path = os.path.join(dir_path, name)
            rel_path = os.path.relpath(full_path, directory_path)

            if not include_ignored and gitignore_spec.match_file(rel_path):
                continue

            is_last = idx == len(dirs + regular_files) - 1
            current_prefix = "└── " if is_last else "├── "

            if os.path.isdir(full_path):
                files.append(f"{prefix}{current_prefix}{name}/")  # Add trailing slash for directories
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
