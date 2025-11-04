"""Shared pytest fixtures for all tests."""

import tempfile
from pathlib import Path

import pathspec
import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as temp_dir_name:
        yield Path(temp_dir_name)


@pytest.fixture
def sample_repo(temp_dir):
    """Create a sample repository structure for testing."""
    # Create test files
    (temp_dir / "README.md").write_text("# Test Repository", encoding="utf-8")
    (temp_dir / ".gitignore").write_text("*.log\n__pycache__/\n", encoding="utf-8")
    (temp_dir / "main.py").write_text("print('Hello, World!')", encoding="utf-8")
    (temp_dir / "test.log").write_text("test log content", encoding="utf-8")

    # Create nested directory structure
    src_dir = temp_dir / "src"
    src_dir.mkdir()
    (src_dir / "__init__.py").write_text("", encoding="utf-8")
    (src_dir / "app.py").write_text("# App code", encoding="utf-8")

    # Create docs directory
    docs_dir = temp_dir / "docs"
    docs_dir.mkdir()
    (docs_dir / "guide.md").write_text("# Guide", encoding="utf-8")

    return temp_dir


@pytest.fixture
def empty_gitignore_spec():
    """Create an empty gitignore specification."""
    return pathspec.PathSpec.from_lines("gitwildmatch", [])


@pytest.fixture
def sample_gitignore_spec():
    """Create a sample gitignore specification."""
    patterns = ["*.log", "__pycache__/", "*.pyc", ".env"]
    return pathspec.PathSpec.from_lines("gitwildmatch", patterns)
