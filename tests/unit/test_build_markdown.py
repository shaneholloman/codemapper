"""Unit tests for builders/build_markdown.py"""

from codemapper.builders.build_markdown import generate_file_tree, generate_toc


def test_generate_toc_basic():
    """Test basic TOC generation."""
    file_paths = ["README.md", "main.py", "src/app.py"]
    toc = generate_toc(file_paths, "TestProject")

    assert "<!-- TOC -->" in toc
    assert "<!-- /TOC -->" in toc
    assert "[TestProject](#testproject)" in toc
    assert "[Document Table of Contents](#document-table-of-contents)" in toc
    assert "[`README.md`](#readmemd)" in toc
    assert "[`main.py`](#mainpy)" in toc
    assert "[`src/app.py`](#srcapppy)" in toc


def test_generate_toc_readme_first():
    """Test that README.md is prioritized first in TOC."""
    file_paths = ["main.py", "README.md", "config.py"]
    toc = generate_toc(file_paths, "Test")

    lines = toc.split("\n")
    readme_line = next(i for i, line in enumerate(lines) if "README.md" in line)
    main_line = next(i for i, line in enumerate(lines) if "main.py" in line)

    assert readme_line < main_line


def test_generate_toc_gitignore_second():
    """Test that .gitignore comes after README but before others."""
    file_paths = ["README.md", ".gitignore", "main.py", "app.py"]
    toc = generate_toc(file_paths, "Test")

    lines = toc.split("\n")
    readme_idx = next(i for i, line in enumerate(lines) if "README.md" in line)
    gitignore_idx = next(i for i, line in enumerate(lines) if ".gitignore" in line)
    main_idx = next(i for i, line in enumerate(lines) if "main.py" in line)

    assert readme_idx < gitignore_idx < main_idx


def test_generate_toc_four_space_indent():
    """Test that TOC uses 4-space indentation."""
    file_paths = ["main.py"]
    toc = generate_toc(file_paths, "Test")

    toc.split("\n")
    # First level indent (under main heading)
    assert "    - [Document Table of Contents]" in toc
    # Second level indent (file entries)
    assert "        - [`main.py`]" in toc


def test_generate_toc_backticks_in_filenames():
    """Test that filenames are wrapped in backticks."""
    file_paths = ["src/__init__.py", "app.py"]
    toc = generate_toc(file_paths, "Test")

    assert "[`src/__init__.py`]" in toc
    assert "[`app.py`]" in toc


def test_generate_file_tree_basic(sample_repo, empty_gitignore_spec):
    """Test basic file tree generation."""
    tree = generate_file_tree(str(sample_repo), empty_gitignore_spec)

    assert tree.startswith(".")
    assert "README.md" in tree
    assert "main.py" in tree
    assert "src/" in tree
    assert "├──" in tree or "└──" in tree
    assert "directories" in tree
    assert "files" in tree


def test_generate_file_tree_respects_gitignore(sample_repo):
    """Test that file tree respects gitignore."""
    from codemapper.readers.scan_paths import load_gitignore_specs

    spec = load_gitignore_specs(str(sample_repo))
    tree = generate_file_tree(str(sample_repo), spec)

    assert "README.md" in tree
    assert "test.log" not in tree  # Should be ignored


def test_generate_file_tree_excludes_system_files(temp_dir, empty_gitignore_spec):
    """Test that system files are excluded from tree."""
    (temp_dir / "README.md").write_text("# Test", encoding="utf-8")
    (temp_dir / ".DS_Store").write_text("fake", encoding="utf-8")

    tree = generate_file_tree(str(temp_dir), empty_gitignore_spec)

    assert "README.md" in tree
    assert ".DS_Store" not in tree


def test_generate_file_tree_excludes_lock_files(temp_dir, empty_gitignore_spec):
    """Test that lock files are excluded from tree."""
    (temp_dir / "package.json").write_text("{}", encoding="utf-8")
    (temp_dir / "uv.lock").write_text("", encoding="utf-8")

    tree = generate_file_tree(str(temp_dir), empty_gitignore_spec)

    assert "package.json" in tree
    assert "uv.lock" not in tree


def test_generate_file_tree_counts(temp_dir, empty_gitignore_spec):
    """Test that tree includes directory and file counts."""
    (temp_dir / "file1.txt").write_text("1", encoding="utf-8")
    (temp_dir / "file2.txt").write_text("2", encoding="utf-8")
    (temp_dir / "dir1").mkdir()
    (temp_dir / "dir1" / "file3.txt").write_text("3", encoding="utf-8")

    tree = generate_file_tree(str(temp_dir), empty_gitignore_spec)

    # Should show counts
    assert "1 directories" in tree or "1 directory" in tree
    assert "files" in tree
