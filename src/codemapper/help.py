"""Help text and descriptions for CodeMapper CLI."""

DESCRIPTION = """Generate comprehensive Markdown codemaps from local directories or GitHub repositories.

CodeMapper creates single-file Markdown documents containing:
  - Complete directory tree structure
  - All file contents with syntax highlighting
  - Git metadata (branch, commit, remote)

Output: project.codemap.md or project.docmap.md
Default location: .codemaps/ in current directory
Config file: ~/.codemapper/codemapper.toml (optional)"""

EPILOG = """Examples:
  codemapper /path/to/project
  codemapper https://github.com/user/repo
  codemapper --docs /path/to/project
  codemapper --output-dir ~/all-codemaps /path/to/project
  codemapper --exclude=tests --exclude=docs /path/to/project

Configuration:
  Create ~/.codemapper/codemapper.toml to set defaults:
    output_dir = "~/.codemapper"  # Centralized collection
    prefix_style = "underscore"    # Use _codemaps/ instead of .codemaps/

Precedence: CLI flags > Config file > Defaults

For more info: https://github.com/shaneholloman/codemapper"""

ARG_HELP = {
    "input_path": "Local directory path or GitHub repository URL to process",
    "include_ignored": "Include files normally ignored by .gitignore (default: respect .gitignore)",
    "docs": "Generate documentation map (README + docs/) instead of full codemap",
    "docs_dir": "Custom documentation directory to scan (default: docs/, wiki/, documentation/)",
    "exclude": (
        "Exclude directory from output (repeatable). Always excluded: .git, .venv, .conda, node_modules, cache dirs"
    ),
    "output_dir": (
        "Output directory for generated files. "
        "Overrides config file. "
        "Supports ~ expansion. "
        "Default: .codemaps/ in current directory"
    ),
}
