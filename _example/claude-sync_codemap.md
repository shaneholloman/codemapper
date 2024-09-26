# claude-sync

> CodeMap Source: GitHub repository: <https://github.com/shaneholloman/claude-sync>

This markdown document provides a comprehensive overview of the directory structure and file contents. It aims to give viewers (human or AI) a complete view of the codebase in a single file for easy analysis.

## Document Table of Contents

The table of contents below is for navigational convenience and reflects this document's structure, not the actual file structure of the repository.

<!-- TOC -->

- [claude-sync](#claude-sync)
  - [Document Table of Contents](#document-table-of-contents)
  - [Repo File Tree](#repo-file-tree)
  - [Repo File Contents](#repo-file-contents)
    - [README.md](#readmemd)
    - [.gitignore](#gitignore)
    - [.github/FUNDING.yml](#githubfundingyml)
    - [.github/ISSUE\_TEMPLATE/bug\_report.yml](#githubissue_templatebug_reportyml)
    - [.github/ISSUE\_TEMPLATE/feature\_request.yml](#githubissue_templatefeature_requestyml)
    - [.github/workflows/close-stale-issues-and-prs.yml](#githubworkflowsclose-stale-issues-and-prsyml)
    - [.github/workflows/python-package.yml](#githubworkflowspython-packageyml)
    - [.github/workflows/python-publish.yml](#githubworkflowspython-publishyml)
    - [claudesync.gif](#claudesyncgif)
    - [CODEOWNERS](#codeowners)
    - [CONTRIBUTING.md](#contributingmd)
    - [LICENSE](#license)
    - [pyproject.toml](#pyprojecttoml)
    - [pytest.ini](#pytestini)
    - [requirements.txt](#requirementstxt)
    - [SECURITY.md](#securitymd)
    - [setup.py](#setuppy)
    - [src/claudesync/init.py](#srcclaudesyncinitpy)
    - [src/claudesync/chat\_sync.py](#srcclaudesyncchat_syncpy)
    - [src/claudesync/cli/init.py](#srcclaudesynccliinitpy)
    - [src/claudesync/cli/auth.py](#srcclaudesynccliauthpy)
    - [src/claudesync/cli/category.py](#srcclaudesyncclicategorypy)
    - [src/claudesync/cli/chat.py](#srcclaudesyncclichatpy)
    - [src/claudesync/cli/config.py](#srcclaudesynccliconfigpy)
    - [src/claudesync/cli/file.py](#srcclaudesyncclifilepy)
    - [src/claudesync/cli/main.py](#srcclaudesyncclimainpy)
    - [src/claudesync/cli/organization.py](#srcclaudesynccliorganizationpy)
    - [src/claudesync/cli/project.py](#srcclaudesynccliprojectpy)
    - [src/claudesync/cli/submodule.py](#srcclaudesyncclisubmodulepy)
    - [src/claudesync/cli/sync.py](#srcclaudesyncclisyncpy)
    - [src/claudesync/compression.py](#srcclaudesynccompressionpy)
    - [src/claudesync/configmanager/init.py](#srcclaudesyncconfigmanagerinitpy)
    - [src/claudesync/configmanager/base\_config\_manager.py](#srcclaudesyncconfigmanagerbase_config_managerpy)
    - [src/claudesync/configmanager/file\_config\_manager.py](#srcclaudesyncconfigmanagerfile_config_managerpy)
    - [src/claudesync/configmanager/inmemory\_config\_manager.py](#srcclaudesyncconfigmanagerinmemory_config_managerpy)
    - [src/claudesync/exceptions.py](#srcclaudesyncexceptionspy)
    - [src/claudesync/provider\_factory.py](#srcclaudesyncprovider_factorypy)
    - [src/claudesync/providers/init.py](#srcclaudesyncprovidersinitpy)
    - [src/claudesync/providers/base\_claude\_ai.py](#srcclaudesyncprovidersbase_claude_aipy)
    - [src/claudesync/providers/base\_provider.py](#srcclaudesyncprovidersbase_providerpy)
    - [src/claudesync/providers/claude\_ai.py](#srcclaudesyncprovidersclaude_aipy)
    - [src/claudesync/session\_key\_manager.py](#srcclaudesyncsession_key_managerpy)
    - [src/claudesync/syncmanager.py](#srcclaudesyncsyncmanagerpy)
    - [src/claudesync/utils.py](#srcclaudesyncutilspy)
    - [tests/logging\_test\_case.py](#testslogging_test_casepy)
    - [tests/mock\_http\_server.py](#testsmock_http_serverpy)
    - [tests/test\_chat\_happy\_path.py](#teststest_chat_happy_pathpy)
    - [tests/test\_claude\_ai.py](#teststest_claude_aipy)
    - [tests/test\_happy\_path.py](#teststest_happy_pathpy)

<!-- /TOC -->

## Repo File Tree

This file tree represents the actual structure of the repository. It's crucial for understanding the organization of the codebase.

```tree
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   └── feature_request.yml
│   ├── workflows/
│   │   ├── close-stale-issues-and-prs.yml
│   │   ├── python-package.yml
│   │   └── python-publish.yml
│   └── FUNDING.yml
├── src/
│   └── claudesync/
│       ├── cli/
│       │   ├── __init__.py
│       │   ├── auth.py
│       │   ├── category.py
│       │   ├── chat.py
│       │   ├── config.py
│       │   ├── file.py
│       │   ├── main.py
│       │   ├── organization.py
│       │   ├── project.py
│       │   ├── submodule.py
│       │   └── sync.py
│       ├── configmanager/
│       │   ├── __init__.py
│       │   ├── base_config_manager.py
│       │   ├── file_config_manager.py
│       │   └── inmemory_config_manager.py
│       ├── providers/
│       │   ├── __init__.py
│       │   ├── base_claude_ai.py
│       │   ├── base_provider.py
│       │   └── claude_ai.py
│       ├── __init__.py
│       ├── chat_sync.py
│       ├── compression.py
│       ├── exceptions.py
│       ├── provider_factory.py
│       ├── session_key_manager.py
│       ├── syncmanager.py
│       └── utils.py
├── tests/
│   ├── logging_test_case.py
│   ├── mock_http_server.py
│   ├── test_chat_happy_path.py
│   ├── test_claude_ai.py
│   └── test_happy_path.py
├── .gitignore
├── CODEOWNERS
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── claudesync.gif
├── pyproject.toml
├── pytest.ini
├── requirements.txt
└── setup.py

9 directories, 49 files
```

## Repo File Contents

The following sections present the content of each file in the repository. Large and binary files are acknowledged but their contents are not displayed.

### SECURITY.md

````markdown
# Security Policy

## Reporting Vulnerabilities

We take security seriously and appreciate your help in keeping **claudesync** secure. If you discover a security vulnerability, please follow these guidelines:

1. **Public Disclosure:** If the issue can be safely disclosed, feel free to [open an issue](https://github.com/jahwag/claudesync/issues).

2. **Private Disclosure:** If the issue should not be made public, please contact me directly via DM on Discord:
    - **Discord:** [@jahwag](https://discord.gg/pR4qeMH4u4)
````

### setup.py

```python
from setuptools import setup, find_packages

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
```

### pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
addopts = -v --cov=claudesync --cov-report=term-missing
```

### .gitignore

```ini
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.idea

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

**/*.egg-info
__pycache__

# claude
claude.sync
config.json
claudesync.log
claude_chats
some_value
.claudesync

ROADMAP.md
```

### claudesync.gif

```txt
[Large or binary file detected. File Type: image/gif, Size: 19584 bytes]
```

### CODEOWNERS

```txt
# Default owner for everything in the repo
*       @jahwag
```

### README.md

````markdown
[Error reading file: 'ascii' codec can't decode byte 0xe2 in position 1061: ordinal not in range(128)]
````

### pyproject.toml

```txt
[project]
name = "claudesync"
version = "0.6.1"
authors = [
    {name = "Jahziah Wagner", email = "540380+jahwag@users.noreply.github.com"},
]
description = "A tool to synchronize local files with Claude.ai projects"
license = {file = "LICENSE"}
readme = "README.md"
requires-python = ">=3.10"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "click>=8.1.7",
    "click_completion>=0.5.2",
    "pathspec>=0.12.1",
    "pytest>=8.3.2",
    "python_crontab>=3.2.0",
    "setuptools>=73.0.1",
    "sseclient_py>=1.8.0",
    "tqdm>=4.66.5",
    "pytest-cov>=5.0.0",
    "claudesync>=0.5.4",
    "crontab>=1.0.1",
    "python-crontab>=3.2.0",
    "Brotli>=1.1.0",
    "anthropic>=0.34.2",
    "cryptography>=3.4.7",
]
keywords = [
    "sync",
    "files",
    "Claude.ai",
    "automation",
    "synchronization",
    "project management",
    "file management",
    "cloud sync",
    "cli tool",
    "command line",
    "productivity",
    "development tools",
    "file synchronization",
    "continuous integration",
    "devops",
    "version control"
]

[project.optional-dependencies]
test = [
    "pytest>=8.2.2",
    "pytest-cov>=5.0.0",
]

[project.urls]
"Homepage" = "https://github.com/jahwag/claudesync"
"Bug Tracker" = "https://github.com/jahwag/claudesync/issues"

[project.scripts]
claudesync = "claudesync.cli.main:cli"

[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
include = ["claudesync*"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
addopts = "-v --cov=claudesync --cov-report=term-missing"
```

### requirements.txt

```ini
click>=8.1.7
click_completion>=0.5.2
pathspec>=0.12.1
pytest>=8.3.2
python_crontab>=3.2.0
setuptools>=73.0.1
sseclient_py>=1.8.0
tqdm>=4.66.5
pytest-cov>=5.0.0
claudesync>=0.5.4
crontab>=1.0.1
python-crontab>=3.2.0
Brotli>=1.1.0
anthropic>=0.34.2
cryptography>=3.4.7
```

### CONTRIBUTING.md

````markdown
# Contributing to ClaudeSync

We're excited that you're interested in contributing to ClaudeSync! This document outlines the process for contributing to this project.

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```
   git clone https://github.com/your-username/claudesync.git
   ```
3. Create a new branch for your feature or bug fix:
   ```
   git checkout -b feature/your-feature-name
   ```

## Setting Up the Development Environment

1. Ensure you have Python 3.6 or later installed.
2. Install the development dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Install the package in editable mode:
   ```
   pip install -e .
   ```

## Making Changes

1. Make your changes in your feature branch.
2. Add or update tests as necessary.
3. Run the tests to ensure they pass:
   ```
   python -m unittest discover tests
   ```
4. Update the documentation if you've made changes to the API or added new features.

## Submitting Changes

1. Commit your changes:
   ```
   git commit -am "Add a brief description of your changes"
   ```
2. Push to your fork:
   ```
   git push origin feature/your-feature-name
   ```
3. Submit a pull request through the GitHub website.

## Code Style

We follow the black style guide for Python code. Please ensure your code adheres to this style.

## Reporting Bugs

If you find a bug, please open an issue on the GitHub repository using our bug report template. To do this:

1. Go to the [Issues](https://github.com/jahwag/claudesync/issues) page of the ClaudeSync repository.
2. Click on "New Issue".
3. Select the "Bug Report" template.
4. Fill out the template with as much detail as possible.

When reporting a bug, please include:

- A clear and concise description of the bug
- Steps to reproduce the behavior
- Expected behavior
- Any error messages or stack traces
- Your environment details (OS, Python version, ClaudeSync version)
- Your ClaudeSync configuration (use `claudesync config list`)
- Any relevant logs (you can increase log verbosity with `claudesync config set log_level DEBUG`)

The more information you provide, the easier it will be for us to reproduce and fix the bug.

## Requesting Features

If you have an idea for a new feature, please open an issue on the GitHub repository. Describe the feature and why you think it would be useful for the project.

## Questions

If you have any questions about contributing, feel free to open an issue for discussion.

Thank you for your interest in improving ClaudeSync!
````

### LICENSE

```txt
MIT License

Copyright (c) 2024 Jahziah Wagner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### src/claudesync/chat_sync.py

```python
import json
import logging
import os
import re

from tqdm import tqdm

from .exceptions import ConfigurationError

logger = logging.getLogger(__name__)


def sync_chats(provider, config, sync_all=False):
    """
    Synchronize chats and their artifacts from the remote source.

    This function fetches all chats for the active organization, saves their metadata,
    messages, and extracts any artifacts found in the assistant's messages.

    Args:
        provider: The API provider instance.
        config: The configuration manager instance.
        sync_all (bool): If True, sync all chats regardless of project. If False, only sync chats for the active project.

    Raises:
        ConfigurationError: If required configuration settings are missing.
    """
    # Get the local_path for chats
    local_path = config.get("local_path")
    if not local_path:
        raise ConfigurationError(
            "Local path not set. Use 'claudesync project set' or 'claudesync project create' to set it."
        )

    # Create chats directory within local_path
    chat_destination = os.path.join(local_path, "claude_chats")
    os.makedirs(chat_destination, exist_ok=True)

    # Get the active organization ID
    organization_id = config.get("active_organization_id")
    if not organization_id:
        raise ConfigurationError(
            "No active organization set. Please set an organization."
        )

    # Get the active project ID
    active_project_id = config.get("active_project_id")
    if not active_project_id and not sync_all:
        raise ConfigurationError(
            "No active project set. Please set a project or use the -a flag to sync all chats."
        )

    # Fetch all chats for the organization
    logger.debug(f"Fetching chats for organization {organization_id}")
    chats = provider.get_chat_conversations(organization_id)
    logger.debug(f"Found {len(chats)} chats")

    # Process each chat
    for chat in tqdm(chats, desc="Chats"):
        sync_chat(
            active_project_id,
            chat,
            chat_destination,
            organization_id,
            provider,
            sync_all,
        )

    logger.debug(f"Chats and artifacts synchronized to {chat_destination}")


def sync_chat(
    active_project_id, chat, chat_destination, organization_id, provider, sync_all
):
    # Check if the chat belongs to the active project or if we're syncing all chats
    if sync_all or (
        chat.get("project") and chat["project"].get("uuid") == active_project_id
    ):
        logger.debug(f"Processing chat {chat['uuid']}")
        chat_folder = os.path.join(chat_destination, chat["uuid"])
        os.makedirs(chat_folder, exist_ok=True)

        # Save chat metadata
        metadata_file = os.path.join(chat_folder, "metadata.json")
        if not os.path.exists(metadata_file):
            with open(metadata_file, "w") as f:
                json.dump(chat, f, indent=2)

        # Fetch full chat conversation
        logger.debug(f"Fetching full conversation for chat {chat['uuid']}")
        full_chat = provider.get_chat_conversation(organization_id, chat["uuid"])

        # Process each message in the chat
        for message in full_chat["chat_messages"]:
            message_file = os.path.join(chat_folder, f"{message['uuid']}.json")

            # Skip processing if the message file already exists
            if os.path.exists(message_file):
                logger.debug(f"Skipping existing message {message['uuid']}")
                continue

            # Save the message
            with open(message_file, "w") as f:
                json.dump(message, f, indent=2)

            # Handle artifacts in assistant messages
            if message["sender"] == "assistant":
                artifacts = extract_artifacts(message["text"])
                if artifacts:
                    save_artifacts(artifacts, chat_folder, message)
    else:
        logger.debug(
            f"Skipping chat {chat['uuid']} as it doesn't belong to the active project"
        )


def save_artifacts(artifacts, chat_folder, message):
    logger.info(f"Found {len(artifacts)} artifacts in message {message['uuid']}")
    artifact_folder = os.path.join(chat_folder, "artifacts")
    os.makedirs(artifact_folder, exist_ok=True)
    for artifact in artifacts:
        # Save each artifact
        artifact_file = os.path.join(
            artifact_folder,
            f"{artifact['identifier']}.{get_file_extension(artifact['type'])}",
        )
        if not os.path.exists(artifact_file):
            with open(artifact_file, "w") as f:
                f.write(artifact["content"])


def get_file_extension(artifact_type):
    """
    Get the appropriate file extension for a given artifact type.

    Args:
        artifact_type (str): The MIME type of the artifact.

    Returns:
        str: The corresponding file extension.
    """
    type_to_extension = {
        "text/html": "html",
        "application/vnd.ant.code": "txt",
        "image/svg+xml": "svg",
        "application/vnd.ant.mermaid": "mmd",
        "application/vnd.ant.react": "jsx",
    }
    return type_to_extension.get(artifact_type, "txt")


def extract_artifacts(text):
    """
    Extract artifacts from the given text.

    This function searches for antArtifact tags in the text and extracts
    the artifact information, including identifier, type, and content.

    Args:
        text (str): The text to search for artifacts.

    Returns:
        list: A list of dictionaries containing artifact information.
    """
    artifacts = []

    # Regular expression to match the <antArtifact> tags and extract their attributes and content
    pattern = re.compile(
        r'<antArtifact\s+identifier="([^"]+)"\s+type="([^"]+)"\s+title="([^"]+)">([\s\S]*?)</antArtifact>',
        re.MULTILINE,
    )

    # Find all matches in the text
    matches = pattern.findall(text)

    for match in matches:
        identifier, artifact_type, title, content = match
        artifacts.append(
            {
                "identifier": identifier,
                "type": artifact_type,
                "content": content.strip(),
            }
        )

    return artifacts
```

### src/claudesync/compression.py

```python
import json
import zlib
import bz2
import lzma
import base64
import brotli
from collections import Counter
import os
import io
import heapq


def compress_files(local_path, local_files, algorithm):
    packed_content = _pack_files(local_path, local_files)
    return compress_content(packed_content, algorithm)


def decompress_files(local_path, compressed_content, algorithm):
    decompressed_content = decompress_content(compressed_content, algorithm)
    _unpack_files(local_path, decompressed_content)


def _pack_files(local_path, local_files):
    packed_content = io.StringIO()
    for file_path, file_hash in local_files.items():
        full_path = os.path.join(local_path, file_path)
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        packed_content.write(f"--- BEGIN FILE: {file_path} ---\n")
        packed_content.write(content)
        packed_content.write(f"\n--- END FILE: {file_path} ---\n")
    return packed_content.getvalue()


def _unpack_files(local_path, decompressed_content):
    current_file = None
    current_content = io.StringIO()

    for line in decompressed_content.splitlines():
        if line.startswith("--- BEGIN FILE:"):
            if current_file:
                _write_file(local_path, current_file, current_content.getvalue())
                current_content = io.StringIO()
            current_file = line.split("--- BEGIN FILE:")[1].strip()
        elif line.startswith("--- END FILE:"):
            if current_file:
                _write_file(local_path, current_file, current_content.getvalue())
                current_file = None
                current_content = io.StringIO()
        else:
            current_content.write(line + "\n")

    if current_file:
        _write_file(local_path, current_file, current_content.getvalue())


def _write_file(local_path, file_path, content):
    full_path = os.path.join(local_path, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)


def compress_content(content, algorithm):
    compressors = {
        "zlib": zlib_compress,
        "bz2": bz2_compress,
        "lzma": lzma_compress,
        "brotli": brotli_compress,  # Add Brotli to compressors
        "dictionary": dictionary_compress,
        "rle": rle_compress,
        "huffman": huffman_compress,
        "lzw": lzw_compress,
        "pack": no_compress,
    }
    if algorithm in compressors:
        return compressors[algorithm](content)
    else:
        return content  # No compression


def decompress_content(compressed_content, algorithm):
    decompressors = {
        "zlib": zlib_decompress,
        "bz2": bz2_decompress,
        "lzma": lzma_decompress,
        "brotli": brotli_decompress,  # Add Brotli to decompressors
        "dictionary": dictionary_decompress,
        "rle": rle_decompress,
        "huffman": huffman_decompress,
        "lzw": lzw_decompress,
        "pack": no_decompress,
    }
    if algorithm in decompressors:
        return decompressors[algorithm](compressed_content)
    else:
        return compressed_content  # No decompression


# Pack compression
def no_compress(text):
    return text


def no_decompress(compressed_text):
    return compressed_text


# Brotli compression
def brotli_compress(text):
    compressed = brotli.compress(text.encode("utf-8"))
    return base64.b64encode(compressed).decode("ascii")


def brotli_decompress(compressed_text):
    decoded = base64.b64decode(compressed_text.encode("ascii"))
    return brotli.decompress(decoded).decode("utf-8")


# Zlib compression
def zlib_compress(text):
    compressed = zlib.compress(text.encode("utf-8"))
    return base64.b64encode(compressed).decode("ascii")


def zlib_decompress(compressed_text):
    decoded = base64.b64decode(compressed_text.encode("ascii"))
    return zlib.decompress(decoded).decode("utf-8")


# BZ2 compression
def bz2_compress(text):
    compressed = bz2.compress(text.encode("utf-8"))
    return base64.b64encode(compressed).decode("ascii")


def bz2_decompress(compressed_text):
    decoded = base64.b64decode(compressed_text.encode("ascii"))
    return bz2.decompress(decoded).decode("utf-8")


# LZMA compression
def lzma_compress(text):
    compressed = lzma.compress(text.encode("utf-8"))
    return base64.b64encode(compressed).decode("ascii")


def lzma_decompress(compressed_text):
    decoded = base64.b64decode(compressed_text.encode("ascii"))
    return lzma.decompress(decoded).decode("utf-8")


# Dictionary-based compression
def dictionary_compress(text):
    words = text.split()
    dictionary = {}
    compressed = []

    for word in words:
        if word not in dictionary:
            dictionary[word] = str(len(dictionary))
        compressed.append(dictionary[word])

    return json.dumps({"dict": dictionary, "compressed": " ".join(compressed)})


def dictionary_decompress(compressed_text):
    data = json.loads(compressed_text)
    dictionary = {v: k for k, v in data["dict"].items()}
    return " ".join(dictionary[token] for token in data["compressed"].split())


# Run-length encoding (RLE)
def rle_compress(text):
    compressed = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append((text[i - 1], count))
            count = 1
    compressed.append((text[-1], count))
    return json.dumps(compressed)


def rle_decompress(compressed_text):
    compressed = json.loads(compressed_text)
    return "".join(char * count for char, count in compressed)


# Huffman coding
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_compress(text):
    freq = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}

    def generate_codes(node, code):
        if node.char:
            codes[node.char] = code
            return
        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(root, "")

    encoded = "".join(codes[char] for char in text)
    padding = 8 - len(encoded) % 8
    encoded += "0" * padding

    compressed = bytearray()
    for i in range(0, len(encoded), 8):
        byte = encoded[i : i + 8]
        compressed.append(int(byte, 2))

    return json.dumps(
        {
            "tree": {char: code for char, code in codes.items()},
            "padding": padding,
            "data": base64.b64encode(compressed).decode("ascii"),
        }
    )


def huffman_decompress(compressed_text):
    data = json.loads(compressed_text)
    tree = {code: char for char, code in data["tree"].items()}
    padding = data["padding"]
    compressed = base64.b64decode(data["data"].encode("ascii"))

    binary = "".join(f"{byte:08b}" for byte in compressed)
    binary = binary[:-padding] if padding else binary

    decoded = ""
    code = ""
    for bit in binary:
        code += bit
        if code in tree:
            decoded += tree[code]
            code = ""

    return decoded


# LZW compression
def lzw_compress(text):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    w = ""
    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = len(dictionary)
            w = c
    if w:
        result.append(dictionary[w])
    return base64.b64encode(bytes(result)).decode("ascii")


def lzw_decompress(compressed_text):
    compressed = base64.b64decode(compressed_text.encode("ascii"))
    dictionary = {i: chr(i) for i in range(256)}
    result = []
    w = chr(compressed[0])
    result.append(w)
    for i in range(1, len(compressed)):
        k = compressed[i]
        if k in dictionary:
            entry = dictionary[k]
        elif k == len(dictionary):
            entry = w + w[0]
        else:
            raise ValueError("Bad compressed k: %s" % k)
        result.append(entry)
        dictionary[len(dictionary)] = w + entry[0]
        w = entry
    return "".join(result)
```

### src/claudesync/provider_factory.py

```python
# src/claudesync/provider_factory.py

from .providers.base_provider import BaseProvider
from .providers.claude_ai import ClaudeAIProvider


def get_provider(config=None, provider_name=None) -> BaseProvider:
    """
    Retrieve an instance of a provider class based on the provider name.

    This function serves as a factory to instantiate provider classes. It maintains a registry of available
    providers. If a provider name is not specified, it returns a list of available provider names. If a provider
    name is specified but not found in the registry, it raises a ValueError.

    Args:
        config: for testing
        provider_name (str, optional): The name of the provider to retrieve. If None, returns a list of available
                                       provider names.

    Returns:
        BaseProvider: An instance of the requested provider class.

    Raises:
        ValueError: If the specified provider_name is not found in the registry of providers.
    """
    providers = {
        "claude.ai": ClaudeAIProvider,
        # Add other providers here as they are implemented
    }

    if provider_name is None:
        return list(providers.keys())

    provider_class = providers.get(provider_name)
    if provider_class is None:
        raise ValueError(f"Unsupported provider: {provider_name}")

    return provider_class(config)
```

### src/claudesync/syncmanager.py

```python
[Error reading file: 'ascii' codec can't decode byte 0xe2 in position 2655: ordinal not in range(128)]
```

### src/claudesync/session_key_manager.py

```python
import subprocess
import base64
import logging
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class SessionKeyManager:
    def __init__(self):
        self.ssh_key_path = self._find_ssh_key()
        self.logger = logging.getLogger(__name__)

    def _find_ssh_key(self):
        ssh_dir = Path.home() / ".ssh"
        key_names = ["id_ed25519", "id_ecdsa"]
        for key_name in key_names:
            key_path = ssh_dir / key_name
            if key_path.exists():
                return str(key_path)

        # If no supported key is found, prompt the user to generate an Ed25519 key
        print("* No supported SSH key found. RSA keys are no longer supported.")
        print("* Please generate an Ed25519 key using the following command:")
        print('ssh-keygen -t ed25519 -C "your_email@example.com"')
        return input("Enter the full path to your new Ed25519 private key: ")

    def _get_key_type(self):
        try:
            result = subprocess.run(
                ["ssh-keygen", "-l", "-f", self.ssh_key_path],
                capture_output=True,
                text=True,
                check=True,
            )
            output = result.stdout.lower()
            if "ecdsa" in output:
                return "ecdsa"
            elif "ed25519" in output:
                return "ed25519"
            else:
                raise ValueError(f"Unsupported key type for {self.ssh_key_path}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to determine key type: {e}")
            raise RuntimeError(
                "Failed to determine SSH key type. Make sure the key file is valid and accessible."
            )

    def _derive_key_from_ssh_key(self):
        with open(self.ssh_key_path, "rb") as key_file:
            ssh_key_data = key_file.read()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"claudesync",  # Using a fixed salt; consider using a secure random salt in production
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(ssh_key_data))
        return key

    def encrypt_session_key(self, provider, session_key):
        self._get_key_type()
        return self._encrypt_symmetric(session_key)

    def _encrypt_symmetric(self, session_key):
        key = self._derive_key_from_ssh_key()
        f = Fernet(key)
        encrypted_session_key = f.encrypt(session_key.encode()).decode()
        return encrypted_session_key, "symmetric"

    def decrypt_session_key(self, provider, encryption_method, encrypted_session_key):
        if not encrypted_session_key or not encryption_method:
            return None

        if encryption_method == "symmetric":
            return self._decrypt_symmetric(encrypted_session_key)
        else:
            raise ValueError(f"Unknown encryption method: {encryption_method}")

    def _decrypt_symmetric(self, encrypted_session_key):
        key = self._derive_key_from_ssh_key()
        f = Fernet(key)
        return f.decrypt(encrypted_session_key.encode()).decode()
```

### src/claudesync/exceptions.py

```python
class ConfigurationError(Exception):
    """
    Exception raised when there's an issue with the application's configuration.

    This exception should be raised to indicate problems such as missing required configuration options,
    invalid values, or issues loading configuration files. It helps in distinguishing configuration-related
    errors from other types of exceptions.
    """

    pass


class ProviderError(Exception):
    """
    Exception raised when there's an issue with a provider operation.

    This exception is used to signal failures in operations related to external service providers,
    such as authentication failures, data retrieval errors, or actions that cannot be completed as requested.
    It allows for more granular error handling that is specific to provider interactions.
    """

    pass
```

### src/claudesync/__init__.py

```python

```

### src/claudesync/utils.py

```python
import os
import hashlib
from functools import wraps
from pathlib import Path

import click
import pathspec
import logging

from claudesync.exceptions import ConfigurationError, ProviderError
from claudesync.provider_factory import get_provider

logger = logging.getLogger(__name__)


def normalize_and_calculate_md5(content):
    """
    Calculate the MD5 checksum of the given content after normalizing line endings.

    This function normalizes the line endings of the input content to Unix-style (\n),
    strips leading and trailing whitespace, and then calculates the MD5 checksum of the
    normalized content. This is useful for ensuring consistent checksums across different
    operating systems and environments where line ending styles may vary.

    Args:
        content (str): The content for which to calculate the checksum.

    Returns:
        str: The hexadecimal MD5 checksum of the normalized content.
    """
    normalized_content = content.replace("\r\n", "\n").replace("\r", "\n").strip()
    return hashlib.md5(normalized_content.encode("utf-8")).hexdigest()


def load_gitignore(base_path):
    """
    Loads and parses the .gitignore file from the specified base path.

    This function attempts to find a .gitignore file in the given base path. If found,
    it reads the file and creates a PathSpec object that can be used to match paths
    against the patterns defined in the .gitignore file. This is useful for filtering
    out files that should be ignored based on the project's .gitignore settings.

    Args:
        base_path (str): The base directory path where the .gitignore file is located.

    Returns:
        pathspec.PathSpec or None: A PathSpec object containing the patterns from the .gitignore file
                                    if the file exists; otherwise, None.
    """
    gitignore_path = os.path.join(base_path, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            return pathspec.PathSpec.from_lines("gitwildmatch", f)
    return None


def is_text_file(file_path, sample_size=8192):
    """
    Determines if a file is a text file by checking for the absence of null bytes.

    This function reads a sample of the file (default 8192 bytes) and checks if it contains
    any null byte (\x00). The presence of a null byte is often indicative of a binary file.
    This is a heuristic method and may not be 100% accurate for all file types.

    Args:
        file_path (str): The path to the file to be checked.
        sample_size (int, optional): The number of bytes to read from the file for checking.
                                     Defaults to 8192.

    Returns:
        bool: True if the file is likely a text file, False if it is likely binary or an error occurred.
    """
    try:
        with open(file_path, "rb") as file:
            return b"\x00" not in file.read(sample_size)
    except IOError:
        return False


def compute_md5_hash(content):
    """
    Computes the MD5 hash of the given content.

    This function takes a string as input, encodes it into UTF-8, and then computes the MD5 hash of the encoded string.
    The result is a hexadecimal representation of the hash, which is commonly used for creating a quick and simple
    fingerprint of a piece of data.

    Args:
        content (str): The content for which to compute the MD5 hash.

    Returns:
        str: The hexadecimal MD5 hash of the input content.
    """
    return hashlib.md5(content.encode("utf-8")).hexdigest()


def should_process_file(
    config_manager, file_path, filename, gitignore, base_path, claudeignore
):
    """
    Determines whether a file should be processed based on various criteria.

    This function checks if a file should be included in the synchronization process by applying
    several filters:
    - Checks if the file size is within the configured maximum limit.
    - Skips temporary editor files (ending with '~').
    - Applies .gitignore rules if a gitignore PathSpec is provided.
    - Verifies if the file is a text file.

    Args:
        file_path (str): The full path to the file.
        filename (str): The name of the file.
        gitignore (pathspec.PathSpec or None): A PathSpec object containing .gitignore patterns, if available.
        base_path (str): The base directory path of the project.
        claudeignore (pathspec.PathSpec or None): A PathSpec object containing .claudeignore patterns, if available.

    Returns:
        bool: True if the file should be processed, False otherwise.
    """
    # Check file size
    max_file_size = config_manager.get("max_file_size", 32 * 1024)
    if os.path.getsize(file_path) > max_file_size:
        return False

    # Skip temporary editor files
    if filename.endswith("~"):
        return False

    rel_path = os.path.relpath(file_path, base_path)

    # Use gitignore rules if available
    if gitignore and gitignore.match_file(rel_path):
        return False

    # Use .claudeignore rules if available
    if claudeignore and claudeignore.match_file(rel_path):
        return False

    # Check if it's a text file
    return is_text_file(file_path)


def process_file(file_path):
    """
    Reads the content of a file and computes its MD5 hash.

    This function attempts to read the file as UTF-8 text and compute its MD5 hash.
    If the file cannot be read as UTF-8 or any other error occurs, it logs the issue
    and returns None.

    Args:
        file_path (str): The path to the file to be processed.

    Returns:
        str or None: The MD5 hash of the file's content if successful, None otherwise.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return compute_md5_hash(content)
    except UnicodeDecodeError:
        logger.debug(f"Unable to read {file_path} as UTF-8 text. Skipping.")
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
    return None


def get_local_files(config, local_path, category=None, include_submodules=False):
    """
    Retrieves a dictionary of local files within a specified path, applying various filters.

    Args:
        config: config manager to use
        local_path (str): The base directory path to search for files.
        category (str, optional): The file category to filter by.
        include_submodules (bool, optional): Whether to include files from submodules.

    Returns:
        dict: A dictionary where keys are relative file paths, and values are MD5 hashes of the file contents.
    """
    gitignore = load_gitignore(local_path)
    claudeignore = load_claudeignore(local_path)
    files = {}
    exclude_dirs = {
        ".git",
        ".svn",
        ".hg",
        ".bzr",
        "_darcs",
        "CVS",
        "claude_chats",
        ".claudesync",
    }

    categories = config.get("file_categories", {})
    if category and category not in categories:
        raise ValueError(f"Invalid category: {category}")

    patterns = ["*"]  # Default to all files
    if category:
        patterns = categories[category]["patterns"]

    spec = pathspec.PathSpec.from_lines("gitwildmatch", patterns)

    submodules = config.get("submodules", [])
    submodule_paths = [sm["relative_path"] for sm in submodules]

    for root, dirs, filenames in os.walk(local_path, topdown=True):
        rel_root = os.path.relpath(root, local_path)
        rel_root = "" if rel_root == "." else rel_root

        # Skip submodule directories if not including submodules
        if not include_submodules:
            dirs[:] = [
                d for d in dirs if os.path.join(rel_root, d) not in submodule_paths
            ]

        dirs[:] = [
            d
            for d in dirs
            if d not in exclude_dirs
            and not (gitignore and gitignore.match_file(os.path.join(rel_root, d)))
            and not (
                claudeignore and claudeignore.match_file(os.path.join(rel_root, d))
            )
        ]

        for filename in filenames:
            rel_path = os.path.join(rel_root, filename)
            full_path = os.path.join(root, filename)

            if spec.match_file(rel_path) and should_process_file(
                config, full_path, filename, gitignore, local_path, claudeignore
            ):
                file_hash = process_file(full_path)
                if file_hash:
                    files[rel_path] = file_hash

    return files


def handle_errors(func):
    """
    A decorator that wraps a function to catch and handle specific exceptions.

    This decorator catches exceptions of type ConfigurationError and ProviderError
    that are raised within the decorated function. When such an exception is caught,
    it prints an error message to the console using click's echo function. This is
    useful for CLI applications where a friendly error message is preferred over a
    full traceback for known error conditions.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The wrapper function that includes exception handling.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ConfigurationError, ProviderError) as e:
            click.echo(f"Error: {str(e)}")

    return wrapper


def validate_and_get_provider(config, require_org=True, require_project=False):
    """
    Validates the configuration for the presence of an active provider and session key,
    and optionally checks for an active organization ID and project ID. If validation passes,
    it retrieves the provider instance based on the active provider name.

    Args:
        config (ConfigManager): The configuration manager instance containing settings.
        require_org (bool, optional): Flag to indicate whether an active organization ID
                                      is required. Defaults to True.
        require_project (bool, optional): Flag to indicate whether an active project ID
                                          is required. Defaults to False.

    Returns:
        object: An instance of the provider specified in the configuration.

    Raises:
        ConfigurationError: If the active provider or session key is missing, or if
                            require_org is True and no active organization ID is set,
                            or if require_project is True and no active project ID is set.
        ProviderError: If the session key has expired.
    """
    active_provider = config.get_active_provider()
    if not active_provider:
        raise ConfigurationError(
            "No active provider set. Please select a provider for this project."
        )

    session_key, session_key_expiry = config.get_session_key(active_provider)
    if not session_key:
        raise ConfigurationError(
            f"No valid session key found for {active_provider}. Please log in again."
        )

    if require_org and not config.get("active_organization_id"):
        raise ConfigurationError(
            "No active organization set. Please select an organization."
        )

    if require_project and not config.get("active_project_id"):
        raise ConfigurationError(
            "No active project set. Please select or create a project."
        )

    return get_provider(config, active_provider)


def validate_and_store_local_path(config):
    """
    Prompts the user for the absolute path to their local project directory and stores it in the configuration.

    This function repeatedly prompts the user to enter the absolute path to their local project directory until
    a valid absolute path is provided. The path is validated to ensure it exists, is a directory, and is an absolute path.
    Once a valid path is provided, it is stored in the configuration using the `set` method of the `ConfigManager` object.

    Args:
        config (ConfigManager): The configuration manager instance to store the local path setting.

    Note:
        This function uses `click.prompt` to interact with the user, providing a default path (the current working directory)
        and validating the user's input to ensure it meets the criteria for an absolute path to a directory.
    """

    def get_default_path():
        return os.getcwd()

    while True:
        default_path = get_default_path()
        local_path = click.prompt(
            "Enter the absolute path to your local project directory",
            type=click.Path(
                exists=True, file_okay=False, dir_okay=True, resolve_path=True
            ),
            default=default_path,
            show_default=True,
        )

        if os.path.isabs(local_path):
            config.set("local_path", local_path)
            click.echo(f"Local path set to: {local_path}")
            break
        else:
            click.echo("Please enter an absolute path.")


def load_claudeignore(base_path):
    """
    Loads and parses the .claudeignore file from the specified base path.

    Args:
        base_path (str): The base directory path where the .claudeignore file is located.

    Returns:
        pathspec.PathSpec or None: A PathSpec object containing the patterns from the .claudeignore file
                                    if the file exists; otherwise, None.
    """
    claudeignore_path = os.path.join(base_path, ".claudeignore")
    if os.path.exists(claudeignore_path):
        with open(claudeignore_path, "r") as f:
            return pathspec.PathSpec.from_lines("gitwildmatch", f)
    return None


def detect_submodules(base_path, submodule_detect_filenames):
    """
    Detects submodules within a project based on specific filenames, respecting .gitignore and .claudeignore.

    Args:
        base_path (str): The base directory path to start the search from.
        submodule_detect_filenames (list): List of filenames that indicate a submodule.

    Returns:
        list: A list of tuples (relative_path, detected_filename) for detected submodules,
              excluding the root directory and respecting ignore files.
    """
    submodules = []
    base_path = Path(base_path)
    gitignore = load_gitignore(base_path)
    claudeignore = load_claudeignore(base_path)

    for root, dirs, files in os.walk(base_path):
        rel_root = Path(root).relative_to(base_path)

        # Check if the current directory should be ignored
        if gitignore and gitignore.match_file(str(rel_root)):
            dirs[:] = []  # Don't descend into this directory
            continue
        if claudeignore and claudeignore.match_file(str(rel_root)):
            dirs[:] = []  # Don't descend into this directory
            continue

        for filename in submodule_detect_filenames:
            if filename in files:
                relative_path = str(rel_root)
                # Exclude the root directory (represented by an empty string or '.')
                if relative_path not in ("", "."):
                    # Check if the file itself should be ignored
                    file_path = rel_root / filename
                    if (gitignore and gitignore.match_file(str(file_path))) or (
                        claudeignore and claudeignore.match_file(str(file_path))
                    ):
                        continue
                    submodules.append((relative_path, filename))
                break  # Stop searching this directory once a submodule is found

    return submodules
```

### src/claudesync/cli/auth.py

```python
import click

from claudesync.provider_factory import get_provider
from ..exceptions import ProviderError
from ..utils import handle_errors


@click.group()
def auth():
    """Manage authentication."""
    pass


@auth.command()
@click.option(
    "--provider",
    prompt="Choose provider",
    type=click.Choice(["claude.ai"], case_sensitive=False),
    default="claude.ai",
    help="The provider to use for this project",
)
@click.pass_context
@handle_errors
def login(ctx, provider):
    """Authenticate with an AI provider."""
    config = ctx.obj
    provider_instance = get_provider(config, provider)

    try:
        session_key, expiry = provider_instance.login()
        config.set_session_key(provider, session_key, expiry)
        click.echo(
            f"Successfully authenticated with {provider}. Session key stored globally."
        )
    except ProviderError as e:
        click.echo(f"Authentication failed: {str(e)}")


@auth.command()
@click.pass_obj
def logout(config):
    """Log out from all AI providers."""
    config.clear_all_session_keys()
    click.echo("Logged out from all providers successfully.")


@auth.command()
@click.pass_obj
def ls(config):
    """List all authenticated providers."""
    authenticated_providers = config.get_providers_with_session_keys()
    if authenticated_providers:
        click.echo("Authenticated providers:")
        for provider in authenticated_providers:
            click.echo(f"  - {provider}")
    else:
        click.echo("No authenticated providers found.")
```

### src/claudesync/cli/config.py

```python
import json

import click

from .category import category
from ..exceptions import ConfigurationError
from ..utils import handle_errors


@click.group()
def config():
    """Manage claudesync configuration."""
    pass


@config.command()
@click.argument("key")
@click.argument("value")
@click.pass_obj
@handle_errors
def set(config, key, value):
    """Set a configuration value."""
    # Check if the key exists in the configuration
    if key not in config.global_config and key not in config.local_config:
        raise ConfigurationError(f"Configuration property '{key}' does not exist.")

    # Convert string 'true' and 'false' to boolean
    if value.lower() == "true":
        value = True
    elif value.lower() == "false":
        value = False
    # Try to convert to int or float if possible
    else:
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass  # Keep as string if not a number

    config.set(key, value)
    click.echo(f"Configuration {key} set to {value}")


@config.command()
@click.argument("key")
@click.pass_obj
@handle_errors
def get(config, key):
    """Get a configuration value."""
    value = config.get(key)
    if value is None:
        click.echo(f"Configuration {key} is not set")
    else:
        click.echo(f"{key}: {value}")


@config.command()
@click.pass_obj
@handle_errors
def ls(config):
    """List all configuration values."""
    # Combine global and local configurations
    combined_config = config.global_config.copy()
    combined_config.update(config.local_config)

    # Print the combined configuration as JSON
    click.echo(json.dumps(combined_config, indent=2, sort_keys=True))


config.add_command(category)
```

### src/claudesync/cli/file.py

```python
import click
from ..utils import handle_errors, validate_and_get_provider


@click.group()
def file():
    """Manage remote project files."""
    pass


@file.command()
@click.pass_obj
@handle_errors
def ls(config):
    """List files in the active remote project."""
    provider = validate_and_get_provider(config, require_project=True)
    active_organization_id = config.get("active_organization_id")
    active_project_id = config.get("active_project_id")
    files = provider.list_files(active_organization_id, active_project_id)
    if not files:
        click.echo("No files found in the active project.")
    else:
        click.echo(
            f"Files in project '{config.get('active_project_name')}' (ID: {active_project_id}):"
        )
        for file in files:
            click.echo(
                f"  - {file['file_name']} (ID: {file['uuid']}, Created: {file['created_at']})"
            )
```

### src/claudesync/cli/category.py

```python
import click
from ..utils import handle_errors


@click.group()
def category():
    """Manage file categories."""
    pass


@category.command()
@click.argument("name")
@click.option("--description", required=True, help="Description of the category")
@click.option(
    "--patterns", required=True, multiple=True, help="File patterns for the category"
)
@click.pass_obj
@handle_errors
def add(config, name, description, patterns):
    """Add a new file category."""
    config.add_file_category(name, description, list(patterns))
    click.echo(f"File category '{name}' added successfully.")


@category.command()
@click.argument("name")
@click.pass_obj
@handle_errors
def rm(config, name):
    """Remove a file category."""
    config.remove_file_category(name)
    click.echo(f"File category '{name}' removed successfully.")


@category.command()
@click.argument("name")
@click.option("--description", help="New description for the category")
@click.option("--patterns", multiple=True, help="New file patterns for the category")
@click.pass_obj
@handle_errors
def update(config, name, description, patterns):
    """Update an existing file category."""
    config.update_file_category(name, description, list(patterns) if patterns else None)
    click.echo(f"File category '{name}' updated successfully.")


@category.command()
@click.pass_obj
@handle_errors
def ls(config):
    """List all file categories."""
    categories = config.get("file_categories", {})
    if not categories:
        click.echo("No file categories defined.")
    else:
        for name, data in categories.items():
            click.echo(f"\nCategory: {name}")
            click.echo(f"Description: {data['description']}")
            click.echo("Patterns:")
            for pattern in data["patterns"]:
                click.echo(f"  - {pattern}")


@category.command()
@click.argument("category", required=True)
@click.pass_obj
@handle_errors
def set_default(config, category):
    """Set the default category for synchronization."""
    config.set_default_category(category)
    click.echo(f"Default sync category set to: {category}")
```

### src/claudesync/cli/chat.py

```python
import os

import click
import logging
from ..exceptions import ProviderError
from ..utils import handle_errors, validate_and_get_provider
from ..chat_sync import sync_chats

logger = logging.getLogger(__name__)


@click.group()
def chat():
    """Manage and synchronize chats."""
    pass


@chat.command()
@click.pass_obj
@handle_errors
def pull(config):
    """Synchronize chats and their artifacts from the remote source."""
    provider = validate_and_get_provider(config, require_project=True)
    sync_chats(provider, config)


@chat.command()
@click.pass_obj
@handle_errors
def ls(config):
    """List all chats."""
    provider = validate_and_get_provider(config)
    organization_id = config.get("active_organization_id")
    chats = provider.get_chat_conversations(organization_id)

    for chat in chats:
        project = chat.get("project")
        project_name = project.get("name") if project else ""
        click.echo(
            f"UUID: {chat.get('uuid', 'Unknown')}, "
            f"Name: {chat.get('name', 'Unnamed')}, "
            f"Project: {project_name}, "
            f"Updated: {chat.get('updated_at', 'Unknown')}"
        )


@chat.command()
@click.option("-a", "--all", "delete_all", is_flag=True, help="Delete all chats")
@click.pass_obj
@handle_errors
def rm(config, delete_all):
    """Delete chat conversations. Use -a to delete all chats, or run without -a to select specific chats to delete."""
    provider = validate_and_get_provider(config)
    organization_id = config.get("active_organization_id")

    if delete_all:
        delete_all_chats(provider, organization_id)
    else:
        delete_single_chat(provider, organization_id)


def delete_chats(provider, organization_id, uuids):
    """Delete a list of chats by their UUIDs."""
    try:
        result = provider.delete_chat(organization_id, uuids)
        return len(result), 0
    except ProviderError as e:
        logger.error(f"Error deleting chats: {str(e)}")
        click.echo(f"Error occurred while deleting chats: {str(e)}")
        return 0, len(uuids)


def delete_all_chats(provider, organization_id):
    """Delete all chats for the given organization."""
    if click.confirm("Are you sure you want to delete all chats?"):
        total_deleted = 0
    with click.progressbar(length=100, label="Deleting chats") as bar:
        while True:
            chats = provider.get_chat_conversations(organization_id)
            if not chats:
                break
            uuids_to_delete = [chat["uuid"] for chat in chats[:50]]
            deleted, _ = delete_chats(provider, organization_id, uuids_to_delete)
            total_deleted += deleted
            bar.update(len(uuids_to_delete))
    click.echo(f"Chat deletion complete. Total chats deleted: {total_deleted}")


def delete_single_chat(provider, organization_id):
    """Delete a single chat selected by the user."""
    chats = provider.get_chat_conversations(organization_id)
    if not chats:
        click.echo("No chats found.")
        return

    display_chat_list(chats)
    selected_chat = get_chat_selection(chats)
    if selected_chat:
        confirm_and_delete_chat(provider, organization_id, selected_chat)


def display_chat_list(chats):
    """Display a list of chats to the user."""
    click.echo("Available chats:")
    for idx, chat in enumerate(chats, 1):
        project = chat.get("project")
        project_name = project.get("name") if project else ""
        click.echo(
            f"{idx}. Name: {chat.get('name', 'Unnamed')}, "
            f"Project: {project_name}, Updated: {chat.get('updated_at', 'Unknown')}"
        )


def get_chat_selection(chats):
    """Get a valid chat selection from the user."""
    while True:
        selection = click.prompt(
            "Enter the number of the chat to delete (or 'q' to quit)", type=str
        )
        if selection.lower() == "q":
            return None
        try:
            selection = int(selection)
            if 1 <= selection <= len(chats):
                return chats[selection - 1]
            click.echo("Invalid selection. Please try again.")
        except ValueError:
            click.echo("Invalid input. Please enter a number or 'q' to quit.")


def confirm_and_delete_chat(provider, organization_id, chat):
    """Confirm deletion with the user and delete the selected chat."""
    if click.confirm(
        f"Are you sure you want to delete the chat '{chat.get('name', 'Unnamed')}'?"
    ):
        deleted, _ = delete_chats(provider, organization_id, [chat["uuid"]])
        if deleted:
            click.echo(f"Successfully deleted chat: {chat.get('name', 'Unnamed')}")
        else:
            click.echo(f"Failed to delete chat: {chat.get('name', 'Unnamed')}")


@chat.command()
@click.option("--name", default="", help="Name of the chat conversation")
@click.option("--project", help="UUID of the project to associate the chat with")
@click.pass_obj
@handle_errors
def init(config, name, project):
    """Initializes a new chat conversation on the active provider."""
    provider = validate_and_get_provider(config)
    organization_id = config.get("active_organization_id")
    active_project_id = config.get("active_project_id")
    active_project_name = config.get("active_project_name")
    local_path = config.get("local_path")

    if not organization_id:
        click.echo("No active organization set.")
        return

    if not project:
        project = select_project(
            active_project_id,
            active_project_name,
            local_path,
            organization_id,
            provider,
        )
        if project is None:
            return

    try:
        new_chat = provider.create_chat(
            organization_id, chat_name=name, project_uuid=project
        )
        click.echo(f"Created new chat conversation: {new_chat['uuid']}")
        if name:
            click.echo(f"Chat name: {name}")
        click.echo(f"Associated project: {project}")
    except Exception as e:
        click.echo(f"Failed to create chat conversation: {str(e)}")


@chat.command()
@click.argument("message", nargs=-1, required=True)
@click.option("--chat", help="UUID of the chat to send the message to")
@click.option("--timezone", default="UTC", help="Timezone for the message")
@click.pass_obj
@handle_errors
def message(config, message, chat, timezone):
    """Send a message to a specified chat or create a new chat and send the message."""
    provider = validate_and_get_provider(config, require_project=True)
    active_organization_id = config.get("active_organization_id")
    active_project_id = config.get("active_project_id")
    active_project_name = config.get("active_project_name")

    message = " ".join(message)  # Join all message parts into a single string

    try:
        chat = create_chat(
            config,
            active_project_id,
            active_project_name,
            chat,
            active_organization_id,
            provider,
        )
        if chat is None:
            return

        # Send message and process the streaming response
        for event in provider.send_message(
            active_organization_id, chat, message, timezone
        ):
            if "completion" in event:
                click.echo(event["completion"], nl=False)
            elif "content" in event:
                click.echo(event["content"], nl=False)
            elif "error" in event:
                click.echo(f"\nError: {event['error']}")
            elif "message_limit" in event:
                click.echo(
                    f"\nRemaining messages: {event['message_limit']['remaining']}"
                )

        click.echo()  # Print a newline at the end of the response

    except Exception as e:
        click.echo(f"Failed to send message: {str(e)}")


def create_chat(
    config,
    active_project_id,
    active_project_name,
    chat,
    active_organization_id,
    provider,
):
    if not chat:
        if not active_project_name:
            active_project_id = select_project(
                config,
                active_project_id,
                active_project_name,
                active_organization_id,
                provider,
            )
        if active_project_id is None:
            return None

        # Create a new chat with the selected project
        new_chat = provider.create_chat(
            active_organization_id, project_uuid=active_project_id
        )
        chat = new_chat["uuid"]
        click.echo(f"New chat created with ID: {chat}")
    return chat


def select_project(
    config, active_project_id, active_project_name, active_organization_id, provider
):
    all_projects = provider.get_projects(active_organization_id)
    if not all_projects:
        click.echo("No projects found in the active organization.")
        return None

    # Filter projects to include only the active project and its submodules
    filtered_projects = [
        p
        for p in all_projects
        if p["id"] == active_project_id
        or (
            p["name"].startswith(f"{active_project_name}-SubModule-")
            and not p.get("archived_at")
        )
    ]

    if not filtered_projects:
        click.echo("No active project or related submodules found.")
        return None

    # Determine the current working directory
    current_dir = os.path.abspath(os.getcwd())

    default_project = get_default_project(
        config, active_project_id, active_project_name, current_dir, filtered_projects
    )

    click.echo("Available projects:")
    for idx, proj in enumerate(filtered_projects, 1):
        project_type = (
            "Active Project" if proj["id"] == active_project_id else "Submodule"
        )
        default_marker = " (default)" if idx - 1 == default_project else ""
        click.echo(
            f"{idx}. {proj['name']} (ID: {proj['id']}) - {project_type}{default_marker}"
        )

    while True:
        prompt = "Enter the number of the project to associate with the chat"
        if default_project is not None:
            default_project_name = filtered_projects[default_project]["name"]
            prompt += f" (default: {default_project + 1} - {default_project_name})"
        selection = click.prompt(
            prompt,
            type=int,
            default=default_project + 1 if default_project is not None else None,
        )
        if 1 <= selection <= len(filtered_projects):
            project = filtered_projects[selection - 1]["id"]
            break
        click.echo("Invalid selection. Please try again.")
    return project


def get_default_project(
    config, active_project_id, active_project_name, current_dir, filtered_projects
):
    local_path = config.get("local_path")
    if not local_path:
        return None

    # Find the project that matches the current directory
    default_project = None
    for idx, proj in enumerate(filtered_projects):
        if proj["id"] == active_project_id:
            project_path = os.path.abspath(local_path)
        else:
            submodule_name = proj["name"].replace(
                f"{active_project_name}-SubModule-", ""
            )
            project_path = os.path.abspath(
                os.path.join(local_path, "services", submodule_name)
            )
        if current_dir.startswith(project_path):
            default_project = idx
            break
    return default_project
```

### src/claudesync/cli/sync.py

```python
import os
import shutil
import sys
import click
from crontab import CronTab

from ..utils import handle_errors, validate_and_get_provider


@click.command()
@click.pass_obj
@handle_errors
def ls(config):
    """List files in the active remote project."""
    provider = validate_and_get_provider(config, require_project=True)
    active_organization_id = config.get("active_organization_id")
    active_project_id = config.get("active_project_id")
    files = provider.list_files(active_organization_id, active_project_id)
    if not files:
        click.echo("No files found in the active project.")
    else:
        click.echo(
            f"Files in project '{config.get('active_project_name')}' (ID: {active_project_id}):"
        )
        for file in files:
            click.echo(
                f"  - {file['file_name']} (ID: {file['uuid']}, Created: {file['created_at']})"
            )


def validate_local_path(local_path):
    if not local_path:
        click.echo(
            "No local path set. Please select or create a project to set the local path."
        )
        sys.exit(1)
    if not os.path.exists(local_path):
        click.echo(f"The configured local path does not exist: {local_path}")
        click.echo("Please update the local path by selecting or creating a project.")
        sys.exit(1)


@click.command()
@click.pass_obj
@click.option(
    "--interval", type=int, default=5, prompt="Enter sync interval in minutes"
)
@handle_errors
def schedule(config, interval):
    """Set up automated synchronization at regular intervals."""
    claudesync_path = shutil.which("claudesync")
    if not claudesync_path:
        click.echo(
            "Error: claudesync not found in PATH. Please ensure it's installed correctly."
        )
        sys.exit(1)

    if sys.platform.startswith("win"):
        setup_windows_task(claudesync_path, interval)
    else:
        setup_unix_cron(claudesync_path, interval)


def setup_windows_task(claudesync_path, interval):
    click.echo("Windows Task Scheduler setup:")
    command = f'schtasks /create /tn "ClaudeSync" /tr "{claudesync_path} sync" /sc minute /mo {interval}'
    click.echo(f"Run this command to create the task:\n{command}")
    click.echo('\nTo remove the task, run: schtasks /delete /tn "ClaudeSync" /f')


def setup_unix_cron(claudesync_path, interval):
    cron = CronTab(user=True)
    job = cron.new(command=f"{claudesync_path} sync")
    job.minute.every(interval)
    cron.write()
    click.echo(f"Cron job created successfully! It will run every {interval} minutes.")
    click.echo(
        "\nTo remove the cron job, run: crontab -e and remove the line for ClaudeSync"
    )
```

### src/claudesync/cli/submodule.py

```python
import json
import os

import click
from claudesync.exceptions import ProviderError
from ..utils import (
    handle_errors,
    validate_and_get_provider,
    detect_submodules,
)


@click.group()
def submodule():
    """Manage submodules within the current project."""
    pass


@submodule.command()
@click.pass_obj
@handle_errors
def ls(config):
    """List all detected submodules in the current project."""
    local_path = config.get_local_path()
    if not local_path:
        click.echo(
            "No local project path found. Please select an existing project or create a new one using "
            "'claudesync project select' or 'claudesync project create'."
        )
        return

    submodule_detect_filenames = config.get("submodule_detect_filenames", [])
    submodules = detect_submodules(local_path, submodule_detect_filenames)

    if not submodules:
        click.echo("No submodules detected in the current project.")
    else:
        click.echo("Detected submodules:")
        for submodule, detected_file in submodules:
            click.echo(f"  - {submodule} [{detected_file}]")


@submodule.command()
@click.pass_obj
@handle_errors
def create(config):
    """Creates new projects for each detected submodule that doesn't already exist remotely."""
    provider = validate_and_get_provider(config, require_project=True)
    active_organization_id = config.get("active_organization_id")
    active_project_id = config.get("active_project_id")
    active_project_name = config.get("active_project_name")
    local_path = config.get_local_path()

    if not local_path:
        click.echo(
            "No local project path found. Please select an existing project or create a new one using "
            "'claudesync project select' or 'claudesync project create'."
        )
        return

    submodule_detect_filenames = config.get("submodule_detect_filenames", [])
    submodules_with_files = detect_submodules(local_path, submodule_detect_filenames)

    if not submodules_with_files:
        click.echo("No submodules detected in the current project.")
        return

    # Fetch all remote projects
    all_remote_projects = provider.get_projects(
        active_organization_id, include_archived=False
    )

    click.echo(
        f"Detected {len(submodules_with_files)} submodule(s). Checking for existing remote projects:"
    )

    # Load existing local config
    local_config_path = os.path.join(local_path, ".claudesync", "config.local.json")
    with open(local_config_path, "r") as f:
        local_config = json.load(f)

    # Initialize submodules list if it doesn't exist
    if "submodules" not in local_config:
        local_config["submodules"] = []

    for i, (submodule, detected_file) in enumerate(submodules_with_files, 1):
        submodule_name = os.path.basename(submodule)
        new_project_name = f"{active_project_name}-SubModule-{submodule_name}"

        # Check if the submodule project already exists
        existing_project = next(
            (p for p in all_remote_projects if p["name"] == new_project_name), None
        )

        if existing_project:
            click.echo(
                f"{i}. Submodule '{submodule_name}' already exists as project "
                f"'{new_project_name}' (ID: {existing_project['id']}). Updating local config."
            )
            project_id = existing_project["id"]
        else:
            description = f"Submodule '{submodule_name}' for project '{active_project_name}' (ID: {active_project_id})"
            try:
                new_project = provider.create_project(
                    active_organization_id, new_project_name, description
                )
                project_id = new_project["uuid"]
                click.echo(
                    f"{i}. Created project '{new_project_name}' (ID: {project_id}) for submodule '{submodule_name}'"
                )
            except ProviderError as e:
                click.echo(
                    f"Failed to create project for submodule '{submodule_name}': {str(e)}"
                )
                continue

        # Update or add submodule information in local config
        submodule_config = {
            "active_provider": config.get("active_provider"),
            "active_organization_id": active_organization_id,
            "active_project_id": project_id,
            "active_project_name": new_project_name,
            "relative_path": submodule,
        }

        # Check if submodule already exists in config and update it, or append new entry
        submodule_index = next(
            (
                index
                for (index, d) in enumerate(local_config["submodules"])
                if d["relative_path"] == submodule
            ),
            None,
        )
        if submodule_index is not None:
            local_config["submodules"][submodule_index] = submodule_config
        else:
            local_config["submodules"].append(submodule_config)

    # Save updated local config
    with open(local_config_path, "w") as f:
        json.dump(local_config, f, indent=2)

    click.echo("\nSubmodule project creation and configuration update completed.")
```

### src/claudesync/cli/project.py

```python
import click
import os

from ..provider_factory import get_provider
from ..utils import handle_errors, validate_and_get_provider
from ..exceptions import ProviderError, ConfigurationError
from tqdm import tqdm
from .file import file
from .submodule import submodule
from ..syncmanager import retry_on_403


@click.group()
def project():
    """Manage AI projects within the active organization."""
    pass


@project.command()
@click.option(
    "--name",
    default=lambda: os.path.basename(os.getcwd()),
    prompt="Enter a title for your new project",
    help="The name of the project (defaults to current directory name)",
    show_default="current directory name",
)
@click.option(
    "--description",
    default="Project created with ClaudeSync",
    prompt="Enter the project description",
    help="The project description",
    show_default=True,
)
@click.option(
    "--local-path",
    default=lambda: os.getcwd(),
    prompt="Enter the absolute path to your local project directory",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=True),
    help="The local path for the project (defaults to current working directory)",
    show_default="current working directory",
)
@click.option(
    "--provider",
    prompt="Pick the provider to use for this project",
    type=click.Choice(["claude.ai"], case_sensitive=False),
    default="claude.ai",
    help="The provider to use for this project",
)
@click.option(
    "--organization",
    default=None,
    help="The organization ID to use for this project",
)
@click.pass_context
@handle_errors
def create(ctx, name, description, local_path, provider, organization):
    """Creates a new project for the selected provider."""
    config = ctx.obj
    provider_instance = get_provider(config, provider)

    if organization is None:
        organizations = provider_instance.get_organizations()
        organization_instance = organizations[0] if organizations else None
        organization = organization_instance["id"]

    try:
        new_project = provider_instance.create_project(organization, name, description)
        click.echo(
            f"Project '{new_project['name']}' (uuid: {new_project['uuid']}) has been created successfully."
        )

        config.set("active_provider", provider, local=True)
        config.set("active_organization_id", organization, local=True)
        config.set("active_project_id", new_project["uuid"], local=True)
        config.set("active_project_name", new_project["name"], local=True)
        config.set("local_path", local_path, local=True)

        claudesync_dir = os.path.join(local_path, ".claudesync")
        os.makedirs(claudesync_dir, exist_ok=True)
        config._save_local_config()

        click.echo(
            f"\nProject setup complete. You can now start syncing files with this project. "
            f"URL: https://claude.ai/project/{new_project['uuid']}"
        )

    except (ProviderError, ConfigurationError) as e:
        click.echo(f"Failed to create project: {str(e)}")


@project.command()
@click.pass_obj
@handle_errors
def archive(config):
    """Archive an existing project."""
    provider = validate_and_get_provider(config)
    active_organization_id = config.get("active_organization_id")
    projects = provider.get_projects(active_organization_id, include_archived=False)
    if not projects:
        click.echo("No active projects found.")
        return
    click.echo("Available projects to archive:")
    for idx, project in enumerate(projects, 1):
        click.echo(f"  {idx}. {project['name']} (ID: {project['id']})")
    selection = click.prompt("Enter the number of the project to archive", type=int)
    if 1 <= selection <= len(projects):
        selected_project = projects[selection - 1]
        if click.confirm(
            f"Are you sure you want to archive the project '{selected_project['name']}'? "
            f"Archived projects cannot be modified but can still be viewed."
        ):
            provider.archive_project(active_organization_id, selected_project["id"])
            click.echo(f"Project '{selected_project['name']}' has been archived.")
    else:
        click.echo("Invalid selection. Please try again.")


@project.command()
@click.option(
    "-a",
    "--all",
    "show_all",
    is_flag=True,
    help="Include submodule projects in the selection",
)
@click.option(
    "--provider",
    type=click.Choice(["claude.ai"]),  # Add more providers as they become available
    default="claude.ai",
    help="Specify the provider for repositories without .claudesync",
)
@click.pass_context
@handle_errors
def set(ctx, show_all, provider):
    """Set the active project for syncing."""
    config = ctx.obj

    # If provider is not specified, try to get it from the config
    if not provider:
        provider = config.get("active_provider")

    # If provider is still not available, prompt the user
    if not provider:
        provider = click.prompt(
            "Please specify the provider",
            type=click.Choice(
                ["claude.ai"]
            ),  # Add more providers as they become available
        )

    # Update the config with the provider
    config.set("active_provider", provider, local=True)

    # Now we can get the provider instance
    provider_instance = validate_and_get_provider(config)
    active_organization_id = config.get("active_organization_id")
    active_project_name = config.get("active_project_name")
    projects = provider_instance.get_projects(
        active_organization_id, include_archived=False
    )

    if show_all:
        selectable_projects = projects
    else:
        # Filter out submodule projects
        selectable_projects = [p for p in projects if "-SubModule-" not in p["name"]]

    if not selectable_projects:
        click.echo("No active projects found.")
        return

    click.echo("Available projects:")
    for idx, project in enumerate(selectable_projects, 1):
        project_type = (
            "Main Project"
            if not project["name"].startswith(f"{active_project_name}-SubModule-")
            else "Submodule"
        )
        click.echo(f"  {idx}. {project['name']} (ID: {project['id']}) - {project_type}")

    selection = click.prompt(
        "Enter the number of the project to select", type=int, default=1
    )
    if 1 <= selection <= len(selectable_projects):
        selected_project = selectable_projects[selection - 1]
        config.set("active_project_id", selected_project["id"], local=True)
        config.set("active_project_name", selected_project["name"], local=True)
        click.echo(
            f"Selected project: {selected_project['name']} (ID: {selected_project['id']})"
        )

        # Create .claudesync directory in the current working directory if it doesn't exist
        os.makedirs(".claudesync", exist_ok=True)
        click.echo(f"Ensured .claudesync directory exists in {os.getcwd()}")
    else:
        click.echo("Invalid selection. Please try again.")


@project.command()
@click.option(
    "-a",
    "--all",
    "show_all",
    is_flag=True,
    help="Include archived projects in the list",
)
@click.pass_obj
@handle_errors
def ls(config, show_all):
    """List all projects in the active organization."""
    provider = validate_and_get_provider(config)
    active_organization_id = config.get("active_organization_id")
    projects = provider.get_projects(active_organization_id, include_archived=show_all)
    if not projects:
        click.echo("No projects found.")
    else:
        click.echo("Remote projects:")
        for project in projects:
            status = " (Archived)" if project.get("archived_at") else ""
            click.echo(f"  - {project['name']} (ID: {project['id']}){status}")


@project.command()
@click.option(
    "-a", "--include-archived", is_flag=True, help="Include archived projects"
)
@click.option("-y", "--yes", is_flag=True, help="Skip confirmation prompt")
@click.pass_obj
@handle_errors
def truncate(config, include_archived, yes):
    """Truncate all projects."""
    provider = validate_and_get_provider(config)
    active_organization_id = config.get("active_organization_id")

    projects = provider.get_projects(
        active_organization_id, include_archived=include_archived
    )

    if not projects:
        click.echo("No projects found.")
        return

    if not yes:
        click.echo("This will delete ALL files from the following projects:")
        for project in projects:
            status = " (Archived)" if project.get("archived_at") else ""
            click.echo(f"  - {project['name']} (ID: {project['id']}){status}")
        if not click.confirm(
            "Are you sure you want to continue? This may take some time."
        ):
            click.echo("Operation cancelled.")
            return

    with tqdm(total=len(projects), desc="Deleting files from projects") as pbar:
        for project in projects:
            delete_files_from_project(
                provider, active_organization_id, project["id"], project["name"]
            )
            pbar.update(1)

    click.echo("All files have been deleted from all projects.")


@retry_on_403()
def delete_files_from_project(provider, organization_id, project_id, project_name):
    try:
        files = provider.list_files(organization_id, project_id)
        with tqdm(
            total=len(files), desc=f"Deleting files from {project_name}", leave=False
        ) as file_pbar:
            for current_file in files:
                provider.delete_file(organization_id, project_id, current_file["uuid"])
                file_pbar.update(1)
    except ProviderError as e:
        click.echo(f"Error deleting files from project {project_name}: {str(e)}")


project.add_command(submodule)
project.add_command(file)

__all__ = ["project"]
```

### src/claudesync/cli/__init__.py

```python
from .main import cli

__all__ = ["cli"]
```

### src/claudesync/cli/organization.py

```python
import click
from ..utils import handle_errors, validate_and_get_provider


@click.group()
def organization():
    """Manage AI organizations."""
    pass


@organization.command()
@click.pass_obj
@handle_errors
def ls(config):
    """List all available organizations with required capabilities."""
    provider = validate_and_get_provider(config, require_org=False)
    organizations = provider.get_organizations()
    if not organizations:
        click.echo(
            "No organizations with required capabilities (chat and claude_pro) found."
        )
    else:
        click.echo("Available organizations with required capabilities:")
        for idx, org in enumerate(organizations, 1):
            click.echo(f"  {idx}. {org['name']} (ID: {org['id']})")


@organization.command()
@click.option("--org-id", help="ID of the organization to set as active")
@click.option(
    "--provider",
    type=click.Choice(["claude.ai"]),  # Add more providers as they become available
    default="claude.ai",
    help="Specify the provider for repositories without .claudesync",
)
@click.pass_context
@handle_errors
def set(ctx, org_id, provider):
    """Set the active organization."""
    config = ctx.obj

    # If provider is not specified, try to get it from the config
    if not provider:
        provider = config.get("active_provider")

    # If provider is still not available, prompt the user
    if not provider:
        provider = click.prompt(
            "Please specify the provider",
            type=click.Choice(
                ["claude.ai"]
            ),  # Add more providers as they become available
        )

    # Update the config with the provider
    config.set("active_provider", provider, local=True)

    # Now we can get the provider instance
    provider_instance = validate_and_get_provider(config, require_org=False)
    organizations = provider_instance.get_organizations()

    if not organizations:
        click.echo("No organizations with required capabilities found.")
        return

    if org_id:
        selected_org = next((org for org in organizations if org["id"] == org_id), None)
        if selected_org:
            config.set("active_organization_id", selected_org["id"], local=True)
            click.echo(
                f"Selected organization: {selected_org['name']} (ID: {selected_org['id']})"
            )
        else:
            click.echo(f"Organization with ID {org_id} not found.")
    else:
        click.echo("Available organizations:")
        for idx, org in enumerate(organizations, 1):
            click.echo(f"  {idx}. {org['name']} (ID: {org['id']})")
        selection = click.prompt(
            "Enter the number of the organization you want to work with",
            type=int,
            default=1,
        )
        if 1 <= selection <= len(organizations):
            selected_org = organizations[selection - 1]
            config.set("active_organization_id", selected_org["id"], local=True)
            click.echo(
                f"Selected organization: {selected_org['name']} (ID: {selected_org['id']})"
            )
        else:
            click.echo("Invalid selection. Please try again.")

    # Clear project-related settings when changing organization
    config.set("active_project_id", None, local=True)
    config.set("active_project_name", None, local=True)
    click.echo(
        "Project settings cleared. Please select or create a new project for this organization."
    )
```

### src/claudesync/cli/main.py

```python
from pathlib import Path

import click
import click_completion
import click_completion.core
import json
import subprocess
import urllib.request
from pkg_resources import get_distribution

from claudesync.cli.chat import chat
from claudesync.configmanager import FileConfigManager, InMemoryConfigManager
from claudesync.syncmanager import SyncManager
from claudesync.utils import (
    handle_errors,
    validate_and_get_provider,
    get_local_files,
)
from .auth import auth
from .organization import organization
from .project import project
from .sync import schedule
from .config import config
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

click_completion.init()


@click.group()
@click.pass_context
def cli(ctx):
    """ClaudeSync: Synchronize local files with AI projects."""
    if ctx.obj is None:
        ctx.obj = FileConfigManager()  # InMemoryConfigManager() for testing with mock


@cli.command()
@click.argument(
    "shell", required=False, type=click.Choice(["bash", "zsh", "fish", "powershell"])
)
def install_completion(shell):
    """Install completion for the specified shell."""
    if shell is None:
        shell = click_completion.get_auto_shell()
        click.echo("Shell is set to '%s'" % shell)
    click_completion.install(shell=shell)
    click.echo("Completion installed.")


@cli.command()
@click.pass_context
def upgrade(ctx):
    """Upgrade ClaudeSync to the latest version and reset configuration, preserving sessionKey."""
    config = ctx.obj
    current_version = get_distribution("claudesync").version

    # Check for the latest version
    try:
        with urllib.request.urlopen(
            "https://pypi.org/pypi/claudesync/json"
        ) as response:
            data = json.loads(response.read())
            latest_version = data["info"]["version"]

        if current_version == latest_version:
            click.echo(
                f"You are already on the latest version of ClaudeSync (v{current_version})."
            )
            return
    except Exception as e:
        click.echo(f"Unable to check for the latest version: {str(e)}")
        click.echo("Proceeding with the upgrade process.")

    session_key = config.get_session_key()
    session_key_expiry = config.get("session_key_expiry")

    # Upgrade ClaudeSync
    click.echo(f"Upgrading ClaudeSync from v{current_version} to v{latest_version}...")
    try:
        subprocess.run(["pip", "install", "--upgrade", "claudesync"], check=True)
        click.echo("ClaudeSync has been successfully upgraded.")
    except subprocess.CalledProcessError:
        click.echo(
            "Failed to upgrade ClaudeSync. Please try manually: pip install --upgrade claudesync"
        )

    # Preserve the session key and its expiry
    if session_key and session_key_expiry:
        config.set_session_key(session_key, session_key_expiry)
        click.echo("Session key preserved in the new configuration.")
    else:
        click.echo("No valid session key found in the old configuration.")

    # Inform user about the upgrade process
    click.echo("\nUpgrade process completed:")
    click.echo(
        f"1. ClaudeSync has been upgraded from v{current_version} to v{latest_version}."
    )
    click.echo("2. Your session key has been preserved (if it existed and was valid).")
    click.echo(
        "\nPlease run 'claudesync auth login' to complete your configuration setup if needed."
    )


@cli.command()
@click.option("--category", help="Specify the file category to sync")
@click.option(
    "--uberproject", is_flag=True, help="Include submodules in the parent project sync"
)
@click.pass_obj
@handle_errors
def push(config, category, uberproject):
    """Synchronize the project files, optionally including submodules in the parent project."""
    provider = validate_and_get_provider(config, require_project=True)

    if not category:
        category = config.get_default_category()
        if category:
            click.echo(f"Using default category: {category}")

    active_organization_id = config.get("active_organization_id")
    active_project_id = config.get("active_project_id")
    active_project_name = config.get("active_project_name")
    local_path = config.get_local_path()

    if not local_path:
        click.echo(
            "No .claudesync directory found in this directory or any parent directories. "
            "Please run 'claudesync project create' or 'claudesync project set' first."
        )
        return

    # Detect if we're in a submodule
    current_dir = Path.cwd()
    submodules = config.get("submodules", [])
    current_submodule = next(
        (
            sm
            for sm in submodules
            if Path(local_path) / sm["relative_path"] == current_dir
        ),
        None,
    )

    if current_submodule:
        # We're in a submodule, so only sync this submodule
        click.echo(
            f"Syncing submodule {current_submodule['active_project_name']} [{current_dir}]"
        )
        sync_submodule(provider, config, current_submodule, category)
    else:
        # Sync main project
        sync_manager = SyncManager(provider, config, config.get_local_path())
        remote_files = provider.list_files(active_organization_id, active_project_id)

        if uberproject:
            # Include submodule files in the parent project
            local_files = get_local_files(
                config, local_path, category, include_submodules=True
            )
        else:
            # Exclude submodule files from the parent project
            local_files = get_local_files(
                config, local_path, category, include_submodules=False
            )

        sync_manager.sync(local_files, remote_files)
        click.echo(
            f"Main project '{active_project_name}' synced successfully: https://claude.ai/project/{active_project_id}"
        )

        # Always sync submodules to their respective projects
        for submodule in submodules:
            sync_submodule(provider, config, submodule, category)


def sync_submodule(provider, config, submodule, category):
    submodule_path = Path(config.get_local_path()) / submodule["relative_path"]
    submodule_files = get_local_files(config, str(submodule_path), category)
    remote_submodule_files = provider.list_files(
        submodule["active_organization_id"], submodule["active_project_id"]
    )

    # Create a new ConfigManager instance for the submodule
    submodule_config = InMemoryConfigManager()
    submodule_config.load_from_file_config(config)
    submodule_config.set(
        "active_project_id", submodule["active_project_id"], local=True
    )
    submodule_config.set(
        "active_project_name", submodule["active_project_name"], local=True
    )

    # Create a new SyncManager for the submodule
    submodule_sync_manager = SyncManager(
        provider, submodule_config, str(submodule_path)
    )

    submodule_sync_manager.sync(submodule_files, remote_submodule_files)
    click.echo(
        f"Submodule '{submodule['active_project_name']}' synced successfully: "
        f"https://claude.ai/project/{submodule['active_project_id']}"
    )


cli.add_command(auth)
cli.add_command(organization)
cli.add_command(project)
cli.add_command(schedule)
cli.add_command(config)
cli.add_command(chat)

if __name__ == "__main__":
    cli()
```

### src/claudesync/configmanager/inmemory_config_manager.py

```python
from datetime import datetime

from claudesync.configmanager import BaseConfigManager


class InMemoryConfigManager(BaseConfigManager):
    """
    A configuration manager that stores configuration settings entirely in memory.

    This class provides an in-memory implementation of the BaseConfigManager, meaning that
    all configuration data is stored in Python dictionaries and does not persist between
    program runs.
    """

    def __init__(self):
        """
        Initializes the in-memory configuration manager with default settings.
        """
        super().__init__()
        self.session_keys = {}

    def _load_global_config(self):
        """
        Loads the global configuration settings.

        Since this is an in-memory implementation, this method doesn't load from any external source.
        Instead, it relies on the initial in-memory defaults or previous modifications made during runtime.
        """
        # No action needed for in-memory implementation
        pass

    def _load_local_config(self):
        """
        Loads the local configuration settings.

        Since this is an in-memory implementation, this method doesn't load from any external source.
        """
        # No action needed for in-memory implementation
        pass

    def _save_global_config(self):
        """
        Saves the global configuration settings.

        Since this is an in-memory implementation, this method doesn't save to any external destination.
        """
        # No action needed for in-memory implementation
        pass

    def _save_local_config(self):
        """
        Saves the local configuration settings.

        Since this is an in-memory implementation, this method doesn't save to any external destination.
        """
        # No action needed for in-memory implementation
        pass

    def set(self, key, value, local=False):
        """
        Sets a configuration value in the in-memory store.

        Args:
            key (str): The key of the configuration setting to set.
            value: The value to associate with the given key.
            local (bool): Whether to set the configuration in the local context.
                          If False, the setting is stored in the global context.
                          Default is False.
        """
        if local:
            self.local_config[key] = value
        else:
            self.global_config[key] = value

    def get(self, key, default=None):
        """
        Retrieves a configuration value from the in-memory store.

        Args:
            key (str): The key of the configuration setting to retrieve.
            default: The default value to return if the key is not found.
                     Default is None.

        Returns:
            The value associated with the given key, or the default value if the key
            does not exist.
        """
        return self.local_config.get(key, self.global_config.get(key, default))

    def _find_local_config_dir(self):
        """
        Finds the local configuration directory.

        Returns:
            None: Since this is an in-memory implementation, there is no local configuration directory.
        """
        return None

    def set_session_key(self, provider, session_key, expiry):
        self.session_keys[provider] = {"session_key": session_key, "expiry": expiry}

    def get_session_key(self, provider):
        if provider in self.session_keys:
            data = self.session_keys[provider]
            if datetime.now() < data["expiry"]:
                return data["session_key"], data["expiry"]
        return None, None

    def load_from_file_config(self, file_config_manager):
        self.global_config = file_config_manager.global_config.copy()
        self.local_config = file_config_manager.local_config.copy()

        # Copy session keys
        if hasattr(file_config_manager, "session_keys"):
            self.session_keys = file_config_manager.session_keys.copy()
        else:
            # If FileConfigManager doesn't have session_keys attribute,
            # we need to manually copy the session keys
            for provider in file_config_manager.get_providers_with_session_keys():
                session_key, expiry = file_config_manager.get_session_key(provider)
                if session_key and expiry:
                    self.set_session_key(provider, session_key, expiry)

    def get_active_provider(self):
        """
        Retrieves the active provider from the local configuration.

        Returns:
            str: The name of the active provider, or None if not set.
        """
        return self.local_config.get("active_provider")

    def get_local_path(self):
        return "."
```

### src/claudesync/configmanager/base_config_manager.py

```python
from abc import ABC, abstractmethod
import copy


class BaseConfigManager(ABC):
    """
    Abstract base class for managing configuration settings.

    This class defines the interface for configuration management and includes
    common functionality that can be shared across different implementations,
    such as file-based and in-memory configurations.
    """

    def __init__(self):
        """
        Initializes the configuration manager with empty global and local configurations.

        - `global_config`: A dictionary to store global configuration settings that apply
          universally across all environments.
        - `local_config`: A dictionary to store local configuration settings specific to
          the current environment or project.
        """
        self.global_config = {}
        self.local_config = {}

    def _get_default_config(self):
        """
        Returns the default configuration dictionary.

        This method centralizes the default configuration settings, making it easier to manage and update defaults.

        Returns:
            dict: The default configuration settings.
        """
        return {
            "log_level": "INFO",
            "upload_delay": 0.5,
            "max_file_size": 32 * 1024,
            "two_way_sync": False,
            "prune_remote_files": True,
            "claude_api_url": "https://api.claude.ai/api",
            "compression_algorithm": "none",
            "submodule_detect_filenames": [
                "pom.xml",
                "build.gradle",
                "package.json",
                "setup.py",
                "Cargo.toml",
                "go.mod",
            ],
            "file_categories": {
                "all_files": {
                    "description": "All files not ignored",
                    "patterns": ["*"],
                },
                "all_source_code": {
                    "description": "All source code files",
                    "patterns": [
                        "*.java",
                        "*.py",
                        "*.js",
                        "*.ts",
                        "*.c",
                        "*.cpp",
                        "*.h",
                        "*.hpp",
                        "*.go",
                        "*.rs",
                    ],
                },
                "production_code": {
                    "description": "Production source code",
                    "patterns": [
                        "**/src/**/*.java",
                        "**/*.py",
                        "**/*.js",
                        "**/*.ts",
                        "**/*.vue",
                    ],
                },
                "test_code": {
                    "description": "Test source code",
                    "patterns": [
                        "**/test/**/*.java",
                        "**/tests/**/*.py",
                        "**/test_*.py",
                        "**/*Test.java",
                    ],
                },
                "build_config": {
                    "description": "Build configuration files",
                    "patterns": [
                        "**/pom.xml",
                        "**/build.gradle",
                        "**/package.json",
                        "**/setup.py",
                        "**/Cargo.toml",
                        "**/go.mod",
                        "**/pyproject.toml",
                        "**/requirements.txt",
                        "**/*.tf",
                        "**/*.yaml",
                        "**/*.yml",
                        "**/*.properties",
                    ],
                },
                "uberproject_java": {
                    "description": "Uberproject Java + Javascript",
                    "patterns": [
                        "**/src/**/*.java",
                        "**/*.py",
                        "**/*.js",
                        "**/*.ts",
                        "**/*.vue",
                        "**/pom.xml",
                        "**/build.gradle",
                        "**/package.json",
                        "**/setup.py",
                        "**/Cargo.toml",
                        "**/go.mod",
                        "**/pyproject.toml",
                        "**/requirements.txt",
                        "**/*.tf",
                        "**/*.yaml",
                        "**/*.yml",
                        "**/*.properties",
                    ],
                },
            },
        }

    @abstractmethod
    def _load_global_config(self):
        """
        Loads the global configuration settings.

        This method should be implemented by subclasses to load the global configuration
        from the appropriate source (e.g., a file or an in-memory structure).
        """
        pass

    @abstractmethod
    def _load_local_config(self):
        """
        Loads the local configuration settings.

        This method should be implemented by subclasses to load the local configuration
        from the appropriate source (e.g., a file or an in-memory structure).
        """
        pass

    @abstractmethod
    def _save_global_config(self):
        """
        Saves the global configuration settings.

        This method should be implemented by subclasses to save the global configuration
        to the appropriate destination (e.g., a file or an in-memory structure).
        """
        pass

    @abstractmethod
    def _save_local_config(self):
        """
        Saves the local configuration settings.

        This method should be implemented by subclasses to save the local configuration
        to the appropriate destination (e.g., a file or an in-memory structure).
        """
        pass

    @abstractmethod
    def set(self, key, value, local=False):
        """
        Sets a configuration value.

        Args:
            key (str): The key of the configuration setting to set.
            value: The value to associate with the given key.
            local (bool): Whether to set the configuration in the local context.
                          If False, the setting is stored in the global context.
                          Default is False.

        This method should be implemented by subclasses to handle the setting of
        configuration values, either globally or locally.
        """
        pass

    @abstractmethod
    def get(self, key, default=None):
        """
        Retrieves a configuration value.

        Args:
            key (str): The key of the configuration setting to retrieve.
            default: The default value to return if the key is not found.
                     Default is None.

        Returns:
            The value associated with the given key, or the default value if the key
            does not exist.

        This method should be implemented by subclasses to retrieve configuration
        values, checking the local context first, then the global context.
        """
        pass

    @abstractmethod
    def _find_local_config_dir(self):
        """
        Finds the local configuration directory.

        Returns:
            Path: The path to the local configuration directory, or None if no
            directory is found.

        This method should be implemented by subclasses to locate the directory where
        local configuration files are stored.
        """
        pass

    # Common methods that are shared between implementations
    def get_default_category(self):
        """
        Retrieves the default synchronization category.

        Returns:
            str: The default synchronization category, as specified in the configuration.
        """
        return self.get("default_sync_category")

    def set_default_category(self, category):
        """
        Sets the default synchronization category.

        Args:
            category (str): The category to set as the default for synchronization.
        """
        self.set("default_sync_category", category, local=True)

    def copy(self):
        """
        Creates a deep copy of the configuration manager.

        Returns:
            BaseConfigManager: A new instance of the configuration manager with
                               a deep copy of the global and local configurations.

        This method is useful when you need to duplicate the current state of the
        configuration manager, preserving the settings in a new instance.
        """
        new_instance = self.__class__()
        new_instance.global_config = copy.deepcopy(self.global_config)
        new_instance.local_config = copy.deepcopy(self.local_config)
        return new_instance
```

### src/claudesync/configmanager/file_config_manager.py

```python
import json
import logging
import os
from datetime import datetime
from pathlib import Path

from claudesync.configmanager.base_config_manager import BaseConfigManager
from claudesync.session_key_manager import SessionKeyManager


class FileConfigManager(BaseConfigManager):
    """
    Manages the configuration for ClaudeSync, handling both global and local (project-specific) settings.

    This class provides methods to load, save, and access configuration settings from both
    a global configuration file (~/.claudesync/config.json) and a local configuration file
    (.claudesync/config.local.json) in the project directory. Session keys are stored separately
    in provider-specific files.
    """

    def __init__(self):
        """
        Initialize the ConfigManager.

        Sets up paths for global and local configuration files and loads both configurations.
        """
        super().__init__()
        self.global_config_dir = Path.home() / ".claudesync"
        self.global_config_file = self.global_config_dir / "config.json"
        self.global_config = self._load_global_config()
        self.local_config = {}
        self.local_config_dir = None
        self._load_local_config()

    def _load_global_config(self):
        """
        Loads the global configuration from the JSON file.

        If the configuration file doesn't exist, it creates the directory (if necessary)
        and returns the default configuration.

        Returns:
            dict: The loaded global configuration with default values for missing keys.
        """
        if not self.global_config_file.exists():
            self.global_config_dir.mkdir(parents=True, exist_ok=True)
            return self._get_default_config()

        with open(self.global_config_file, "r") as f:
            config = json.load(f)
            defaults = self._get_default_config()
            for key, value in defaults.items():
                if key not in config:
                    config[key] = value
            return config

    def _find_local_config_dir(self, max_depth=100):
        """
        Finds the nearest directory containing a .claudesync folder.

        Searches from the current working directory upwards until it finds a .claudesync folder
        or reaches the root directory. Excludes the ~/.claudesync directory.

        Returns:
            Path: The path containing the .claudesync folder, or None if not found.
        """
        current_dir = Path.cwd()
        root_dir = Path(current_dir.root)
        home_dir = Path.home()
        depth = 0  # Initialize depth counter

        while current_dir != root_dir:
            claudesync_dir = current_dir / ".claudesync"
            if claudesync_dir.is_dir() and claudesync_dir != home_dir / ".claudesync":
                return current_dir

            current_dir = current_dir.parent
            depth += 1  # Increment depth counter

            # Sanity check: stop if max_depth is reached
            if depth > max_depth:
                return None

        return None

    def _load_local_config(self):
        """
        Loads the local configuration from the nearest .claudesync/config.local.json file.

        Sets the local_config_dir and populates the local_config dictionary.
        """
        self.local_config_dir = self._find_local_config_dir()
        if self.local_config_dir:
            local_config_file = (
                self.local_config_dir / ".claudesync" / "config.local.json"
            )
            if local_config_file.exists():
                with open(local_config_file, "r") as f:
                    self.local_config = json.load(f)

    def get_local_path(self):
        """
        Retrieves the path of the directory containing the .claudesync folder.

        Returns:
            str: The path of the directory containing the .claudesync folder, or None if not found.
        """
        return str(self.local_config_dir) if self.local_config_dir else None

    def get(self, key, default=None):
        """
        Retrieves a configuration value.

        Checks the local configuration first, then falls back to the global configuration.

        Args:
            key (str): The key for the configuration setting to retrieve.
            default (any, optional): The default value to return if the key is not found. Defaults to None.

        Returns:
            The value of the configuration setting if found, otherwise the default value.
        """
        return self.local_config.get(key) or self.global_config.get(key, default)

    def set(self, key, value, local=False):
        """
        Sets a configuration value and saves the configuration.

        Args:
            key (str): The key for the configuration setting to set.
            value (any): The value to set for the given key.
            local (bool): If True, sets the value in the local configuration. Otherwise, sets it in the global configuration.
        """
        if local:
            if not self.local_config_dir:
                self.local_config_dir = Path.cwd()
                (self.local_config_dir / ".claudesync").mkdir(exist_ok=True)
            self.local_config[key] = value
            self._save_local_config()
        else:
            self.global_config[key] = value
            self._save_global_config()

    def _save_global_config(self):
        """
        Saves the current global configuration to the JSON file.

        This method writes the current state of the `global_config` attribute to the configuration file,
        pretty-printing the JSON for readability.
        """
        with open(self.global_config_file, "w") as f:
            json.dump(self.global_config, f, indent=2)

    def _save_local_config(self):
        """
        Saves the current local configuration to the .claudesync/config.local.json file.
        """
        if self.local_config_dir:
            local_config_file = (
                self.local_config_dir / ".claudesync" / "config.local.json"
            )
            with open(local_config_file, "w") as f:
                json.dump(self.local_config, f, indent=2)

    def set_session_key(self, provider, session_key, expiry):
        """
        Sets the session key and its expiry for a specific provider.

        Args:
            provider (str): The name of the provider.
            session_key (str): The session key to set.
            expiry (datetime): The expiry datetime for the session key.
        """
        try:
            session_key_manager = SessionKeyManager()
            encrypted_session_key, encryption_method = (
                session_key_manager.encrypt_session_key(provider, session_key)
            )

            self.global_config_dir.mkdir(parents=True, exist_ok=True)
            provider_key_file = self.global_config_dir / f"{provider}.key"
            with open(provider_key_file, "w") as f:
                json.dump(
                    {
                        "session_key": encrypted_session_key,
                        "session_key_encryption_method": encryption_method,
                        "session_key_expiry": expiry.isoformat(),
                    },
                    f,
                )
        except RuntimeError as e:
            logging.error(f"Failed to encrypt session key: {str(e)}")
            raise

    def get_session_key(self, provider):
        """
        Retrieves the session key for the specified provider if it's still valid.

        Args:
            provider (str): The name of the provider.

        Returns:
            tuple: A tuple containing the session key and expiry if valid, (None, None) otherwise.
        """
        provider_key_file = self.global_config_dir / f"{provider}.key"
        if not provider_key_file.exists():
            return None, None

        with open(provider_key_file, "r") as f:
            data = json.load(f)

        encrypted_key = data.get("session_key")
        encryption_method = data.get("session_key_encryption_method")
        expiry_str = data.get("session_key_expiry")

        if not encrypted_key or not expiry_str:
            return None, None

        expiry = datetime.fromisoformat(expiry_str)
        if datetime.now() > expiry:
            return None, None

        try:
            session_key_manager = SessionKeyManager()
            session_key = session_key_manager.decrypt_session_key(
                provider, encryption_method, encrypted_key
            )
            return session_key, expiry
        except RuntimeError as e:
            logging.error(f"Failed to decrypt session key: {str(e)}")
            return None, None

    def add_file_category(self, category_name, description, patterns):
        """
        Adds a new file category to the global configuration.

        Args:
            category_name (str): The name of the category to add.
            description (str): A description of the category.
            patterns (list): A list of file patterns for the category.
        """
        if "file_categories" not in self.global_config:
            self.global_config["file_categories"] = {}
        self.global_config["file_categories"][category_name] = {
            "description": description,
            "patterns": patterns,
        }
        self._save_global_config()

    def remove_file_category(self, category_name):
        """
        Removes a file category from the global configuration.

        Args:
            category_name (str): The name of the category to remove.
        """
        if (
            "file_categories" in self.global_config
            and category_name in self.global_config["file_categories"]
        ):
            del self.global_config["file_categories"][category_name]
            self._save_global_config()

    def update_file_category(self, category_name, description=None, patterns=None):
        """
        Updates an existing file category in the global configuration.

        Args:
            category_name (str): The name of the category to update.
            description (str, optional): The new description for the category. If None, the description is not updated.
            patterns (list, optional): The new list of file patterns for the category. If None, the patterns are not updated.
        """
        if (
            "file_categories" in self.global_config
            and category_name in self.global_config["file_categories"]
        ):
            if description is not None:
                self.global_config["file_categories"][category_name][
                    "description"
                ] = description
            if patterns is not None:
                self.global_config["file_categories"][category_name][
                    "patterns"
                ] = patterns
            self._save_global_config()

    def clear_all_session_keys(self):
        """
        Removes all stored session keys.
        """
        for file in self.global_config_dir.glob("*.key"):
            os.remove(file)

    def get_active_provider(self):
        """
        Retrieves the active provider from the local configuration.

        Returns:
            str: The name of the active provider, or None if not set.
        """
        return self.local_config.get("active_provider")

    def get_providers_with_session_keys(self):
        """
        Retrieves a list of providers that have valid session keys.

        Returns:
            list: A list of provider names with valid session keys.
        """
        providers = []
        for file in self.global_config_dir.glob("*.key"):
            provider = file.stem
            session_key, expiry = self.get_session_key(provider)
            if session_key and expiry > datetime.now():
                providers.append(provider)
        return providers
```

### src/claudesync/configmanager/__init__.py

```python
from .base_config_manager import BaseConfigManager
from .file_config_manager import FileConfigManager
from .inmemory_config_manager import InMemoryConfigManager

__all__ = ["BaseConfigManager", "FileConfigManager", "InMemoryConfigManager"]
```

### src/claudesync/providers/claude_ai.py

```python
import urllib.request
import urllib.error
import urllib.parse
import json
import gzip
from datetime import datetime, timezone
from .base_claude_ai import BaseClaudeAIProvider
from ..exceptions import ProviderError


class ClaudeAIProvider(BaseClaudeAIProvider):
    def __init__(self, config=None):
        super().__init__(config)

    def _make_request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip",
        }

        session_key, expiry = self.config.get_session_key("claude.ai")
        cookies = {
            "sessionKey": session_key,
        }

        try:
            self.logger.debug(f"Making {method} request to {url}")
            self.logger.debug(f"Headers: {headers}")
            self.logger.debug(f"Cookies: {cookies}")
            if data:
                self.logger.debug(f"Request data: {data}")

            # Prepare the request
            req = urllib.request.Request(url, method=method)
            for key, value in headers.items():
                req.add_header(key, value)

            # Add cookies
            cookie_string = "; ".join([f"{k}={v}" for k, v in cookies.items()])
            req.add_header("Cookie", cookie_string)

            # Add data if present
            if data:
                json_data = json.dumps(data).encode("utf-8")
                req.data = json_data

            # Make the request
            with urllib.request.urlopen(req) as response:
                self.logger.debug(f"Response status code: {response.status}")
                self.logger.debug(f"Response headers: {response.headers}")

                # Handle gzip encoding
                if response.headers.get("Content-Encoding") == "gzip":
                    content = gzip.decompress(response.read())
                else:
                    content = response.read()

                content_str = content.decode("utf-8")
                self.logger.debug(f"Response content: {content_str[:1000]}...")

                if not content:
                    return None

                return json.loads(content_str)

        except urllib.error.HTTPError as e:
            self.handle_http_error(e)
        except urllib.error.URLError as e:
            self.logger.error(f"URL Error: {str(e)}")
            raise ProviderError(f"API request failed: {str(e)}")
        except json.JSONDecodeError as json_err:
            self.logger.error(f"Failed to parse JSON response: {str(json_err)}")
            self.logger.error(f"Response content: {content_str}")
            raise ProviderError(f"Invalid JSON response from API: {str(json_err)}")

    def handle_http_error(self, e):
        self.logger.debug(f"Request failed: {str(e)}")
        self.logger.debug(f"Response status code: {e.code}")
        self.logger.debug(f"Response headers: {e.headers}")

        try:
            # Check if the content is gzip-encoded
            if e.headers.get("Content-Encoding") == "gzip":
                content = gzip.decompress(e.read())
            else:
                content = e.read()

            # Try to decode the content as UTF-8
            content_str = content.decode("utf-8")
        except UnicodeDecodeError:
            # If UTF-8 decoding fails, try to decode as ISO-8859-1
            content_str = content.decode("iso-8859-1")

        self.logger.debug(f"Response content: {content_str}")

        if e.code == 403:
            error_msg = "Received a 403 Forbidden error."
            raise ProviderError(error_msg)
        elif e.code == 429:
            try:
                error_data = json.loads(content_str)
                resets_at_unix = json.loads(error_data["error"]["message"])["resetsAt"]
                resets_at_local = datetime.fromtimestamp(
                    resets_at_unix, tz=timezone.utc
                ).astimezone()
                formatted_time = resets_at_local.strftime("%a %b %d %Y %H:%M:%S %Z%z")
                error_msg = f"Message limit exceeded. Try again after {formatted_time}"
            except (KeyError, json.JSONDecodeError) as parse_error:
                error_msg = f"HTTP 429: Too Many Requests. Failed to parse error response: {parse_error}"
            self.logger.error(error_msg)
            raise ProviderError(error_msg)
        else:
            error_msg = f"API request failed with status code {e.code}: {content_str}"
            self.logger.error(error_msg)
            raise ProviderError(error_msg)

    def _make_request_stream(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        session_key, _ = self.config.get_session_key("claude.ai")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
            "Content-Type": "application/json",
            "Accept": "text/event-stream",
            "Cookie": f"sessionKey={session_key}",
        }

        req = urllib.request.Request(url, method=method, headers=headers)
        if data:
            req.data = json.dumps(data).encode("utf-8")

        try:
            return urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            self.handle_http_error(e)
        except urllib.error.URLError as e:
            raise ProviderError(f"API request failed: {str(e)}")
```

### src/claudesync/providers/base_provider.py

```python
# src/claudesync/providers/base_provider.py

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    @abstractmethod
    def login(self):
        """Authenticate with the provider and return a session key."""
        pass

    @abstractmethod
    def get_organizations(self):
        """Retrieve a list of organizations the user is a member of."""
        pass

    @abstractmethod
    def get_projects(self, organization_id, include_archived=False):
        """Retrieve a list of projects for a specified organization."""
        pass

    @abstractmethod
    def list_files(self, organization_id, project_id):
        """List all files within a specified project and organization."""
        pass

    @abstractmethod
    def upload_file(self, organization_id, project_id, file_name, content):
        """Upload a file to a specified project within an organization."""
        pass

    @abstractmethod
    def delete_file(self, organization_id, project_id, file_uuid):
        """Delete a file from a specified project within an organization."""
        pass

    @abstractmethod
    def archive_project(self, organization_id, project_id):
        """Archive a specified project within an organization."""
        pass

    @abstractmethod
    def create_project(self, organization_id, name, description=""):
        """Create a new project within a specified organization."""
        pass

    @abstractmethod
    def get_chat_conversations(self, organization_id):
        """Retrieve a list of chat conversations for a specified organization."""
        pass

    @abstractmethod
    def get_published_artifacts(self, organization_id):
        """Retrieve a list of published artifacts for a specified organization."""
        pass

    @abstractmethod
    def get_chat_conversation(self, organization_id, conversation_id):
        """Retrieve the full content of a specific chat conversation."""
        pass

    @abstractmethod
    def get_artifact_content(self, organization_id, artifact_uuid):
        """Retrieve the full content of a specific published artifact."""
        pass

    @abstractmethod
    def delete_chat(self, organization_id, conversation_uuids):
        """Delete specified chats for a given organization."""
        pass

    @abstractmethod
    def create_chat(self, organization_id, chat_name="", project_uuid=None):
        """Create a new chat conversation in the specified organization."""
        pass

    @abstractmethod
    def send_message(self, organization_id, chat_id, prompt, timezone="UTC"):
        """Send a message to a specified chat conversation."""
        pass
```

### src/claudesync/providers/base_claude_ai.py

```python
import datetime
import json
import logging
import urllib
import sseclient

import click
from .base_provider import BaseProvider
from ..configmanager import FileConfigManager, InMemoryConfigManager
from ..exceptions import ProviderError


def is_url_encoded(s):
    decoded_s = urllib.parse.unquote(s)
    return decoded_s != s


def _get_session_key_expiry():
    while True:
        date_format = "%a, %d %b %Y %H:%M:%S %Z"
        default_expires = datetime.datetime.now(
            datetime.timezone.utc
        ) + datetime.timedelta(days=30)
        formatted_expires = default_expires.strftime(date_format).strip()
        expires = click.prompt(
            "Please enter the expires time for the sessionKey (optional)",
            default=formatted_expires,
            type=str,
        ).strip()
        try:
            expires_on = datetime.datetime.strptime(expires, date_format)
            return expires_on
        except ValueError:
            click.echo(
                "The entered date does not match the required format. Please try again."
            )


class BaseClaudeAIProvider(BaseProvider):
    def __init__(self, config=None):
        self.config = config
        if self.config is None:
            self.config = InMemoryConfigManager()
            self.config.load_from_file_config(
                FileConfigManager()
            )  # a provider may not edit the config
        self.logger = logging.getLogger(__name__)
        self._configure_logging()

    @property
    def base_url(self):
        return self.config.get("claude_api_url", "https://api.claude.ai/api")

    def _configure_logging(self):
        log_level = self.config.get("log_level", "INFO")
        logging.basicConfig(level=getattr(logging, log_level))
        self.logger.setLevel(getattr(logging, log_level))

    def login(self):
        click.echo(
            "A session key is required to call: " + self.config.get("claude_api_url")
        )
        click.echo("To obtain your session key, please follow these steps:")
        click.echo("1. Open your web browser and go to https://claude.ai")
        click.echo("2. Log in to your Claude account if you haven't already")
        click.echo("3. Once logged in, open your browser's developer tools:")
        click.echo("   - Chrome/Edge: Press F12 or Ctrl+Shift+I (Cmd+Option+I on Mac)")
        click.echo("   - Firefox: Press F12 or Ctrl+Shift+I (Cmd+Option+I on Mac)")
        click.echo(
            "   - Safari: Enable developer tools in Preferences > Advanced, then press Cmd+Option+I"
        )
        click.echo(
            "4. In the developer tools, go to the 'Application' tab (Chrome/Edge) or 'Storage' tab (Firefox)"
        )
        click.echo(
            "5. In the left sidebar, expand 'Cookies' and select 'https://claude.ai'"
        )
        click.echo(
            "6. Locate the cookie named 'sessionKey' and copy its value. "
            "Ensure that the value is not URL-encoded."
        )

        while True:
            session_key = click.prompt(
                "Please enter your sessionKey", type=str, hide_input=True
            )
            if not session_key.startswith("sk-ant"):
                click.echo(
                    "Invalid sessionKey format. Please make sure it starts with 'sk-ant'."
                )
                continue
            if is_url_encoded(session_key):
                click.echo(
                    "The session key appears to be URL-encoded. Please provide the decoded version."
                )
                continue

            expires = _get_session_key_expiry()
            try:
                self.config.set_session_key("claude.ai", session_key, expires)
                organizations = self.get_organizations()
                if organizations:
                    return session_key, expires  # Return the session key and expiry
            except ProviderError as e:
                click.echo(e)
                click.echo(
                    "Failed to retrieve organizations. Please enter a valid sessionKey."
                )

        # This line should never be reached, but we'll add it for completeness
        raise ProviderError("Failed to authenticate after multiple attempts")

    def get_organizations(self):
        response = self._make_request("GET", "/organizations")
        if not response:
            raise ProviderError("Unable to retrieve organization information")
        return [
            {"id": org["uuid"], "name": org["name"]}
            for org in response
            if (
                {"chat", "claude_pro"}.issubset(set(org.get("capabilities", [])))
                or {"chat", "raven"}.issubset(set(org.get("capabilities", [])))
            )
        ]

    def get_projects(self, organization_id, include_archived=False):
        response = self._make_request(
            "GET", f"/organizations/{organization_id}/projects"
        )
        projects = [
            {
                "id": project["uuid"],
                "name": project["name"],
                "archived_at": project.get("archived_at"),
            }
            for project in response
            if include_archived or project.get("archived_at") is None
        ]
        return projects

    def list_files(self, organization_id, project_id):
        response = self._make_request(
            "GET", f"/organizations/{organization_id}/projects/{project_id}/docs"
        )
        return [
            {
                "uuid": file["uuid"],
                "file_name": file["file_name"],
                "content": file["content"],
                "created_at": file["created_at"],
            }
            for file in response
        ]

    def upload_file(self, organization_id, project_id, file_name, content):
        data = {"file_name": file_name, "content": content}
        return self._make_request(
            "POST", f"/organizations/{organization_id}/projects/{project_id}/docs", data
        )

    def delete_file(self, organization_id, project_id, file_uuid):
        return self._make_request(
            "DELETE",
            f"/organizations/{organization_id}/projects/{project_id}/docs/{file_uuid}",
        )

    def archive_project(self, organization_id, project_id):
        data = {"is_archived": True}
        return self._make_request(
            "PUT", f"/organizations/{organization_id}/projects/{project_id}", data
        )

    def create_project(self, organization_id, name, description=""):
        data = {"name": name, "description": description, "is_private": True}
        return self._make_request(
            "POST", f"/organizations/{organization_id}/projects", data
        )

    def get_chat_conversations(self, organization_id):
        return self._make_request(
            "GET", f"/organizations/{organization_id}/chat_conversations"
        )

    def get_published_artifacts(self, organization_id):
        return self._make_request(
            "GET", f"/organizations/{organization_id}/published_artifacts"
        )

    def get_chat_conversation(self, organization_id, conversation_id):
        return self._make_request(
            "GET",
            f"/organizations/{organization_id}/chat_conversations/{conversation_id}?rendering_mode=raw",
        )

    def get_artifact_content(self, organization_id, artifact_uuid):
        artifacts = self._make_request(
            "GET", f"/organizations/{organization_id}/published_artifacts"
        )
        for artifact in artifacts:
            if artifact["published_artifact_uuid"] == artifact_uuid:
                return artifact.get("artifact_content", "")
        raise ProviderError(f"Artifact with UUID {artifact_uuid} not found")

    def delete_chat(self, organization_id, conversation_uuids):
        endpoint = f"/organizations/{organization_id}/chat_conversations/delete_many"
        data = {"conversation_uuids": conversation_uuids}
        return self._make_request("POST", endpoint, data)

    def _make_request(self, method, endpoint, data=None):
        raise NotImplementedError("This method should be implemented by subclasses")

    def create_chat(self, organization_id, chat_name="", project_uuid=None):
        """
        Create a new chat conversation in the specified organization.

        Args:
            organization_id (str): The UUID of the organization.
            chat_name (str, optional): The name of the chat. Defaults to an empty string.
            project_uuid (str, optional): The UUID of the project to associate the chat with. Defaults to None.

        Returns:
            dict: The created chat conversation data.

        Raises:
            ProviderError: If the chat creation fails.
        """
        data = {
            "uuid": self._generate_uuid(),
            "name": chat_name,
            "project_uuid": project_uuid,
        }
        return self._make_request(
            "POST", f"/organizations/{organization_id}/chat_conversations", data
        )

    def _generate_uuid(self):
        """Generate a UUID for the chat conversation."""
        import uuid

        return str(uuid.uuid4())

    def _make_request_stream(self, method, endpoint, data=None):
        # This method should be implemented by subclasses to return a response object
        # that can be used with sseclient
        raise NotImplementedError("This method should be implemented by subclasses")

    def send_message(self, organization_id, chat_id, prompt, timezone="UTC"):
        endpoint = (
            f"/organizations/{organization_id}/chat_conversations/{chat_id}/completion"
        )
        data = {
            "prompt": prompt,
            "timezone": timezone,
            "attachments": [],
            "files": [],
        }
        response = self._make_request_stream("POST", endpoint, data)
        client = sseclient.SSEClient(response)
        for event in client.events():
            if event.data:
                try:
                    yield json.loads(event.data)
                except json.JSONDecodeError:
                    yield {"error": "Failed to parse JSON"}
            if event.event == "error":
                yield {"error": event.data}
            if event.event == "done":
                break
```

### src/claudesync/providers/__init__.py

```python

```

### .github/FUNDING.yml

```yml
# These are supported funding model platforms

github: jahwag # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
lfx_crowdfunding: # Replace with a single LFX Crowdfunding project-name e.g., cloud-foundry
polar: # Replace with a single Polar username
buy_me_a_coffee: # Replace with a single Buy Me a Coffee username
thanks_dev: # Replace with a single thanks.dev username
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']
```

### .github/ISSUE_TEMPLATE/feature_request.yml

```yml
[Error reading file: 'charmap' codec can't decode byte 0x8f in position 2748: character maps to <undefined>]
```

### .github/ISSUE_TEMPLATE/bug_report.yml

```yml
name: ClaudeSync Bug Report
description: Report a bug in ClaudeSync.
labels: ["bug"]
projects: ["claudesync/bugs"]
assignees:
  - claudesync-team
body:
  - type: markdown
    attributes:
      value: |
        ### üêû ClaudeSync Bug Report

        Thank you for taking the time to report a bug. Please fill out the following information to help us resolve the issue.

  - type: input
    id: os
    attributes:
      label: Operating System
      description: Which operating system this occurred on
      placeholder: e.g., Windows 10
    validations:
      required: true

  - type: input
    id: python_version
    attributes:
      label: Python Version
      description: E.g. as given by `python --version` and paste the output below.
      placeholder: e.g., 3.13
    validations:
      required: true

  - type: input
    id: claudesync_version
    attributes:
      label: ClaudeSync Version
      description: E.g. as given by `pip show claudesync | grep Version`
      placeholder: e.g., 0.6.0
    validations:
      required: true

  - type: dropdown
    id: installation_type
    attributes:
      label: Installation Type
      description: Is this a new installation or an upgrade from an older version of ClaudeSync?
      options:
        - New
        - Upgraded
      default: 0
    validations:
      required: true

  - type: textarea
    id: configuration
    attributes:
      label: Configuration
      description: Output of `claudesync config ls`. *(Please remove any sensitive information)*
      placeholder: |
        ```bash
        claudesync config ls
        # Paste configuration here
        ```
    validations:
      required: true

  - type: textarea
    id: steps_to_reproduce
    attributes:
      label: Steps to Reproduce
      description: Provide the steps to reproduce the bug.
      placeholder: |
        1. Step one
        2. Step two
        3. Step three
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: Description
      description: What went wrong?
      placeholder: Describe the issue you encountered.
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: Logs
      description: Optional. Paste relevant logs here.
      placeholder: |
        ```bash
        claudesync config set log_level DEBUG
        # Paste logs here
        ```
      render: shell
    validations:
      required: false

  - type: markdown
    attributes:
      value: |
        ---
        ### üôè Thank You for Your Contribution!
```

### .github/workflows/python-publish.yml

```yml
# This workflow will upload a Python Package using Twine when a release is created
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#publishing-to-package-registries

# This workflow uses actions that are not certified by GitHub.
# They are provided by a third-party and are governed by
# separate terms of service, privacy policy, and support
# documentation.

name: Upload Python Package

on:
  release:
    types: [created]

permissions:
  contents: read

jobs:
  deploy:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build
    - name: Build package
      run: python -m build
    - name: Publish package
      uses: pypa/gh-action-pypi-publish@27b31702a0e7fc50959f5ad993c78deac1bdfc29
      with:
        user: __token__
        password: ${{ secrets.PYPI_API_TOKEN }}
```

### .github/workflows/close-stale-issues-and-prs.yml

```yml
name: 'Automatically Manage Stale Issues and PRs'
permissions:
  issues: write
  pull-requests: write

on:
  schedule:
    - cron: '30 1 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          stale-issue-message: 'This issue has been marked as stale due to 14 days of inactivity. Please remove the stale label or comment to keep it open, otherwise, it will be closed in 3 days.'
          stale-pr-message: 'This pull request has been marked as stale due to 7 days of inactivity. Please remove the stale label or comment to keep it open, otherwise, it will be closed in 3 days.'
          close-issue-message: 'This issue was closed due to 3 additional days of inactivity after being marked as stale.'
          close-pr-message: 'This pull request was closed due to 3 additional days of inactivity after being marked as stale.'
          days-before-issue-stale: 14
          days-before-pr-stale: 7
          days-before-issue-close: 3
          days-before-pr-close: 3
```

### .github/workflows/python-package.yml

```yml
name: Python package

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 1
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        pip install -e .
        python -m pip install --upgrade pip
        python -m pip install flake8 pytest black
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --max-complexity=10 --extend-ignore=E203,E701 --max-line-length=127 --statistics
    - name: Format with Black
      run: |
        black --check --diff .
    - name: Test with pytest
      run: |
        pytest
```

### tests/test_happy_path.py

```python
import threading
import time
import unittest
from click.testing import CliRunner
from unittest.mock import patch
from claudesync.cli.main import cli
from claudesync.configmanager import InMemoryConfigManager
from mock_http_server import run_mock_server


class TestClaudeSyncHappyPath(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.mock_server_thread = threading.Thread(target=run_mock_server)
        cls.mock_server_thread.daemon = True
        cls.mock_server_thread.start()
        time.sleep(1)  # Wait for the mock server to start

    def setUp(self):
        self.runner = CliRunner()
        self.config = InMemoryConfigManager()
        self.config.set(
            "claude_api_url", "http://127.0.0.1:8000/api"
        )  # Set BASE_URL for the mock server

    @patch("claudesync.utils.get_local_files")
    def test_happy_path(self, mock_get_local_files):

        # Mock the API calls
        mock_get_local_files.return_value = {"test.txt": "content_hash"}

        # Login
        result = self.runner.invoke(
            cli,
            ["auth", "login", "--provider", "claude.ai"],
            input="sk-ant-1234\nThu, 26 Sep 2099 17:07:53 UTC\n",
            obj=self.config,
        )
        self.assertEqual(0, result.exit_code)
        self.assertIn("Successfully authenticated with claude.ai", result.output)

        # Create project
        result = self.runner.invoke(
            cli,
            [
                "project",
                "create",
                "--name",
                "New Project",
                "--description",
                "Test description",
                "--local-path",
                "./",
                "--provider",
                "claude.ai",
            ],
            obj=self.config,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn(
            "Project 'New Project' (uuid: new_proj) has been created successfully."
            "\n\nProject setup complete. You can now start syncing files with this project. "
            "URL: https://claude.ai/project/new_proj\n",
            result.output,
        )

        # Push project
        result = self.runner.invoke(cli, ["push"], obj=self.config)
        print("Login output:", result.output)
        print("Login exit code:", result.exit_code)
        if result.exception:
            print("Login exception:", result.exception)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Main project 'New Project' synced successfully", result.output)


if __name__ == "__main__":
    unittest.main()
```

### tests/test_claude_ai.py

```python
import unittest
import threading
import time
from unittest.mock import patch
from datetime import datetime

from claudesync.configmanager import InMemoryConfigManager
from claudesync.providers.claude_ai import ClaudeAIProvider
from claudesync.exceptions import ProviderError
from mock_http_server import run_mock_server


class TestClaudeAIProvider(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_server_thread = threading.Thread(target=run_mock_server)
        cls.mock_server_thread.daemon = True
        cls.mock_server_thread.start()
        time.sleep(1)

    def setUp(self):
        self.config = InMemoryConfigManager()
        self.config.set("claude_api_url", "http://127.0.0.1:8000/api")
        self.provider = ClaudeAIProvider(self.config)

    def test_get_organizations(self):
        organizations = self.provider.get_organizations()
        self.assertEqual(len(organizations), 1)
        self.assertEqual(organizations[0]["id"], "org1")
        self.assertEqual(organizations[0]["name"], "Test Org 1")

    def test_get_projects(self):
        projects = self.provider.get_projects("org1")
        self.assertEqual(len(projects), 1)
        self.assertEqual(projects[0]["id"], "proj1")
        self.assertEqual(projects[0]["name"], "Test Project 1")

    def test_create_project(self):
        new_project = self.provider.create_project(
            "org1", "New Project", "Test description"
        )
        self.assertEqual(new_project["uuid"], "new_proj")
        self.assertEqual(new_project["name"], "New Project")

    def test_login(self):
        expiry_str = "Thu, 26 Sep 2099 17:07:53 UTC"

        with patch("click.prompt", side_effect=["sk-ant-test123", expiry_str]):
            with patch.object(
                self.provider,
                "get_organizations",
                return_value=[{"id": "org1", "name": "Test Org"}],
            ):
                session_key, returned_expiry = self.provider.login()

        self.assertEqual("sk-ant-test123", session_key)
        self.assertIsInstance(returned_expiry, datetime)

    def test_list_files(self):
        with patch.object(
            self.provider,
            "_make_request",
            return_value=[
                {
                    "uuid": "file1",
                    "file_name": "test.txt",
                    "content": "Hello",
                    "created_at": "2023-01-01T00:00:00Z",
                }
            ],
        ):
            files = self.provider.list_files("org1", "proj1")
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0]["uuid"], "file1")
        self.assertEqual(files[0]["file_name"], "test.txt")

    def test_upload_file(self):
        with patch.object(
            self.provider, "_make_request", return_value={"uuid": "file1"}
        ):
            result = self.provider.upload_file("org1", "proj1", "test.txt", "Hello")
        self.assertEqual(result["uuid"], "file1")

    def test_delete_file(self):
        with patch.object(self.provider, "_make_request", return_value=None):
            result = self.provider.delete_file("org1", "proj1", "file1")
        self.assertIsNone(result)

    def test_archive_project(self):
        with patch.object(
            self.provider, "_make_request", return_value={"is_archived": True}
        ):
            result = self.provider.archive_project("org1", "proj1")
        self.assertTrue(result["is_archived"])

    def test_get_published_artifacts(self):
        with patch.object(
            self.provider,
            "_make_request",
            return_value=[{"id": "artifact1", "name": "Test Artifact"}],
        ):
            artifacts = self.provider.get_published_artifacts("org1")
        self.assertEqual(len(artifacts), 1)
        self.assertEqual(artifacts[0]["id"], "artifact1")

    def test_get_artifact_content(self):
        with patch.object(
            self.provider,
            "_make_request",
            return_value=[
                {
                    "published_artifact_uuid": "artifact1",
                    "artifact_content": "Test content",
                }
            ],
        ):
            content = self.provider.get_artifact_content("org1", "artifact1")
        self.assertEqual(content, "Test content")

    def test_delete_chat(self):
        with patch.object(
            self.provider, "_make_request", return_value={"deleted": ["chat1"]}
        ):
            result = self.provider.delete_chat("org1", ["chat1"])
        self.assertEqual(result["deleted"], ["chat1"])

    def test_create_chat(self):
        with patch.object(
            self.provider,
            "_make_request",
            return_value={"uuid": "chat1", "name": "New Chat"},
        ):
            chat = self.provider.create_chat("org1", "New Chat", "proj1")
        self.assertEqual(chat["uuid"], "chat1")
        self.assertEqual(chat["name"], "New Chat")

    def test_get_chat_conversations(self):
        chats = self.provider.get_chat_conversations("org1")
        self.assertEqual(len(chats), 2)
        self.assertEqual(chats[0]["uuid"], "chat1")
        self.assertEqual(chats[0]["name"], "Test Chat 1")

    def test_get_chat_conversation(self):
        chat = self.provider.get_chat_conversation("org1", "chat1")
        self.assertEqual(chat["uuid"], "chat1")
        self.assertEqual(len(chat["messages"]), 2)

    def test_send_message(self):
        messages = list(self.provider.send_message("org1", "chat1", "Hello"))
        self.assertEqual(len(messages), 3)
        self.assertEqual(messages[0]["completion"], "Hello")
        self.assertEqual(messages[1]["completion"], " there. ")

    def test_handle_http_error_403(self):
        # This test still needs to use a mock as we can't easily trigger a 403 from our mock server
        mock_error = unittest.mock.MagicMock(code=403, headers={})
        mock_error.read.return_value = b'{"error": "Forbidden"}'
        with self.assertRaises(ProviderError) as context:
            self.provider.handle_http_error(mock_error)
        self.assertIn("403 Forbidden error", str(context.exception))


if __name__ == "__main__":
    unittest.main()
```

### tests/logging_test_case.py

```python
import unittest
import sys
import logging


class LoggingTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up logging to write to stdout
        cls.logger = logging.getLogger(cls.__name__)
        cls.logger.setLevel(logging.DEBUG)

        # Create a StreamHandler for stdout
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)

        # Create a Formatter and set it for the handler
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        # Add the handler to the logger
        cls.logger.addHandler(handler)

    def setUp(self):
        self.logger.info(f"Starting test: {self._testMethodName}")

    def tearDown(self):
        self.logger.info(f"Finished test: {self._testMethodName}")

    def run(self, result=None):
        test_method = getattr(self, self._testMethodName)
        doc = test_method.__doc__
        if doc:
            self.logger.info(f"Test description: {doc.strip()}")
        super().run(result)


class MyTests(LoggingTestCase):
    def test_example(self):
        """This is an example test."""
        self.logger.debug("This is a debug message")
        self.logger.info("This is an info message")
        self.assertEqual(1 + 1, 2)
        self.logger.warning("This is a warning message")
```

### tests/mock_http_server.py

```python
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse


class MockClaudeAIHandler(BaseHTTPRequestHandler):
    files = {}  # Store files in memory

    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.endswith("/chat_conversations"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = json.dumps(
                [
                    {"uuid": "chat1", "name": "Test Chat 1"},
                    {"uuid": "chat2", "name": "Test Chat 2"},
                ]
            )
            self.wfile.write(response.encode())
        elif "/chat_conversations/" in parsed_path.path:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = json.dumps(
                {
                    "uuid": "chat1",
                    "name": "Test Chat 1",
                    "messages": [
                        {"uuid": "msg1", "content": "Hello"},
                        {"uuid": "msg2", "content": "World"},
                    ],
                }
            )
            self.wfile.write(response.encode())
        else:
            print(f"Received GET request: {self.path}")
            # time.sleep(0.01)  # Add a small delay to simulate network latency
            parsed_path = urlparse(self.path)
            if parsed_path.path == "/api/organizations":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = json.dumps(
                    [
                        {
                            "uuid": "org1",
                            "name": "Test Org 1",
                            "capabilities": ["chat", "claude_pro"],
                        },
                        {
                            "uuid": "org2",
                            "name": "Test Org 2",
                            "capabilities": ["chat"],
                        },
                    ]
                )
                self.wfile.write(response.encode())
            elif parsed_path.path.startswith(
                "/api/organizations/"
            ) and parsed_path.path.endswith("/projects"):
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = json.dumps(
                    [
                        {
                            "uuid": "proj1",
                            "name": "Test Project 1",
                            "archived_at": None,
                        },
                        {
                            "uuid": "proj2",
                            "name": "Test Project 2",
                            "archived_at": "2023-01-01",
                        },
                    ]
                )
                self.wfile.write(response.encode())
            elif parsed_path.path.startswith(
                "/api/organizations/"
            ) and parsed_path.path.endswith("/docs"):
                org_id, project_id = (
                    parsed_path.path.split("/")[-3],
                    parsed_path.path.split("/")[-2],
                )
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                files = self.files.get(f"{org_id}/{project_id}", [])
                response = json.dumps(files)
                self.wfile.write(response.encode())
            else:
                self.send_error(404, "Not Found")

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        parsed_path = urlparse(self.path)

        if parsed_path.path.endswith("/chat_conversations"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = json.dumps({"uuid": "new_chat", "name": "New Chat"})
            self.wfile.write(response.encode())
        elif parsed_path.path.endswith("/completion"):
            self.send_response(200)
            self.send_header("Content-type", "text/event-stream")
            self.end_headers()
            self.wfile.write(b'data: {"completion": "Hello"}\n\n')
            self.wfile.write(b'data: {"completion": " there. "}\n\n')
            self.wfile.write(
                b'data: {"completion": "I apologize for the confusion. You\'re right."}\n\n'
            )
            self.wfile.write(b"event: done\n\n")
        else:
            # time.sleep(0.01)  # Add a small delay to simulate network latency
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            parsed_path = urlparse(self.path)

            if parsed_path.path.startswith(
                "/api/organizations/"
            ) and parsed_path.path.endswith("/projects"):
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = json.dumps({"uuid": "new_proj", "name": "New Project"})
                self.wfile.write(response.encode())
            elif parsed_path.path.startswith(
                "/api/organizations/"
            ) and parsed_path.path.endswith("/docs"):
                org_id, project_id = (
                    parsed_path.path.split("/")[-3],
                    parsed_path.path.split("/")[-2],
                )
                data = json.loads(post_data.decode("utf-8"))
                file_data = {
                    "uuid": f"file_{len(self.files.get(f'{org_id}/{project_id}', []))}",
                    "file_name": data["file_name"],
                    "content": data["content"],
                    "created_at": "2023-01-01T00:00:00Z",
                }
                if f"{org_id}/{project_id}" not in self.files:
                    self.files[f"{org_id}/{project_id}"] = []
                self.files[f"{org_id}/{project_id}"].append(file_data)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(file_data).encode())
            else:
                self.send_error(404, "Not Found")

    def do_DELETE(self):
        # time.sleep(0.01)  # Add a small delay to simulate network latency
        parsed_path = urlparse(self.path)
        if (
            parsed_path.path.startswith("/api/organizations/")
            and "/docs/" in parsed_path.path
        ):
            org_id, project_id, file_uuid = (
                parsed_path.path.split("/")[-4],
                parsed_path.path.split("/")[-3],
                parsed_path.path.split("/")[-1],
            )
            if f"{org_id}/{project_id}" in self.files:
                self.files[f"{org_id}/{project_id}"] = [
                    f
                    for f in self.files[f"{org_id}/{project_id}"]
                    if f["uuid"] != file_uuid
                ]
            self.send_response(204)
            self.end_headers()
        else:
            self.send_error(404, "Not Found")


def run_mock_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, MockClaudeAIHandler)
    print(f"Mock server running on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run_mock_server()
```

### tests/test_chat_happy_path.py

```python
import unittest
import threading
import time
from click.testing import CliRunner
from claudesync.cli.main import cli
from claudesync.configmanager import InMemoryConfigManager
from mock_http_server import run_mock_server


class TestChatHappyPath(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the mock server in a separate thread
        cls.mock_server_thread = threading.Thread(target=run_mock_server)
        cls.mock_server_thread.daemon = True
        cls.mock_server_thread.start()
        time.sleep(1)  # Give the server a moment to start

    def setUp(self):
        self.runner = CliRunner()
        self.config = InMemoryConfigManager()
        self.config.set("claude_api_url", "http://localhost:8000/api")

    def test_chat_happy_path(self):
        # Step 1: Login
        result = self.runner.invoke(
            cli,
            ["auth", "login", "--provider", "claude.ai"],
            input="sk-ant-1234\nThu, 26 Sep 2099 17:07:53 UTC\n",
            obj=self.config,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Successfully authenticated with claude.ai", result.output)

        # Step 2: Set organization
        result = self.runner.invoke(
            cli, ["organization", "set"], input="1\n", obj=self.config
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Selected organization: Test Org 1", result.output)

        # Step 3: Create project
        result = self.runner.invoke(
            cli,
            [
                "project",
                "create",
                "--name",
                "Test Project",
                "--description",
                "Test Description",
                "--local-path",
                ".",
            ],
            obj=self.config,
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn(
            "Project 'New Project' (uuid: new_proj) has been created successfully.",
            result.output,
        )

        # Step 4: Send message
        result = self.runner.invoke(
            cli, ["chat", "message", "Hello, Claude!"], input="1\n", obj=self.config
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Hello there.", result.output)
        self.assertIn("I apologize for the confusion. You're right.", result.output)


if __name__ == "__main__":
    unittest.main()
```

> This concludes the repository's file contents. Please review thoroughly for a comprehensive understanding of the codebase.