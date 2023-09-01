import requests
import os


def health_check_dispatch():
    username = "marsvo1ta"
    repo_name = "checker"
    workflow_name = "python-app.yml"
    access_token = os.environ.get('DISPATCH')

    url = f"https://api.github.com/repos/{username}/{repo_name}/actions/workflows/{workflow_name}/dispatches"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.post(url, json={"ref": "main"}, headers=headers)

    if response.status_code == 204:
        print("Workflow dispatch successful.")
    else:
        print("Workflow dispatch failed:", response.text)
