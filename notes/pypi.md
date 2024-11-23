# Publishing CodeMapper to PyPI

Instructions to prepare and publish the CodeMapper project to PyPI using `pyproject.toml`.

## Table of Contents

- [Publishing CodeMapper to PyPI](#publishing-codemapper-to-pypi)
  - [Table of Contents](#table-of-contents)
  - [Local Testing](#local-testing)
  - [Testing from Source Directory](#testing-from-source-directory)
  - [Building the Package](#building-the-package)
  - [Troubleshooting](#troubleshooting)

## Local Testing

To test the package locally before publishing to PyPI:

1. Create a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the package locally:

    ```sh
    pip install -e .
    ```

3. Test the package:

    ```sh
    codemapper /path/to/test/directory_or_GITHUB-REPO-URL
    ```

## Testing from Source Directory

To test the `codemapper` directly from the source directory:

1. Set the `PYTHONPATH` to the `src` directory and run the `codemapper` module:

    ```sh
    PYTHONPATH=src python -m codemapper.main <path_to_directory_or_github_url>
    ```

2. Example to run `codemapper` in the current directory:

    ```sh
    set PYTHONPATH=src && python -m codemapper.main .
    ```

## Building the Package

1. Install build tools:

    ```sh
    pip install --upgrade setuptools wheel build twine
    ```

2. Build the package:

    ```sh
    # before doing ensure
    # 1. update version in pyproject.toml
    # 2. update changelog.md
    python -m build
    ```

    This will generate distribution files in the `dist` directory.

3. Upload the package to PyPI:

    ```sh
    python -m twine upload dist/*
    ```

4. Update the package:

    ```sh
    pip install --upgrade codemapper
    ```

## Troubleshooting

- **FileNotFoundError: [Errno 2] No such file or directory: 'README.md'**:
  - Ensure `README.md` is in the same directory as `pyproject.toml`.
  - Check your current working directory.

- **HTTPError: 400 Client Error: File already exists**:
  - You cannot overwrite an existing version on PyPI.
  - Increment the version number in `pyproject.toml` and try again.

- **ImportError: No module named 'codemapper'**:
  - Ensure the package is installed correctly: `pip install -e .`
  - Check if you're in the correct virtual environment.

- **Permission denied when uploading to PyPI**:
  - Verify your PyPI credentials.
  - Ensure you have the necessary permissions to upload the package.

- **Package not found on PyPI after upload**:
  - Wait a few minutes, as it can take some time for the package to appear.
  - Double-check the package name and version on PyPI.

Remember to always test your package locally in a fresh virtual environment before uploading to PyPI. This ensures that your package works as expected when installed by other users.
