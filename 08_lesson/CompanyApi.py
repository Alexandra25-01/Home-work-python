import requests


class CompanyApi:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, users=None):
        if users is None:
            users = {}
        data = {
            "title": title,
            "users": users
        }
        resp = requests.post(
            f"{self.base_url}/projects",
            json=data,
            headers=self.headers
        )
        return resp

    def update_project(self, project_id, title=None, deleted=None, users=None):
        data = {}
        if title is not None:
            data["title"] = title
        if deleted is not None:
            data["deleted"] = deleted
        if users is not None:
            data["users"] = users

        resp = requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        return resp

    def get_project(self, project_id):
        resp = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return resp
