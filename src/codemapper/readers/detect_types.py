"""File type detection for CodeMapper."""

import mimetypes
import os

from ..config import CODE_FENCE_MAP, LARGE_FILE_EXTENSIONS


def determine_code_fence(file_path: str) -> str:
    """Determine the appropriate code fence language based on the file path."""
    _, ext = os.path.splitext(file_path)
    file_name = os.path.basename(file_path)

    # Check for specific file names first
    if file_name in CODE_FENCE_MAP:
        return CODE_FENCE_MAP[file_name]

    # Then check for extensions
    return CODE_FENCE_MAP.get(ext.lower(), "txt")


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
            "application/typescript",
            "application/xml",
            "application/x-httpd-php",
            "application/x-sh",
            "application/x-csh",
            "application/x-yaml",
            "application/toml",
        ]
        return not any(mime_type.startswith(text_type) for text_type in text_mime_types)

    # If MIME type couldn't be determined, assume it's not a large file
    return False
