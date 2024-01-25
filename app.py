import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env
load_dotenv()

# GitHub API URL
api_url = "https://api.github.com/repos/{owner}/{repo}"

# Retrieve GitHub token from environment variable
token = os.getenv("GITHUB_TOKEN")

# List of repositories to delete
# Prompt user for repository names
repos_input = input("Enter repository names (comma-separated repo1,repo2,repo3): ")
repos_to_delete = [repo.strip() for repo in repos_input.split(",")]

# Function to delete a repository
def delete_repo(repo):
    url = api_url.format(owner="nadotdev", repo=repo)
    headers = {"Authorization": f"token {token}"}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Repository {repo} deleted successfully.")
    else:
        print(f"Failed to delete repository {repo}. Status code: {response.status_code}")

# Loop through the list and delete repositories
for repo_name in repos_to_delete:
    delete_repo(repo_name)
