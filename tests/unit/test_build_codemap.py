"""Unit tests for builders/build_codemap.py"""

from codemapper.builders.build_codemap import generate_markdown_document
from codemapper.types import CodeMapConfig


def test_generate_markdown_document_basic(sample_repo, sample_gitignore_spec):
    """Test basic codemap generation."""
    config = CodeMapConfig(
        directory_path=str(sample_repo),
        gitignore_spec=sample_gitignore_spec,
        include_ignored=False,
        source="Test source",
        base_name="TestRepo",
        exclude_dirs=None,
    )

    result = generate_markdown_document(config)

    # Check structure
    assert "# TestRepo" in result
    assert "CodeMap Source: Test source" in result
    assert "## Document Table of Contents" in result
    assert "## Repo File Tree" in result
    assert "## Repo File Contents" in result


def test_generate_markdown_document_includes_files(sample_repo, sample_gitignore_spec):
    """Test that codemap includes expected files."""
    config = CodeMapConfig(
        directory_path=str(sample_repo),
        gitignore_spec=sample_gitignore_spec,
        source="Test",
        base_name="Test",
    )

    result = generate_markdown_document(config)

    assert "README.md" in result
    assert "main.py" in result
    assert "src/app.py" in result


def test_generate_markdown_document_respects_gitignore(sample_repo):
    """Test that codemap respects gitignore rules."""
    from codemapper.readers.scan_paths import load_gitignore_specs

    spec = load_gitignore_specs(str(sample_repo))
    config = CodeMapConfig(
        directory_path=str(sample_repo),
        gitignore_spec=spec,
        source="Test",
        base_name="Test",
    )

    result = generate_markdown_document(config)

    assert "README.md" in result
    assert "test.log" not in result  # Should be gitignored


def test_generate_markdown_document_uses_backticks_in_headings(sample_repo, empty_gitignore_spec):
    """Test that file headings use backticks."""
    config = CodeMapConfig(
        directory_path=str(sample_repo),
        gitignore_spec=empty_gitignore_spec,
        source="Test",
        base_name="Test",
    )

    result = generate_markdown_document(config)

    assert "### `README.md`" in result
    assert "### `main.py`" in result


def test_generate_markdown_document_four_backticks_for_markdown(temp_dir, empty_gitignore_spec):
    """Test that markdown files use quadruple backticks."""
    (temp_dir / "doc.md").write_text("# Documentation", encoding="utf-8")

    config = CodeMapConfig(
        directory_path=str(temp_dir),
        gitignore_spec=empty_gitignore_spec,
        source="Test",
        base_name="Test",
    )

    result = generate_markdown_document(config)

    # Markdown files should use ````markdown
    assert "````markdown" in result
    assert "### `doc.md`" in result
