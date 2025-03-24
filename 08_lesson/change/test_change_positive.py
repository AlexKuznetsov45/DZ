class TestChangeProjectTitle:
    def test_change_project_title_to_Lesson_8(
        self, projects_api, pytestconfig
    ):
        # Получаем идентификатор проекта из предыдущего теста
        project_id = pytestconfig.cache.get("project_id", None)
        assert project_id is not None, "Идентификатор проекта не был сохранен!"

        updated_payload = {"title": "Урок 8"}
        response = projects_api.update_project(project_id, updated_payload)

        # Проверяем успешное обновление
        assert response.status_code == 200

        # Выводим тело ответа для отладки
        print(f"Response text: {response.text}")
