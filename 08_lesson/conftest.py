import requests
import pytest


# Базовая настройка URL и токена
@pytest.fixture(scope="session")
def base_url():
    return "https://yougile.com/api-v2"


@pytest.fixture(scope="session")
def authorization_token():
    return "Ваш ключ"


# Класс для взаимодействия с API
class ProjectsAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_project(self, title, users):
        url = f"{self.base_url}/projects"
        payload = {"title": title, "users": users}
        response = requests.post(url, json=payload, headers=self.headers)
        return response

    def get_project_by_id(self, project_id):
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_project(self, project_id, data):
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.put(url, json=data, headers=self.headers)
        return response

    def delete_project(self, project_id):
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.delete(url, headers=self.headers)
        return response


# Основной фикстуры
@pytest.fixture(scope="session")
def projects_api(base_url, authorization_token):
    return ProjectsAPI(base_url, authorization_token)
