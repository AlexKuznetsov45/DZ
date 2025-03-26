class TestChangeProjectTitleNegative:
    def test_change_project_title_empty_title(
        self, projects_api, pytestconfig
    ):
        # Получаем идентификатор проекта из предыдущего теста
        project_id = (
            pytestconfig.cache.get("project_id", None)
        )
        assert project_id is not None, "Идентификатор проекта не был сохранен!"

        # Пробуем обновить проект с пустым названием
        updated_payload = {"title": ""}
        response = projects_api.update_project(
            project_id,
            updated_payload
        )

        # Ожидаем, что сервер вернет ошибку 400 (Bad Request)
        assert response.status_code == 400
        assert "error" in response.json()
