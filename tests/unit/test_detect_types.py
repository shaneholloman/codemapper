"""Unit tests for readers/detect_types.py"""

from codemapper.readers.detect_types import determine_code_fence, is_large_file


def test_determine_code_fence_by_extension():
    """Test code fence determination by file extension."""
    assert determine_code_fence("test.py") == "python"
    assert determine_code_fence("README.md") == "markdown"
    assert determine_code_fence("script.sh") == "bash"
    assert determine_code_fence("data.json") == "json"
    assert determine_code_fence("app.ts") == "typescript"
    assert determine_code_fence("component.tsx") == "tsx"
    assert determine_code_fence("style.css") == "css"


def test_determine_code_fence_by_filename():
    """Test code fence determination by specific filename."""
    assert determine_code_fence("Dockerfile") == "dockerfile"
    assert determine_code_fence("Makefile") == "makefile"
    assert determine_code_fence(".gitignore") == "ini"
    assert determine_code_fence("package.json") == "json"


def test_determine_code_fence_unknown():
    """Test code fence for unknown file types."""
    assert determine_code_fence("unknown.xyz") == "txt"
    assert determine_code_fence("no_extension") == "txt"


def test_is_large_file_by_extension():
    """Test large file detection by extension."""
    # Image files
    assert is_large_file("photo.jpg") is True
    assert is_large_file("image.png") is True
    assert is_large_file("icon.svg") is True

    # Video files
    assert is_large_file("video.mp4") is True
    assert is_large_file("movie.avi") is True

    # Audio files
    assert is_large_file("song.mp3") is True
    assert is_large_file("audio.wav") is True

    # Database files
    assert is_large_file("data.db") is True
    assert is_large_file("app.sqlite") is True

    # Log and temp files
    assert is_large_file("app.log") is True
    assert is_large_file("temp.tmp") is True
    assert is_large_file("backup.bak") is True


def test_is_large_file_code_files():
    """Test that code files are NOT considered large."""
    assert is_large_file("app.py") is False
    assert is_large_file("script.js") is False
    assert is_large_file("component.ts") is False
    assert is_large_file("styles.css") is False
    assert is_large_file("README.md") is False
    assert is_large_file("config.json") is False
    assert is_large_file("data.csv") is False


def test_is_large_file_known_text_types():
    """Test that known text file types are not considered large."""
    assert is_large_file("test.txt") is False
    assert is_large_file("config.yaml") is False
    assert is_large_file("script.sh") is False


def test_is_large_file_actual_file(temp_dir):
    """Test large file detection with actual files."""
    # Create small text file
    small_file = temp_dir / "small.txt"
    small_file.write_text("Hello World", encoding="utf-8")
    assert is_large_file(str(small_file)) is False

    # Create binary file
    binary_file = temp_dir / "test.bin"
    binary_file.write_bytes(b"\x00\x01\x02\x03")
    assert is_large_file(str(binary_file)) is True
