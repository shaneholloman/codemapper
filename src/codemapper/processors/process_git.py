"""Git operations for CodeMapper."""

import os
import subprocess


def clone_github_repo(repo_url: str) -> str:
    """Clone a GitHub repository into a '_github' directory."""
    github_dir = os.path.join(".", "_github")
    os.makedirs(github_dir, exist_ok=True)

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(github_dir, repo_name)

    if os.path.exists(repo_path):
        print(f"Repository '{repo_name}' already exists. Updating...")
        subprocess.run(["git", "-C", repo_path, "pull", "--depth", "1"], check=True)
        return repo_path

    print(f"Cloning repository '{repo_name}'...")
    subprocess.run(["git", "clone", "--depth", "1", repo_url, repo_path], check=True)
    return repo_path


def get_git_info(directory_path: str) -> dict[str, str]:
    """Extract git metadata from a directory if it's a git repository."""
    git_info = {}

    try:
        # Check if it's a git repository
        subprocess.run(
            ["git", "-C", directory_path, "rev-parse", "--git-dir"],
            capture_output=True,
            text=True,
            check=True,
        )

        # Get current branch
        branch_result = subprocess.run(
            ["git", "-C", directory_path, "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        git_info["branch"] = branch_result.stdout.strip()

        # Get commit hash
        hash_result = subprocess.run(
            ["git", "-C", directory_path, "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        git_info["commit"] = hash_result.stdout.strip()[:8]  # Short hash

        # Get commit date
        date_result = subprocess.run(
            ["git", "-C", directory_path, "log", "-1", "--format=%ci"],
            capture_output=True,
            text=True,
            check=True,
        )
        git_info["date"] = date_result.stdout.strip()

        # Get remote URL if available
        remote_result = subprocess.run(
            ["git", "-C", directory_path, "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
        )
        if remote_result.returncode == 0:
            git_info["remote"] = remote_result.stdout.strip()

    except (subprocess.CalledProcessError, FileNotFoundError):
        # Not a git repo or git not available
        pass

    return git_info
