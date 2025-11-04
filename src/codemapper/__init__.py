"""
CodeMapper: A tool for generating comprehensive Markdown artifacts of
directory structures and file contents.

Package Structure:
- main.py: Entry point and CLI handling
- utils.py: Core functionality and helper functions
- config.py: Configuration constants and settings

This package provides functionality to analyze local directories or GitHub repositories,
creating detailed Markdown documentation of their structure and contents.
"""

from importlib.metadata import version

__version__ = version("codemapper")
