"""File content reading for CodeMapper."""

import os

import chardet

from ..config import MAX_FILE_SIZE_CHARS
from .detect_types import is_large_file


def get_file_info(file_path: str) -> str:
    """Get information about a file without reading its contents."""
    import mimetypes

    size = os.path.getsize(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)
    return f"File Type: {mime_type or 'Unknown'}, Size: {size} bytes"


def read_file_content(file_path: str) -> str:
    """Read file content with encoding detection and large file handling."""
    if is_large_file(file_path):
        return f"[Large or binary file detected. {get_file_info(file_path)}]"

    # Check file size before reading to avoid context bloat
    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE_CHARS:
        chars_formatted = f"{file_size:,}"
        tokens_estimate = file_size // 4  # Rough estimate: 1 token ≈ 4 chars
        return (
            f"[File too large for context inclusion. "
            f"Size: {chars_formatted} characters (~{tokens_estimate:,} tokens). "
            f"Maximum size: {MAX_FILE_SIZE_CHARS:,} characters.]"
        )

    try:
        with open(file_path, "rb") as file:
            raw_data = file.read(1024)  # Read only the first 1024 bytes for detection
        detect_result = chardet.detect(raw_data)
        detected_encoding = detect_result["encoding"] if detect_result else None

        encodings_to_try = [detected_encoding, "utf-8", "latin-1"]

        for encoding in encodings_to_try:
            if encoding:
                try:
                    with open(file_path, encoding=encoding) as file:
                        content = file.read().rstrip()
                        # Double-check after reading in case file grew or encoding inflated size
                        if len(content) > MAX_FILE_SIZE_CHARS:
                            chars_formatted = f"{len(content):,}"
                            tokens_estimate = len(content) // 4
                            return (
                                f"[File too large for context inclusion. "
                                f"Size: {chars_formatted} characters (~{tokens_estimate:,} tokens). "
                                f"Maximum size: {MAX_FILE_SIZE_CHARS:,} characters.]"
                            )
                        return content
                except UnicodeDecodeError:
                    continue

        return f"[Error: Unable to decode file with detected encoding ({detected_encoding}), UTF-8, or Latin-1]"
    except OSError as e:
        return f"[Error reading file: {str(e)}]"
