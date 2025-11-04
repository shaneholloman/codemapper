"""Directory processing and filtering for CodeMapper."""

import os
import re

from .process_git import get_git_info


def should_exclude_directory(
    dir_name: str, include_ignored: bool = False, exclude_dirs: list[str] | None = None
) -> bool:
    """
    Determine if a directory should be excluded from processing.

    Args:
        dir_name: Name of the directory to check
        include_ignored: Whether to include git-ignored files
        exclude_dirs: List of additional directories to exclude
    """
    # Default exclusions - always exclude these
    always_exclude = {".git", ".venv", ".conda", "node_modules"}

    # Cache and build directories - exclude unless specifically included
    cache_exclusions = {
        ".ruff_cache",
        ".pytest_cache",
        ".mypy_cache",
        ".tox",
        "__pycache__",
        ".cache",
        "dist",
        "build",
        "*.egg-info",
    }

    if include_ignored:
        return dir_name in always_exclude

    # Combine all exclusions with user-specified ones
    exclusions = always_exclude | cache_exclusions
    if exclude_dirs:
        exclusions.update(exclude_dirs)

    return dir_name in exclusions


def detect_input_type(input_path: str) -> tuple[str, str]:
    """Detect whether the input is a local directory or a GitHub URL."""
    # Check if it's a valid local directory
    if os.path.isdir(input_path):
        return "local", input_path

    # Check if it's a valid GitHub URL
    github_pattern = r"^https?://github\.com/[\w-]+/[\w.-]+(?:\.git)?$"
    if re.match(github_pattern, input_path):
        return "github", input_path

    raise ValueError("Invalid input. Please provide a valid local directory path or GitHub URL.")


def capture_source(input_path: str, directory_path: str | None = None) -> str:
    """Capture the source of the pulled repo with git metadata."""
    source_lines = []

    if os.path.isdir(input_path):
        source_lines.append(f"Local directory: `{os.path.abspath(input_path)}`")
    else:
        source_lines.append(f"GitHub repository: <{input_path}>")

    # Add git information if available
    git_dir = directory_path if directory_path else input_path
    if os.path.isdir(git_dir):
        git_info = get_git_info(git_dir)
        if git_info:
            source_lines.append("")
            source_lines.append("**Git Information:**")
            source_lines.append("")
            if "branch" in git_info:
                source_lines.append(f"- Branch: `{git_info['branch']}`")
            if "commit" in git_info:
                source_lines.append(f"- Commit: `{git_info['commit']}`")
            if "date" in git_info:
                source_lines.append(f"- Date: {git_info['date']}")
            if "remote" in git_info:
                source_lines.append(f"- Remote: <{git_info['remote']}>")

    return "\n".join(source_lines)
