"""Unit tests for writers/manage_output.py"""

import os

from codemapper.writers.manage_output import manage_output_directory


def test_manage_output_directory_default(temp_dir):
    """Test default output directory management."""
    os.chdir(temp_dir)
    output_path = manage_output_directory("testproject", str(temp_dir))

    assert output_path == "./.codemaps/testproject.codemap.md"
    assert os.path.exists("./.codemaps")


def test_manage_output_directory_custom_output_dir(temp_dir):
    """Test custom output directory."""
    os.chdir(temp_dir)
    custom_dir = str(temp_dir / "custom")
    output_path = manage_output_directory("testproject", str(temp_dir), output_dir=custom_dir)

    assert output_path.startswith(custom_dir)
    assert output_path.endswith("testproject.codemap.md")
    assert os.path.exists(custom_dir)


def test_manage_output_directory_custom_suffix(temp_dir):
    """Test custom file suffix."""
    os.chdir(temp_dir)
    output_path = manage_output_directory("testproject", str(temp_dir), suffix=".docmap.md")

    assert output_path.endswith(".docmap.md")


def test_manage_output_directory_creates_dir(temp_dir):
    """Test that output directory is created if it doesn't exist."""
    os.chdir(temp_dir)
    output_path = manage_output_directory("test", str(temp_dir))

    output_dir = os.path.dirname(output_path)
    assert os.path.exists(output_dir)
    assert os.path.isdir(output_dir)


def test_manage_output_directory_expands_tilde(temp_dir):
    """Test that ~ is expanded in output directory."""
    output_path = manage_output_directory("test", str(temp_dir), output_dir="~/codemaps")

    assert "~" not in output_path
    assert output_path.startswith("/")
