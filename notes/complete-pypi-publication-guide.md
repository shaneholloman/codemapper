# Complete Step-by-Step Guide: Publishing CodeMapper to PyPI

This guide provides a detailed, step-by-step process for converting the CodeMapper repository for PyPI publication and the entire PyPI publication process, including branching strategies.

## Table of Contents

- [Complete Step-by-Step Guide: Publishing CodeMapper to PyPI](#complete-step-by-step-guide-publishing-codemapper-to-pypi)
  - [Table of Contents](#table-of-contents)
  - [1. Initial Setup](#1-initial-setup)
  - [2. Creating a PyPI Account](#2-creating-a-pypi-account)
  - [3. Branching for PyPI Preparation](#3-branching-for-pypi-preparation)
  - [4. Restructuring the Project](#4-restructuring-the-project)
  - [5. Creating and Updating Necessary Files](#5-creating-and-updating-necessary-files)
  - [6. Updating the Main Script](#6-updating-the-main-script)
  - [7. Local Testing](#7-local-testing)
  - [8. Building the Package](#8-building-the-package)
  - [9. Publishing to PyPI](#9-publishing-to-pypi)
  - [10. Post-Publication Steps](#10-post-publication-steps)
  - [11. Updating the Package](#11-updating-the-package)
  - [12. Troubleshooting](#12-troubleshooting)

## 1. Initial Setup

1.1. Ensure git is installed:

```bash
git --version
```

1.2. If not installed, install git:

- For Ubuntu/Debian: `sudo apt-get install git`
- For macOS: Install Xcode Command Line Tools
- For Windows: Download and install from git-scm.com

1.3. Configure git (if not already done):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

1.4. Clone your repository (if not already done):

```bash
git clone https://github.com/shaneholloman/codemapper.git
cd codemapper
```

## 2. Creating a PyPI Account

2.1. Go to <https://pypi.org> and click on "Register".

2.2. Fill out the registration form with your details.

2.3. Verify your email address by clicking the link sent to your email.

2.4. Enable two-factor authentication (2FA) for added security:

- Go to your account settings
- Click on "Add 2FA"
- Follow the prompts to set up 2FA using an authenticator app

## 3. Branching for PyPI Preparation

3.1. Ensure you're on the main branch and it's up to date:

```bash
git checkout main
git pull origin main
```

3.2. Create a new branch for PyPI preparation:

```bash
git checkout -b pypi-prep
```

3.3. Verify you're on the new branch:

```bash
git branch
```

## 4. Restructuring the Project

4.1. Create the new directory structure:

```bash
mkdir -p src/codemapper tests
```

4.2. Move the main script:

```bash
mv codemapper.py src/codemapper/
```

4.3. Create an empty test file:

```bash
touch tests/test_codemapper.py
```

## 5. Creating and Updating Necessary Files

5.1. Create `src/codemapper/__init__.py`:

```bash
echo "from .codemapper import main

__version__ = \"3.2.1\"" > src/codemapper/__init__.py
```

5.2. Create `setup.py`:

```bash
cat << EOF > setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="codemapper",
    version="3.2.1",
    author="Shane Holloman",
    author_email="your.email@example.com",
    description="A tool to generate comprehensive Markdown artifacts of directory structures and file contents",
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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
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
EOF
```

5.3. Create `pyproject.toml`:

```bash
cat << EOF > pyproject.toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 100
target-version = ['py36', 'py37', 'py38', 'py39']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''
EOF
```

5.4. Update `README.md` to include PyPI installation and usage instructions:

```bash
cat << EOF >> README.md

## Installation

You can install CodeMapper using pip:

\`\`\`bash
pip install codemapper
\`\`\`

## Usage

After installation, you can use CodeMapper from the command line:

\`\`\`bash
codemapper <path_to_directory_or_github_url> [--include-ignored]
\`\`\`

For more information, please refer to the full documentation.
EOF
```

## 6. Updating the Main Script

TODO:

6.1. Update `src/codemapper/codemapper.py` to handle paths correctly:

- Open the file in your preferred text editor
- Replace relative path references with `os.path.join(os.getcwd(), ...)`
- Ensure all file operations use absolute paths

6.2. Create `src/codemapper/__main__.py`:

```bash
echo "from .codemapper import main

if __name__ == \"__main__\":
    main()" > src/codemapper/__main__.py
```

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
