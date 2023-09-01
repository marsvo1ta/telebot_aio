import requests
import os


def regress_dispatch():
    username = "marsvo1ta"
    repo_name = "regress"
    workflow_name = "regress_workflow_prod.yml"
    access_token = os.environ.get('DISPATCH')

    url = f"https://api.github.com/repos/{username}/{repo_name}/actions/workflows/{workflow_name}/dispatches"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.post(url, json={"ref": "prod"}, headers=headers)

    if response.status_code == 204:
        print("Workflow dispatch successful.")
    else:
        print("Workflow dispatch failed:", response.text)
