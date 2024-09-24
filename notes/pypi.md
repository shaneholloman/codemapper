# Complete Step-by-Step Guide: Publishing CodeMapper to PyPI

This guide provides a detailed, step-by-step process for converting the CodeMapper repository for PyPI publication and the entire PyPI publication process, including branching strategies.

## Table of Contents

- [Complete Step-by-Step Guide: Publishing CodeMapper to PyPI](#complete-step-by-step-guide-publishing-codemapper-to-pypi)
  - [Table of Contents](#table-of-contents)
  - [7. Local Testing](#7-local-testing)
  - [8. Building the Package](#8-building-the-package)
  - [9. Publishing to PyPI](#9-publishing-to-pypi)
  - [10. Post-Publication Steps](#10-post-publication-steps)
  - [11. Updating the Package](#11-updating-the-package)
  - [12. Troubleshooting](#12-troubleshooting)

## 7. Local Testing

7.1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

7.2. Install the package locally:

```bash
pip install -e .
```

7.3. Test the package:

```bash
codemapper /path/to/test/directory
```

7.4. If any issues arise, fix them and repeat steps 7.2 and 7.3

## 8. Building the Package

8.1. Install build tools:

```bash
pip install --upgrade setuptools wheel twine
```

8.2. Build the package:

```bash
python setup.py sdist bdist_wheel
```

## 9. Publishing to PyPI

9.1. Upload the package to PyPI:

```bash
python -m twine upload dist/*
```

9.2. Enter your PyPI credentials when prompted.

9.3. Verify the package is available on PyPI by visiting <https://pypi.org/project/codemapper/>

## 10. Post-Publication Steps

10.1. Commit your changes:

```bash
git add .
git commit -m "Prepare CodeMapper for PyPI publication"
```

10.2. Push the branch to GitHub:

```bash
git push -u origin pypi-prep
```

10.3. Create a pull request on GitHub:

- Go to your repository on GitHub
- Click "Compare & pull request"
- Review the changes and create the pull request

10.4. Merge the pull request:

- After review, click "Merge pull request"
- Confirm the merge

10.5. Switch back to the main branch and pull changes:

```bash
git checkout main
git pull origin main
```

10.6. Create a new release on GitHub:

- Go to your repository on GitHub
- Click "Releases" > "Create a new release"
- Tag version: v3.2.1
- Release title: CodeMapper 3.2.1
- Describe the release and click "Publish release"

## 11. Updating the Package

When you need to update the package:

11.1. Create a new branch for the update:

```bash
git checkout -b update-vX.X.X
```

11.2. Make necessary changes to your code.

11.3. Update the version number in `setup.py` and `src/codemapper/__init__.py`.

11.4. Commit the changes:

```bash
git add .
git commit -m "Update to version X.X.X"
```

11.5. Push the branch and create a pull request as in steps 10.2-10.4.

11.6. After merging, checkout and pull the main branch:

```bash
git checkout main
git pull origin main
```

11.7. Rebuild the package:

I typically delete to the old build files before rebuilding.

```bash
python setup.py sdist bdist_wheel
```

11.8. Upload the new version:

```bash
python -m twine upload dist/*
```

11.9. Create a new release on GitHub as in step 10.6.

## 12. Troubleshooting

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
