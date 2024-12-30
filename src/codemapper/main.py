"""
CodeMapper: Comprehensive Codebase Visualization for Humans and AI

Main execution module for CodeMapper tool.
"""

import argparse
import os
import subprocess
import sys

from . import __version__
from .config import CODEMAP_SUFFIX, DOCMAP_SUFFIX
from .utils import (
    load_gitignore_specs,
    generate_markdown_document,
    detect_input_type,
    clone_github_repo,
    manage_output_directory,
    capture_source,
    CodeMapConfig,
)

# Import both the function and the configuration class
from .docmap import generate_docmap_content, DocMapConfig


def main():
    """Main function to orchestrate the markdown document generation process."""
    parser = argparse.ArgumentParser(
        description="Generate markdown document from directory structure or GitHub repository."
    )
    parser.add_argument(
        "input_path",
        nargs="?",
        help="Path to the directory to process or GitHub repository URL",
    )
    parser.add_argument(
        "--include-ignored",
        action="store_true",
        help="Include files normally ignored by .gitignore",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"CodeMapper version {__version__}",
        help="Show the version number and exit",
    )
    parser.add_argument(
        "--docs",
        action="store_true",
        help="Generate documentation map instead of code map",
    )
    parser.add_argument(
        "--docs-dir",
        help="Specify custom documentation directory path",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        help="Exclude specified directory from output (can be used multiple times). "
        "Note: .venv, .conda, and node_modules are excluded by default.",
    )
    args = parser.parse_args()

    if not args.input_path:
        parser.print_help()
        sys.exit(1)

    try:
        input_type, path = detect_input_type(args.input_path)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    source = capture_source(args.input_path)

    if input_type == "github":
        try:
            directory_path = clone_github_repo(path)
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
            sys.exit(1)
        except OSError as e:
            print(f"Error creating directory: {e}")
            sys.exit(1)
    else:
        directory_path = path

    if not os.path.isabs(args.input_path) and not args.input_path.startswith(
        ("http://", "https://")
    ):
        base_name = os.path.basename(os.path.abspath(args.input_path))
    else:
        base_name = os.path.basename(directory_path)

    gitignore_spec = load_gitignore_specs(directory_path)

    if args.docs:
        # Create a DocMapConfig object with all our parameters
        doc_config = DocMapConfig(
            directory_path=directory_path,
            gitignore_spec=gitignore_spec,
            include_ignored=args.include_ignored,
            source=source,
            base_name=base_name,
            doc_dir=args.docs_dir,
            exclude_dirs=args.exclude,
        )
        # Pass the config object to generate_docmap_content
        markdown_content = generate_docmap_content(doc_config)
        output_file_path = manage_output_directory(
            base_name=base_name,
            input_path=args.input_path,
            suffix=DOCMAP_SUFFIX,
        )
    else:
        # Create a CodeMapConfig object with all our parameters
        code_config = CodeMapConfig(
            directory_path=directory_path,
            gitignore_spec=gitignore_spec,
            include_ignored=args.include_ignored,
            source=source,
            base_name=base_name,
            exclude_dirs=args.exclude,
        )
        # Pass the config object to generate_markdown_document
        markdown_content = generate_markdown_document(code_config)
        output_file_path = manage_output_directory(
            base_name=base_name,
            input_path=args.input_path,
            suffix=CODEMAP_SUFFIX,
        )

    with open(output_file_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file has been created: {output_file_path}")


if __name__ == "__main__":
    main()
