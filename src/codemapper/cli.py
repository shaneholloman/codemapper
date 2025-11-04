"""
CodeMapper: Comprehensive Codebase Visualization for Humans and AI

Main execution module for CodeMapper tool.
"""

import argparse
import os
import subprocess
import sys

from . import __version__
from .builders.build_codemap import generate_markdown_document
from .builders.build_docmap import generate_docmap_content
from .config import CODEMAP_SUFFIX, DOCMAP_SUFFIX, get_output_directory, load_user_config
from .processors.process_dir import capture_source, detect_input_type
from .processors.process_git import clone_github_repo
from .readers.scan_paths import load_gitignore_specs
from .types import CodeMapConfig, DocMapConfig
from .writers.manage_output import manage_output_directory


def main():
    """Main function to orchestrate the markdown document generation process."""
    parser = argparse.ArgumentParser(
        prog="codemapper",
        description=(
            "Generate comprehensive Markdown codemaps from local directories or GitHub repositories.\n\n"
            "CodeMapper creates single-file Markdown documents containing:\n"
            "  - Complete directory tree structure\n"
            "  - All file contents with syntax highlighting\n"
            "  - Git metadata (branch, commit, remote)\n\n"
            "Output: project.codemap.md or project.docmap.md\n"
            "Default location: .codemaps/ in current directory\n"
            "Config file: ~/.codemapper/codemapper.toml (optional)"
        ),
        epilog=(
            "Examples:\n"
            "  codemapper /path/to/project\n"
            "  codemapper https://github.com/user/repo\n"
            "  codemapper --docs /path/to/project\n"
            "  codemapper --output-dir ~/all-codemaps /path/to/project\n"
            "  codemapper --exclude=tests --exclude=docs /path/to/project\n\n"
            "Configuration:\n"
            "  Create ~/.codemapper/codemapper.toml to set defaults:\n"
            '    output_dir = "~/.codemapper"  # Centralized collection\n'
            '    prefix_style = "underscore"    # Use _codemaps/ instead of .codemaps/\n\n'
            "Precedence: CLI flags > Config file > Defaults\n\n"
            "For more info: https://github.com/shaneholloman/codemapper"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "input_path",
        nargs="?",
        metavar="PATH_OR_URL",
        help="Local directory path or GitHub repository URL to process",
    )
    parser.add_argument(
        "--include-ignored",
        action="store_true",
        help="Include files normally ignored by .gitignore (default: respect .gitignore)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"CodeMapper version {__version__}",
    )
    parser.add_argument(
        "--docs",
        action="store_true",
        help="Generate documentation map (README + docs/) instead of full codemap",
    )
    parser.add_argument(
        "--docs-dir",
        metavar="DIR",
        help="Custom documentation directory to scan (default: docs/, wiki/, documentation/)",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        metavar="DIR",
        help=(
            "Exclude directory from output (repeatable). Always excluded: .git, .venv, .conda, node_modules, cache dirs"
        ),
    )
    parser.add_argument(
        "--output-dir",
        metavar="DIR",
        help=(
            "Output directory for generated files. "
            "Overrides config file. "
            "Supports ~ expansion. "
            "Default: .codemaps/ in current directory"
        ),
    )
    args = parser.parse_args()

    # Load user configuration
    user_config = load_user_config()

    if not args.input_path:
        parser.print_help()
        sys.exit(1)

    try:
        input_type, path = detect_input_type(args.input_path)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

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

    # Capture source with git info after we have directory_path
    source = capture_source(args.input_path, directory_path)

    if not os.path.isabs(args.input_path) and not args.input_path.startswith(("http://", "https://")):
        base_name = os.path.basename(os.path.abspath(args.input_path))
    else:
        base_name = os.path.basename(directory_path)

    gitignore_spec = load_gitignore_specs(directory_path)

    # Determine output directory based on CLI, config, and defaults
    output_dir = get_output_directory(args.output_dir, user_config)

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
            output_dir=output_dir,
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
            output_dir=output_dir,
        )

    with open(output_file_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file has been created: {output_file_path}")


if __name__ == "__main__":
    main()
