"""Unit tests for readers/read_files.py"""

import pytest

from codemapper.readers.read_files import get_file_info, read_file_content


def test_read_file_content_utf8(temp_dir):
    """Test reading UTF-8 encoded files."""
    test_file = temp_dir / "utf8.txt"
    content = "Hello, World!"
    test_file.write_text(content, encoding="utf-8")

    result = read_file_content(str(test_file))
    assert result == content


def test_read_file_content_unicode(temp_dir):
    """Test reading files with unicode characters."""
    test_file = temp_dir / "unicode.txt"
    content = "Hello, 世界! Привет!"
    test_file.write_text(content, encoding="utf-8")

    result = read_file_content(str(test_file))
    assert result == content


def test_read_file_content_binary(temp_dir):
    """Test that binary files are detected and not read."""
    test_file = temp_dir / "test.bin"
    test_file.write_bytes(b"\x00\x01\x02\x03\xff")

    result = read_file_content(str(test_file))
    assert "Large or binary file detected" in result
    assert "File Type:" in result


def test_read_file_content_large_file(temp_dir):
    """Test that very large files show size warning."""
    test_file = temp_dir / "huge.txt"
    # Create file larger than 300k chars
    large_content = "x" * 350000
    test_file.write_text(large_content, encoding="utf-8")

    result = read_file_content(str(test_file))
    assert "File too large for context inclusion" in result
    assert "characters" in result
    assert "tokens" in result
    assert "300,000" in result


def test_read_file_content_nonexistent(temp_dir):
    """Test reading non-existent file."""
    # File doesn't exist, so os.path.getsize will raise FileNotFoundError
    # which gets caught by the OSError except block
    with pytest.raises(FileNotFoundError):
        read_file_content(str(temp_dir / "nonexistent.txt"))


def test_read_file_content_strips_trailing_whitespace(temp_dir):
    """Test that trailing whitespace is removed."""
    test_file = temp_dir / "whitespace.txt"
    test_file.write_text("content\n\n\n", encoding="utf-8")

    result = read_file_content(str(test_file))
    assert result == "content"
    assert not result.endswith("\n")


def test_get_file_info(temp_dir):
    """Test file info extraction."""
    test_file = temp_dir / "test.txt"
    test_file.write_text("Hello", encoding="utf-8")

    info = get_file_info(str(test_file))
    assert "File Type:" in info
    assert "Size:" in info
    assert "bytes" in info


def test_read_file_content_empty_file(temp_dir):
    """Test reading empty file."""
    test_file = temp_dir / "empty.txt"
    test_file.write_text("", encoding="utf-8")

    result = read_file_content(str(test_file))
    assert result == ""


def test_read_file_content_image_file(temp_dir):
    """Test that image files are marked as binary."""
    test_file = temp_dir / "test.jpg"
    test_file.write_bytes(b"\xff\xd8\xff")  # JPEG magic bytes

    result = read_file_content(str(test_file))
    assert "Large or binary file detected" in result
