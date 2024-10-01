# Publishing CodeMapper to PyPI

How to prepare the CodeMapper project for publication on PyPI, including testing, building the package, publishing to PyPI, and updating the package.

## Table of Contents

- [Publishing CodeMapper to PyPI](#publishing-codemapper-to-pypi)
  - [Table of Contents](#table-of-contents)
  - [Local Testing](#local-testing)
  - [Building the Package](#building-the-package)
  - [Troubleshooting](#troubleshooting)

## Local Testing

Sometime you just want to run the script locally to test it before publishing it to PyPI. Here's how you can do that:

Easy and fast way:

```sh
python -m src.codemapper.codemapper https://github.com/shaneholloman/claude-sync
```

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the package locally:

```bash
pip install -e .
```

Test the package:

```bash
codemapper /path/to/test/directory or URL
```

If any issues arise, fix them and repeat steps 7.2 and 7.3

## Building the Package

Install build tools:

```bash
pip install --upgrade setuptools wheel twine build installer
```

Rebuild the package:

I typically delete to the old build files before rebuilding.

```bash
python -m build
```

Upload the new version:

```bash
# have you pypi credentials ready
python -m twine upload dist/*
```

```sh
# pip install the latest version
pip install --upgrade codemapper
```

Create a new release on GitHub as in step 10.6.

## Troubleshooting

- **FileNotFoundError: [Errno 2] No such file or directory: 'README.md'**:
  - Ensure README.md is in the same directory as setup.py.
  - Check your current working directory.

- **HTTPError: 400 Client Error: File already exists**:
  - You cannot overwrite an existing version on PyPI.
  - Increment the version number and try again.

- **ImportError: No module named 'codemapper'**:
  - Ensure the package is installed correctly: `pip install -e .`
  - Check if you're in the correct virtual environment.

- **Permission denied when uploading to PyPI**:
  - Verify your PyPI credentials.
  - Ensure you have the necessary permissions to upload the package.
  - Check if your 2FA token is correct (if 2FA is enabled).

- **Package not found on PyPI after upload**:
  - Wait a few minutes, as it can take some time for the package to appear.
  - Double-check the package name and version on PyPI.

Remember to always test your package locally in a fresh virtual environment before uploading to PyPI. This ensures that your package works as expected when installed by other users.
