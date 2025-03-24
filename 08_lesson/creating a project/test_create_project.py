# Позитивный тест на создание проекта
class TestCreateProject:
    def test_create_project_with_token(self, projects_api, pytestconfig):
        # Определение полезной нагрузки для создания проекта
        payload = {
            "title": "Урок 8 YouGile",
            # Ваш идентификатор пользователя
            "users": {
                "94556598-71f2-4851-b934-60a84270fd56": "admin"
            },
        }

        # Отправка запроса на создание проекта
        response = projects_api.create_project(
            payload["title"],
            payload["users"]
        )

        # Проверка успешного выполнения запроса
        assert response.status_code == 201, (
            f"Ошибка создания проекта: "
            f"{response.text}"
        )

        # Проверка наличия поля 'id' в ответе
        new_project = response.json()
        assert "id" in new_project, "Ответ не содержит идентификатор проекта!"

        # Извлечение и вывод идентификатора проекта
        new_project_id = new_project["id"]
        print(f"Created project ID: {new_project_id}")

        # Дополнительные проверки
        assert len(new_project_id) > 0, (
            "Идентификатор проекта пустой или отсутствует!"
        )

        # Сохранение идентификатора проекта для использования в других тестах
        pytestconfig.cache.set("project_id", new_project_id)
