"""Unit tests for processors/process_dir.py"""

import pytest

from codemapper.processors.process_dir import capture_source, detect_input_type, should_exclude_directory


def test_should_exclude_directory_defaults():
    """Test default directory exclusions."""
    assert should_exclude_directory(".git") is True
    assert should_exclude_directory(".venv") is True
    assert should_exclude_directory(".conda") is True
    assert should_exclude_directory("node_modules") is True
    assert should_exclude_directory("src") is False


def test_should_exclude_directory_cache_dirs():
    """Test cache directory exclusions."""
    assert should_exclude_directory(".ruff_cache") is True
    assert should_exclude_directory(".pytest_cache") is True
    assert should_exclude_directory("__pycache__") is True
    assert should_exclude_directory("dist") is True
    assert should_exclude_directory("build") is True


def test_should_exclude_directory_include_ignored():
    """Test that include_ignored only excludes always_exclude set."""
    # With include_ignored=True, only always_exclude is enforced
    assert should_exclude_directory(".git", include_ignored=True) is True
    assert should_exclude_directory(".venv", include_ignored=True) is True
    assert should_exclude_directory(".ruff_cache", include_ignored=True) is False
    assert should_exclude_directory("dist", include_ignored=True) is False


def test_should_exclude_directory_custom_exclusions():
    """Test custom directory exclusions."""
    custom = ["custom_dir", "another_dir"]
    assert should_exclude_directory("custom_dir", exclude_dirs=custom) is True
    assert should_exclude_directory("another_dir", exclude_dirs=custom) is True
    assert should_exclude_directory("normal_dir", exclude_dirs=custom) is False


def test_detect_input_type_local_directory(temp_dir):
    """Test detection of local directory."""
    input_type, path = detect_input_type(str(temp_dir))
    assert input_type == "local"
    assert path == str(temp_dir)


def test_detect_input_type_github_url():
    """Test detection of GitHub URL."""
    url = "https://github.com/user/repo"
    input_type, path = detect_input_type(url)
    assert input_type == "github"
    assert path == url


def test_detect_input_type_github_url_with_git():
    """Test detection of GitHub URL with .git suffix."""
    url = "https://github.com/user/repo.git"
    input_type, path = detect_input_type(url)
    assert input_type == "github"
    assert path == url


def test_detect_input_type_http_github():
    """Test detection of GitHub URL with http (not https)."""
    url = "http://github.com/user/repo"
    input_type, path = detect_input_type(url)
    assert input_type == "github"
    assert path == url


def test_detect_input_type_invalid():
    """Test that invalid input raises ValueError."""
    with pytest.raises(ValueError, match="Invalid input"):
        detect_input_type("not-a-path-or-url")

    with pytest.raises(ValueError, match="Invalid input"):
        detect_input_type("https://gitlab.com/user/repo")


def test_capture_source_local_directory(temp_dir):
    """Test capturing source for local directory."""
    source = capture_source(str(temp_dir))
    assert "Local directory:" in source
    assert str(temp_dir) in source


def test_capture_source_github_url():
    """Test capturing source for GitHub URL."""
    url = "https://github.com/user/repo"
    source = capture_source(url)
    assert "GitHub repository:" in source
    assert url in source


def test_capture_source_with_git_info(sample_repo):
    """Test capturing source includes git info if available."""
    # Initialize git repo
    import subprocess

    subprocess.run(["git", "init"], cwd=sample_repo, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=sample_repo, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=sample_repo, capture_output=True)
    subprocess.run(["git", "add", "."], cwd=sample_repo, capture_output=True)
    subprocess.run(["git", "commit", "-m", "Initial"], cwd=sample_repo, capture_output=True)

    source = capture_source(str(sample_repo))
    assert "Git Information:" in source
    assert "Branch:" in source
    assert "Commit:" in source
