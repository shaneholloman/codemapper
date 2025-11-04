"""Type definitions and dataclasses for CodeMapper."""

from dataclasses import dataclass

import pathspec


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
        exclude_dirs (list[str] | None): List of directories to exclude, defaults to None
    """

    directory_path: str
    gitignore_spec: pathspec.PathSpec
    include_ignored: bool = False
    source: str = ""
    base_name: str = ""
    exclude_dirs: list[str] | None = None


@dataclass
class CodeMapConfig(BaseMapConfig):
    """Configuration class for code mapping generation.

    Inherits from BaseMapConfig to provide configuration for code mapping.
    See BaseMapConfig for documentation of inherited attributes.
    """


@dataclass
class DocMapConfig(BaseMapConfig):
    """Configuration class for document mapping generation.

    Inherits from BaseMapConfig to provide configuration for documentation mapping.
    See BaseMapConfig for documentation of inherited attributes.

    Additional Attributes:
        doc_dir (str | None): Custom documentation directory, defaults to None
    """

    doc_dir: str | None = None
