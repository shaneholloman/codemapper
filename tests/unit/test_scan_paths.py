"""Unit tests for readers/scan_paths.py"""

import pathspec

from codemapper.readers.scan_paths import collect_file_paths, load_gitignore_specs


def test_load_gitignore_specs_with_file(temp_dir):
    """Test loading gitignore specifications."""
    gitignore = temp_dir / ".gitignore"
    gitignore.write_text("*.log\n__pycache__/\n*.pyc\n", encoding="utf-8")

    spec = load_gitignore_specs(str(temp_dir))
    assert isinstance(spec, pathspec.PathSpec)
    assert spec.match_file("test.log") is True
    assert spec.match_file("main.py") is False
    assert spec.match_file("__pycache__/") is True


def test_load_gitignore_specs_no_file(temp_dir):
    """Test loading gitignore when no .gitignore exists."""
    spec = load_gitignore_specs(str(temp_dir))
    assert isinstance(spec, pathspec.PathSpec)
    # Empty spec should not match anything
    assert spec.match_file("any.file") is False


def test_collect_file_paths_basic(sample_repo, empty_gitignore_spec):
    """Test basic file path collection."""
    paths = collect_file_paths(str(sample_repo), empty_gitignore_spec)

    assert "README.md" in paths
    assert "main.py" in paths
    assert "src/app.py" in paths
    assert "src/__init__.py" in paths


def test_collect_file_paths_respects_gitignore(sample_repo):
    """Test that gitignore rules are respected."""
    spec = load_gitignore_specs(str(sample_repo))
    paths = collect_file_paths(str(sample_repo), spec)

    assert "README.md" in paths
    assert "main.py" in paths
    assert "test.log" not in paths  # Should be ignored


def test_collect_file_paths_include_ignored(sample_repo):
    """Test including git-ignored files."""
    spec = load_gitignore_specs(str(sample_repo))
    paths = collect_file_paths(str(sample_repo), spec, include_ignored=True)

    assert "test.log" in paths  # Now included


def test_collect_file_paths_excludes_system_files(temp_dir, empty_gitignore_spec):
    """Test that system files are excluded."""
    (temp_dir / "README.md").write_text("# Test", encoding="utf-8")
    (temp_dir / ".DS_Store").write_text("fake", encoding="utf-8")
    (temp_dir / "Thumbs.db").write_text("fake", encoding="utf-8")

    paths = collect_file_paths(str(temp_dir), empty_gitignore_spec)

    assert "README.md" in paths
    assert ".DS_Store" not in paths
    assert "Thumbs.db" not in paths


def test_collect_file_paths_excludes_lock_files(temp_dir, empty_gitignore_spec):
    """Test that lock files are excluded."""
    (temp_dir / "package.json").write_text("{}", encoding="utf-8")
    (temp_dir / "package-lock.json").write_text("{}", encoding="utf-8")
    (temp_dir / "uv.lock").write_text("", encoding="utf-8")
    (temp_dir / "yarn.lock").write_text("", encoding="utf-8")

    paths = collect_file_paths(str(temp_dir), empty_gitignore_spec)

    assert "package.json" in paths
    assert "package-lock.json" not in paths
    assert "uv.lock" not in paths
    assert "yarn.lock" not in paths


def test_collect_file_paths_excludes_archives(temp_dir, empty_gitignore_spec):
    """Test that archive files are excluded."""
    (temp_dir / "README.md").write_text("# Test", encoding="utf-8")
    (temp_dir / "archive.zip").write_bytes(b"PK\x03\x04")
    (temp_dir / "backup.tar.gz").write_bytes(b"\x1f\x8b")

    paths = collect_file_paths(str(temp_dir), empty_gitignore_spec)

    assert "README.md" in paths
    assert "archive.zip" not in paths
    assert "backup.tar.gz" not in paths


def test_collect_file_paths_normalized_separators(temp_dir, empty_gitignore_spec):
    """Test that path separators are normalized to forward slashes."""
    nested = temp_dir / "nested" / "deep"
    nested.mkdir(parents=True)
    (nested / "file.py").write_text("code", encoding="utf-8")

    paths = collect_file_paths(str(temp_dir), empty_gitignore_spec)

    # All paths should use forward slashes
    nested_files = [p for p in paths if "nested" in p]
    assert len(nested_files) > 0
    assert all("/" in p and "\\" not in p for p in nested_files)
    assert "nested/deep/file.py" in paths


def test_collect_file_paths_exclude_directories(temp_dir, empty_gitignore_spec):
    """Test excluding specific directories."""
    (temp_dir / "src").mkdir()
    (temp_dir / "src" / "app.py").write_text("code", encoding="utf-8")
    (temp_dir / "tests").mkdir()
    (temp_dir / "tests" / "test.py").write_text("test", encoding="utf-8")

    paths = collect_file_paths(str(temp_dir), empty_gitignore_spec, exclude_dirs=["tests"])

    assert any("src/app.py" in p for p in paths)
    assert not any("tests/" in p for p in paths)
