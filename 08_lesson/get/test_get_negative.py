class TestGetProjectByInvalidID:
    def test_get_project_by_invalid_id(self, projects_api):
        # Используем заведомо несуществующий идентификатор проекта
        invalid_project_id = "nonexistent-project-id"

        # Делаем запрос на получение проекта по его идентификатору
        response = projects_api.get_project_by_id(invalid_project_id)

        # Проверяем, что сервер вернул ошибку 404 (Not Found)
        assert response.status_code == 404
        assert "error" in response.json(), "Ответ не содержит ключ 'error'!"
