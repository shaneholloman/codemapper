
"""Configuration and constants for CodeMapper."""

ARCHIVE_EXTENSIONS = {
    ".zip", ".tar", ".gz", ".rar", ".7z", ".bz2", ".xz",
    ".tgz", ".tbz2", ".tar.gz", ".tar.bz2",
}

CODE_FENCE_MAP = {
    ".bat": "batch",
    ".c": "c",
    ".cfg": "ini",
    ".conf": "ini",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".css": "css",
    ".csv": "csv",
    ".dart": "dart",
    ".dockerfile": "dockerfile",
    ".go": "go",
    ".groovy": "groovy",
    ".h": "cpp",
    ".hbs": "handlebars",
    ".hcl": "hcl",
    ".hpp": "cpp",
    ".html": "html",
    ".ini": "ini",
    ".j2": "jinja2",
    ".java": "java",
    ".js": "javascript",
    ".json": "json",
    ".jsx": "jsx",
    ".kt": "kotlin",
    ".lua": "lua",
    ".log": "log",
    ".md": "markdown",
    ".php": "php",
    ".pl": "perl",
    ".pkl": "pickle",
    ".proto": "protobuf",
    ".ps1": "powershell",
    ".py": "python",
    ".r": "r",
    ".rb": "ruby",
    ".rs": "rust",
    ".scala": "scala",
    ".sh": "bash",
    ".sql": "sql",
    ".swift": "swift",
    ".tf": "hcl",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".txt": "text",
    ".vue": "vue",
    ".xml": "xml",
    ".yaml": "yml",
    ".yml": "yml",
    ".gitignore": "ini",
    "requirements.txt": "ini",
    "requirements.yml": "yml",
    "Dockerfile": "dockerfile",
    "Makefile": "makefile",
    "": "txt",  # Default fallback
}

LARGE_FILE_EXTENSIONS = {
    # Database files
    ".db", ".sqlite", ".sqlite3", ".dbf", ".mdb", ".accdb",
    ".sql", ".psql", ".dmp",
    # Image files
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".ico",
    ".svg", ".webp", ".eps", ".raw", ".cr2", ".nef",
    # Video files
    ".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm",
    ".vob", ".ogv",
    # Audio files
    ".mp3", ".wav", ".ogg", ".flac",
    # Document files
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".odt",
    # Archive files
    ".zip", ".tar", ".gz", ".rar", ".7z", ".bz2", ".xz",
    ".tgz", ".tbz2",
    # Executable files
    ".exe", ".msi", ".apk", ".app", ".dmg", ".iso", ".jar",
    ".deb", ".rpm",
    # Font files
    ".ttf", ".otf", ".woff", ".woff2", ".eot", ".fon",
    # Binary files
    ".bin", ".dll", ".so", ".dylib", ".dat", ".sav",
}