"""
CodeMapper: A tool for generating comprehensive Markdown artifacts of
directory structures and file contents.

Package Structure:
- cli.py: CLI entry point and argument parsing
- config.py: Configuration constants and TOML loading
- types.py: Dataclass definitions

- readers/: Input operations (file reading, directory scanning)
- processors/: Data transformation (git operations, format conversion)
- builders/: Document assembly (codemap, docmap, markdown structures)
- writers/: Output operations (file writing, directory management)

This package provides functionality to analyze local directories or GitHub repositories,
creating detailed Markdown documentation of their structure and contents.
"""

from importlib.metadata import version

__version__ = version("codemapper")

# Export key functions and types for backward compatibility
from .builders.build_codemap import generate_markdown_document
from .builders.build_docmap import generate_docmap_content
from .config import get_output_directory, load_user_config
from .processors.process_dir import capture_source, detect_input_type, should_exclude_directory
from .processors.process_git import clone_github_repo, get_git_info
from .readers.detect_types import determine_code_fence, is_large_file
from .readers.read_files import read_file_content
from .readers.scan_paths import collect_file_paths, load_gitignore_specs
from .types import BaseMapConfig, CodeMapConfig, DocMapConfig
from .writers.manage_output import manage_output_directory

__all__ = [
    "__version__",
    # Types
    "BaseMapConfig",
    "CodeMapConfig",
    "DocMapConfig",
    # Config
    "load_user_config",
    "get_output_directory",
    # Readers
    "determine_code_fence",
    "is_large_file",
    "read_file_content",
    "collect_file_paths",
    "load_gitignore_specs",
    # Processors
    "should_exclude_directory",
    "detect_input_type",
    "capture_source",
    "clone_github_repo",
    "get_git_info",
    # Builders
    "generate_markdown_document",
    "generate_docmap_content",
    # Writers
    "manage_output_directory",
]
