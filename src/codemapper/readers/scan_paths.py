"""Directory scanning and path collection for CodeMapper."""

import os

import pathspec

from ..config import ARCHIVE_EXTENSIONS, LOCK_FILES, SYSTEM_FILES
from ..processors.process_dir import should_exclude_directory


def collect_file_paths(
    directory_path: str,
    gitignore_spec: pathspec.PathSpec,
    include_ignored: bool = False,
    exclude_dirs: list[str] | None = None,
) -> list[str]:
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
            # Skip system files
            if filename in SYSTEM_FILES:
                continue
            # Skip lock files
            if filename in LOCK_FILES:
                continue
            # Skip archive files
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


def load_gitignore_specs(base_path: str) -> pathspec.PathSpec:
    """Load .gitignore specifications from the given base path."""
    gitignore_path = os.path.join(base_path, ".gitignore")
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, encoding="utf-8") as file:
            return pathspec.PathSpec.from_lines("gitwildmatch", file)
    return pathspec.PathSpec.from_lines("gitwildmatch", [])
