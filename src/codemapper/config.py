"""Configuration and constants for CodeMapper."""

import os
from dataclasses import dataclass
from pathlib import Path

import pathspec

# Standard documentation directory names to check
DOC_DIRECTORIES = {
    "docs",
    "wiki",
    "documentation",
}

# Output file suffixes
CODEMAP_SUFFIX = ".codemap.md"
DOCMAP_SUFFIX = ".docmap.md"

# Default prefix styles
PREFIX_STYLES = {
    "dot": ".codemaps",
    "underscore": "_codemaps",
    "dash": "-codemaps",
}


def load_user_config() -> dict:
    """Load user configuration from ~/.config/codemapper/config.toml."""
    config_locations = [
        Path.home() / ".config" / "codemapper" / "config.toml",
        Path.home() / ".codemapper.toml",
    ]

    for config_path in config_locations:
        if config_path.exists():
            try:
                import tomllib
            except ImportError:
                try:
                    import tomli as tomllib
                except ImportError:
                    # If no TOML parser available, return empty config
                    return {}

            with open(config_path, "rb") as f:
                return tomllib.load(f)

    return {}


def get_output_directory(
    cli_output_dir: str | None = None,
    config: dict | None = None,
) -> str:
    """
    Determine the output directory based on CLI args, config, and defaults.

    Precedence: CLI flag > Config file > Default (.codemaps in CWD)

    Args:
        cli_output_dir: Output directory from CLI --output-dir flag
        config: Loaded configuration dictionary

    Returns:
        str: The output directory path to use
    """
    # CLI flag has highest priority
    if cli_output_dir:
        return os.path.expanduser(cli_output_dir)

    # Check config file
    if config and "output_dir" in config:
        return os.path.expanduser(config["output_dir"])

    # Default: use prefix_style from config or default to "dot"
    prefix_style = "dot"
    if config and "prefix_style" in config:
        prefix_style = config.get("prefix_style", "dot")

    directory_name = PREFIX_STYLES.get(prefix_style, PREFIX_STYLES["dot"])
    return os.path.join(".", directory_name)


@dataclass
class BaseMapConfig:
    """Base configuration class for mapping generation.

    This class holds the common parameters needed for generating maps.
    It serves as a base class for specific mapping configurations.

    Attributes:
        directory_path (str): The path to the directory being mapped
        gitignore_spec (pathspec.PathSpec): Gitignore specifications to follow
        include_ignored (bool): Whether to include ignored files, defaults to False
        source (str): Source information string, defaults to empty string
        base_name (str): Base name for documentation, defaults to empty string
        exclude_dirs (Optional[List[str]]): List of directories to exclude, defaults to None
    """

    directory_path: str
    gitignore_spec: pathspec.PathSpec
    include_ignored: bool = False
    source: str = ""
    base_name: str = ""
    exclude_dirs: list[str] | None = None


ARCHIVE_EXTENSIONS = {
    ".zip",
    ".tar",
    ".gz",
    ".rar",
    ".7z",
    ".bz2",
    ".xz",
    ".tgz",
    ".tbz2",
    ".tar.gz",
    ".tar.bz2",
}

# System and temporary files to always exclude
SYSTEM_FILES = {
    ".DS_Store",
    "Thumbs.db",
    "desktop.ini",
    ".localized",
    ".Spotlight-V100",
    ".Trashes",
    ".fseventsd",
    ".TemporaryItems",
    ".DocumentRevisions-V100",
    ".VolumeIcon.icns",
    "thumbs.db",
    "ehthumbs.db",
    "._.DS_Store",
}

CODE_FENCE_MAP = {
    ".adoc": "asciidoc",
    ".astro": "astro",
    ".bat": "batch",
    ".c": "c",
    ".cfg": "ini",
    ".clj": "clojure",
    ".conf": "ini",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".css": "css",
    ".csv": "csv",
    ".dart": "dart",
    ".dockerfile": "dockerfile",
    ".elixir": "elixir",
    ".elm": "elm",
    ".ex": "elixir",
    ".exs": "elixir",
    ".go": "go",
    ".graphql": "graphql",
    ".groovy": "groovy",
    ".h": "cpp",
    ".hbs": "handlebars",
    ".hcl": "hcl",
    ".hpp": "cpp",
    ".htm": "html",
    ".html": "html",
    ".ini": "ini",
    ".j2": "jinja2",
    ".java": "java",
    ".js": "javascript",
    ".json": "json",
    ".json5": "json5",
    ".jsonc": "jsonc",
    ".jsx": "jsx",
    ".kt": "kotlin",
    ".lock": "text",
    ".lua": "lua",
    ".log": "log",
    ".md": "markdown",
    ".mdx": "markdown",
    ".mjs": "javascript",
    ".php": "php",
    ".pl": "perl",
    ".pkl": "pickle",
    ".proto": "protobuf",
    ".ps1": "powershell",
    ".py": "python",
    ".r": "r",
    ".rb": "ruby",
    ".rs": "rust",
    ".sass": "sass",
    ".scala": "scala",
    ".scss": "scss",
    ".sh": "bash",
    ".sql": "sql",
    ".svelte": "svelte",
    ".swift": "swift",
    ".tf": "hcl",
    ".toml": "toml",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".txt": "text",
    ".vue": "vue",
    ".xml": "xml",
    ".yaml": "yml",
    ".yml": "yml",
    ".zig": "zig",
    ".gitignore": "ini",
    ".dockerignore": "ini",
    ".env": "bash",
    ".env.example": "bash",
    ".prettierrc": "json",
    ".eslintrc": "json",
    "requirements.txt": "ini",
    "requirements.yml": "yml",
    "Dockerfile": "dockerfile",
    "Makefile": "makefile",
    "Cargo.toml": "toml",
    "Cargo.lock": "toml",
    "package.json": "json",
    "package-lock.json": "json",
    "tsconfig.json": "json",
    "": "txt",  # Default fallback
}

# Maximum file size in characters for content inclusion (~75k tokens = ~300k chars)
MAX_FILE_SIZE_CHARS = 300000

LARGE_FILE_EXTENSIONS = {
    # Database files
    ".db",
    ".sqlite",
    ".sqlite3",
    ".dbf",
    ".mdb",
    ".accdb",
    ".sql",
    ".psql",
    ".dmp",
    # Log and temp files
    ".log",
    ".logs",
    ".tmp",
    ".temp",
    ".cache",
    ".bak",
    ".backup",
    ".old",
    ".swp",
    ".swo",
    # Image files
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".ico",
    ".svg",
    ".webp",
    ".eps",
    ".raw",
    ".cr2",
    ".nef",
    # Video files
    ".mp4",
    ".avi",
    ".mov",
    ".wmv",
    ".flv",
    ".mkv",
    ".webm",
    ".vob",
    ".ogv",
    # Audio files
    ".mp3",
    ".wav",
    ".ogg",
    ".flac",
    # Document files
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".odt",
    # Archive files
    ".zip",
    ".tar",
    ".gz",
    ".rar",
    ".7z",
    ".bz2",
    ".xz",
    ".tgz",
    ".tbz2",
    # Executable files
    ".exe",
    ".msi",
    ".apk",
    ".app",
    ".dmg",
    ".iso",
    ".jar",
    ".deb",
    ".rpm",
    # Font files
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
    ".eot",
    ".fon",
    # Binary files
    ".bin",
    ".dll",
    ".so",
    ".dylib",
    ".dat",
    ".sav",
}
