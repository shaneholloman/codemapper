"""Output file management for CodeMapper."""

import os

from ..config import CODEMAP_SUFFIX


def manage_output_directory(
    base_name: str,
    input_path: str,
    suffix: str = CODEMAP_SUFFIX,
    output_dir: str | None = None,
) -> str:
    """
    Manage the output directory for the markdown output.

    Args:
        base_name (str): Base name for the output file
        input_path (str): Original input path (used for relative path handling)
        suffix (str): Suffix for the output file. Defaults to CODEMAP_SUFFIX.
        output_dir (str | None): Output directory path. Defaults to None (use .codemaps in CWD).

    Returns:
        str: Path to the output file
    """
    # Use provided output_dir or default to .codemaps in current directory
    if output_dir is None:
        output_dir = os.path.join(".", ".codemaps")

    # Expand user home directory if present
    output_dir = os.path.expanduser(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # If input_path is a relative path, use its basename
    if not os.path.isabs(input_path) and not input_path.startswith(("http://", "https://")):
        base_name = os.path.basename(os.path.abspath(input_path))

    file_name = f"{base_name}{suffix}"
    return os.path.join(output_dir, file_name)
