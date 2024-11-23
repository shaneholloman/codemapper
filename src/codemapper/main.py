"""
CodeMapper: Comprehensive Codebase Visualization for Humans and AI

Main execution module for CodeMapper tool.
"""

import argparse
import os
import subprocess  # Added missing import
import sys

from . import __version__
from .utils import (
    load_gitignore_specs,
    generate_markdown_document,
    detect_input_type,
    clone_github_repo,
    manage_output_directory,
    capture_source,  # Added missing import
)

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
    markdown_content = generate_markdown_document(
        directory_path, gitignore_spec, args.include_ignored, source, base_name
    )

    output_file_path = manage_output_directory(base_name, args.input_path)

    with open(output_file_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file has been created: {output_file_path}")

if __name__ == "__main__":
    main()
