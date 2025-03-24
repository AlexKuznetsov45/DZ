class TestCreateProjectNegative:
    def test_create_project_missing_title(self, projects_api):
        # Определение полезной нагрузки для создания проекта
        payload = {
            "users": {
                "94556598-71f2-4851-b934-60a84270fd56": "admin"  # Ваш ID
            }
        }

        # Отправка запроса на создание проекта без названия
        response = projects_api.create_project(None, payload["users"])

        # Проверка, что сервер вернул ошибку 400 (Bad Request)
        assert response.status_code == 400, (
            f"Ожидалась ошибка 400, но получен статус-код: "
            f"{response.status_code}"
        )
        assert "error" in response.json(), "Ответ не содержит ключ 'error'!"
