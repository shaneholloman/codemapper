"""Unit tests for CodeMapper functionality."""

import tempfile
from pathlib import Path

import pytest
import pathspec

from codemapper.utils import (
    should_exclude_directory,
    determine_code_fence,
    load_gitignore_specs,
    collect_file_paths,
    is_large_file,
    read_file_content,
)

@pytest.fixture(name='test_dir')
def create_temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as temp_dir_name:
        yield temp_dir_name

@pytest.fixture(name='test_repo')
def create_sample_repo(test_dir):
    """Create a sample repository structure for testing."""
    # Create test files
    Path(test_dir, "README.md").write_text("# Test Repository", encoding='utf-8')
    Path(test_dir, ".gitignore").write_text("*.log\n__pycache__/", encoding='utf-8')
    Path(test_dir, "main.py").write_text("print('Hello, World!')", encoding='utf-8')
    Path(test_dir, "test.log").write_text("test log content", encoding='utf-8')

    # Create nested directory structure
    src_dir = Path(test_dir, "src")
    src_dir.mkdir()
    Path(src_dir, "__init__.py").write_text("", encoding='utf-8')
    Path(src_dir, "app.py").write_text("# App code", encoding='utf-8')

    return test_dir

# Test cases for utility functions
def test_should_exclude_directory():
    """Test directory exclusion logic."""
    assert should_exclude_directory(".git") is True
    assert should_exclude_directory("src") is False
    assert should_exclude_directory(".git", include_ignored=True) is True
    assert should_exclude_directory(".gitignore", include_ignored=True) is False

def test_determine_code_fence():
    """Test code fence language determination."""
    assert determine_code_fence("test.py") == "python"
    assert determine_code_fence("README.md") == "markdown"
    assert determine_code_fence("Dockerfile") == "dockerfile"
    assert determine_code_fence("unknown.xyz") == "txt"

def test_load_gitignore_specs(test_repo):
    """Test gitignore specifications loading."""
    specs = load_gitignore_specs(test_repo)
    assert isinstance(specs, pathspec.PathSpec)
    assert specs.match_file("test.log") is True
    assert specs.match_file("main.py") is False

def test_collect_file_paths(test_repo):
    """Test file path collection."""
    specs = load_gitignore_specs(test_repo)
    paths = collect_file_paths(test_repo, specs)

    assert "README.md" in paths
    assert "main.py" in paths
    assert "src/app.py" in paths
    assert "test.log" not in paths  # Should be ignored per .gitignore

    # Test with include_ignored=True
    all_paths = collect_file_paths(test_repo, specs, include_ignored=True)
    assert "test.log" in all_paths

def test_is_large_file(test_dir):
    """Test large file detection."""
    # Create a test file larger than typical text files
    large_file = Path(test_dir, "large.bin")
    large_file.write_bytes(b'\0' * 1024 * 1024)  # 1MB file

    small_file = Path(test_dir, "small.txt")
    small_file.write_text("Hello World", encoding='utf-8')

    assert is_large_file(str(large_file)) is True
    assert is_large_file(str(small_file)) is False

def test_read_file_content(test_dir):
    """Test file content reading with different encodings."""
    # Test UTF-8 file
    utf8_file = Path(test_dir, "utf8.txt")
    utf8_content = "Hello, 世界!"
    utf8_file.write_text(utf8_content, encoding='utf-8')
    assert read_file_content(str(utf8_file)) == utf8_content

    # Test binary file
    bin_file = Path(test_dir, "test.bin")
    bin_file.write_bytes(b'\x00\x01\x02\x03')
    assert "Large or binary file detected" in read_file_content(str(bin_file))

def test_integration_sample_repo(test_repo):
    """Integration test using a sample repository."""
    specs = load_gitignore_specs(test_repo)
    paths = collect_file_paths(test_repo, specs)

    assert len(paths) >= 3  # README.md, main.py, src/app.py

    allowed_extensions = ('.md', '.py')
    allowed_files = {'.gitignore'}
    assert all(
        p.endswith(allowed_extensions) or p in allowed_files
        for p in paths
    )

# Add test for handling non-existent files
def test_read_nonexistent_file():
    """Test reading a non-existent file."""
    content = read_file_content("nonexistent_file.txt")
    assert "Error reading file" in content

if __name__ == "__main__":
    pytest.main([__file__])
