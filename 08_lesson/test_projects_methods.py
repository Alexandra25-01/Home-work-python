from CompanyApi import CompanyApi
from config import TOKEN, BASE_URL

api = CompanyApi(BASE_URL, TOKEN)


def test_create_project_positive():
    create_resp = api.create_project("Тестовый проект")
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]
    get_resp = api.get_project(project_id)
    data = get_resp.json()
    assert data["title"] == "Тестовый проект"


def test_create_project_negative():
    create_resp = api.create_project("")
    assert create_resp.status_code == 400


def test_update_project_positive():
    create_resp = api.create_project("Проект до изменения")
    project_id = create_resp.json()["id"]
    update_resp = api.update_project(
        project_id, title="Проект после изменения"
        )
    assert update_resp.status_code == 200
    get_resp = api.get_project(project_id)
    data = get_resp.json()
    assert data["title"] == "Проект после изменения"


def test_update_project_negative():
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = api.update_project(invalid_id, title="Неверный проект")
    assert response.status_code == 404


def test_get_project_positive():
    create_resp = api.create_project("Проект для получения")
    project_id = create_resp.json()["id"]
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["title"] == "Проект для получения"


def test_get_project_negative():
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(invalid_id)
    assert response.status_code == 404
