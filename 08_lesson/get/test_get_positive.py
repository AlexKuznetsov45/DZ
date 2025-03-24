class TestGetProjectByID:
    def test_get_project_by_id(self, projects_api, pytestconfig):
        # Получаем идентификатор проекта из предыдущего теста
        project_id = pytestconfig.cache.get("project_id", None)
        assert project_id is not None, "Идентификатор проекта не был сохранен!"

        # Делаем запрос на получение проекта по его идентификатору
        response = projects_api.get_project_by_id(project_id)

        # Проверяем успешный статус ответа
        assert response.status_code == 200

        # Проверяем, что ответ содержит необходимые ключи
        project_data = response.json()
        assert "id" in project_data, "Ответ не содержит идентификатор проекта!"
        assert "title" in project_data, "Ответ не содержит название проекта!"
        assert "timestamp" in project_data, "Ответ не содержит метку времени!"
        assert "users" in project_data, "Нет информации о сотрудниках!"
