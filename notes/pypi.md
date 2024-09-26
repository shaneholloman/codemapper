# Publishing CodeMapper to PyPI

How to prepare the CodeMapper project for publication on PyPI, including testing, building the package, publishing to PyPI, and updating the package.

## Table of Contents

- [Publishing CodeMapper to PyPI](#publishing-codemapper-to-pypi)
  - [Table of Contents](#table-of-contents)
  - [Local Testing](#local-testing)
  - [Building the Package](#building-the-package)
  - [Publishing to PyPI](#publishing-to-pypi)
  - [Post-Publication Steps](#post-publication-steps)
  - [Updating the Package](#updating-the-package)
  - [Troubleshooting](#troubleshooting)

## Local Testing

Sometime you just want to run the script locally to test it before publishing it to PyPI. Here's how you can do that:

Easy and fast way:

```sh
python -m codemapper.codemapper https://github.com/shaneholloman/claude-sync
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
codemapper /path/to/test/directory
```

If any issues arise, fix them and repeat steps 7.2 and 7.3

## Building the Package

Install build tools:

```bash
pip install --upgrade setuptools wheel twine
```

Build the package:

```bash
python setup.py sdist bdist_wheel
```

## Publishing to PyPI

Upload the package to PyPI:

```bash
python -m twine upload dist/*
```

Enter your PyPI credentials when prompted.

Verify the package is available on PyPI by visiting <https://pypi.org/project/codemapper/>

## Post-Publication Steps

Commit your changes:

```bash
git add .
git commit -m "Prepare CodeMapper for PyPI publication"
```

Push the branch to GitHub:

```bash
git push -u origin pypi-prep
```

Create a pull request on GitHub:

- Go to your repository on GitHub
- Click "Compare & pull request"
- Review the changes and create the pull request

Merge the pull request:

- After review, click "Merge pull request"
- Confirm the merge

Switch back to the main branch and pull changes:

```bash
git checkout main
git pull origin main
```

Create a new release on GitHub:

- Go to your repository on GitHub
- Click "Releases" > "Create a new release"
- Tag version: v3.2.1
- Release title: CodeMapper 3.2.1
- Describe the release and click "Publish release"

## Updating the Package

When you need to update the package:

Create a new branch for the update:

```bash
git checkout -b update-vX.X.X
```

Make necessary changes to your code.

Update the version number in `setup.py` and `src/codemapper/__init__.py`.

Commit the changes:

```bash
git add .
git commit -m "Update to version X.X.X"
```

Push the branch and create a pull request as in steps 10.2-10.4.

After merging, checkout and pull the main branch:

```bash
git checkout main
git pull origin main
```

Rebuild the package:

I typically delete to the old build files before rebuilding.

```bash
python setup.py sdist bdist_wheel
```

Upload the new version:

```bash
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

---

By following this detailed guide, you should be able to successfully prepare your CodeMapper project for PyPI, publish it, and manage updates. Always remember to increment the version number for each new release and keep your README and documentation up to date.
