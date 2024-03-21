import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

BASE_URL = "https://api.github.com"
repo_owner = "async-labs"  # Example repo owner
repo_name = "saas"  # Example repo name

access_token = os.getenv("GITHUB_ACCESS_TOKEN")

headers = {
    "Authorization": f"token {access_token}",
    "Accept": "application/vnd.github.v3+json",
}


def fetch_commits():
    """Fetches commits from a GitHub repository and returns them."""
    commits_url = f"{BASE_URL}/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(commits_url, headers=headers, timeout=5)
    if response.ok:
        commits = response.json()
        return [
            {
                "author": commit["commit"]["author"]["name"],
                "message": commit["commit"]["message"],
            }
            for commit in commits[:5]
        ]  # Limit to latest 5 commits
    else:
        print("Failed to fetch commits.")
        return []


