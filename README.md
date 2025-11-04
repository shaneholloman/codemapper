# CodeMapper

> Converts codebases/docs into single-file Markdown documents for language model context and code analysis.

## What It Does

CodeMapper scans a directory or GitHub repository and generates a comprehensive Markdown file containing:

- Complete directory tree structure
- All file contents with syntax highlighting
- Git metadata (branch, commit, remote)

Files are filtered intelligently - binary files, lock files, cache directories, and files over 300k characters are excluded.

## Installation

```bash
uv tool install codemapper
```

## Basic Usage

```bash
# Generate codemap from local directory
codemapper /path/to/project

# Generate codemap from GitHub repository
codemapper https://github.com/user/repo

# Generate documentation map (README + docs/ only)
codemapper --docs /path/to/project
```

## Output

By default, CodeMapper creates `.codemaps/` in your current directory:

- `project.codemap.md` - Full codebase map
- `project.docmap.md` - Documentation-only map (with --docs flag)

## Options

```bash
--docs                    Generate documentation map instead of code map
--docs-dir DIR            Specify custom documentation directory
--exclude DIR             Exclude directory (can be used multiple times)
--output-dir DIR          Custom output directory (overrides config)
--include-ignored         Include files normally ignored by .gitignore
--version                 Show version
--help                    Show help
```

## Configuration

> [!IMPORTANT]
> Without setting codemapper defaults, it will make `.codemaps/` in the current directory. Which is a sane default for projects.

### Optional Configuration

Copy `codemapper.example.toml` to `~/.codemapper/codemapper.toml` for optional configuration:

```toml
# Or, centralized collection: All codemaps can go to one directory
output_dir = "~/.codemapper"

# OR custom prefix: Change directory name in current location
# prefix_style = "dot"        # .codemaps/ (default)
# prefix_style = "underscore" # _codemaps/
# prefix_style = "dash"       # -codemaps/
```

**Precedence:** CLI `--output-dir` > Config `output_dir` > Config `prefix_style` > Default (`.codemaps/` in current directory)

**Without config:** Creates `.codemaps/` where you run the command (project-level management)

**With `output_dir` set:** All codemaps go to one centralized location (system-level management)

## What Gets Excluded

**Always excluded:**

- `.git/`, `.venv/`, `.conda/`, `node_modules/`
- Cache directories: `.ruff_cache/`, `.pytest_cache/`, `__pycache__/`, etc.
- System files: `.DS_Store`, `Thumbs.db`
- Lock files: `uv.lock`, `package-lock.json`, `yarn.lock`, etc.
- Archive files: `.zip`, `.tar`, `.gz`, etc.
- Binary files: images, videos, executables, etc.
- Files over 300k characters (too large for AI context)

**Respects .gitignore** unless `--include-ignored` flag is used.

## Requirements

Python 3.12 or newer

## License

MIT
