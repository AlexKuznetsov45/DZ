import pytest
from ..pages.FormPage import FormPage
from allure import title, description, feature, severity, step

@title("Тестирование заполнения формы")
@description("Тестирует заполнение всех полей формы и проверку валидации.")
@feature("Форма данных")
@severity(severity_level="normal")
@pytest.mark.parametrize(
    "form_values",
    [
        {
            "first_name": "Иван",
            "last_name": "Петров",
            "address": "Ленина, 55-3",
            "email": "test@skypro.com",
            "phone_number": "+7985899998787",
            "zip_code": "",  # Оставляем поле пустым
            "city": "Москва",
            "country": "Россия",
            "job_position": "QA",
            "company": "SkyPro",
        }
    ],
)
def test_fill_form(browser, form_values):
    form_page = FormPage(browser)

    with step("Открытие страницы формы"):
        browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    with step("Заполнение формы"):
        form_page.enter_first_name(form_values["first_name"])
        form_page.enter_last_name(form_values["last_name"])
        form_page.enter_address(form_values["address"])
        form_page.enter_email(form_values["email"])
        form_page.enter_phone_number(form_values["phone_number"])
        form_page.enter_zip_code(form_values["zip_code"])
        form_page.enter_city(form_values["city"])
        form_page.enter_country(form_values["country"])
        form_page.enter_job_position(form_values["job_position"])
        form_page.enter_company(form_values["company"])

    with step("Нажатие кнопки Submit"):
        form_page.click_submit_button()

    with step("Проверка подсветки поля Zip Code"):
        assert (
            form_page.is_zip_code_highlighted_red()
        ), "Zip Code should be highlighted red."

    with step("Проверка успешной валидации остальных полей"):
        form_page.validate_successful_fields()