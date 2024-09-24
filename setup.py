"""
Setup script for CodeMapper package.

This script provides the necessary configuration for packaging and distributing
the CodeMapper tool via PyPI.
"""

import os
import re
from setuptools import setup, find_packages


def get_version():
    """
    Retrieve the package version from __init__.py file.

    Returns:
        str: The package version string.

    Raises:
        RuntimeError: If unable to find the version string.
    """
    init_py = os.path.join(os.path.dirname(__file__), "src", "codemapper", "__init__.py")
    with open(init_py, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError(f"Unable to find version string in {init_py}.")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="codemapper",
    version=get_version(),
    author="Shane Holloman",
    author_email="shaneholloman@gmail.com",
    description="A tool to generate comprehensive Markdown artifacts "
    "of directory structures and file contents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaneholloman/codemapper",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    install_requires=[
        "chardet",
        "pathspec",
    ],
    entry_points={
        "console_scripts": [
            "codemapper=codemapper.codemapper:main",
        ],
    },
)
