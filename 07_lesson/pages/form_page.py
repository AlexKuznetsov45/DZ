from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    FIRST_NAME_LOCATOR = (By.CSS_SELECTOR, "[name='first-name']")
    LAST_NAME_LOCATOR = (By.CSS_SELECTOR, "[name='last-name']")
    ADDRESS_LOCATOR = (By.CSS_SELECTOR, "[name='address']")
    EMAIL_LOCATOR = (By.CSS_SELECTOR, "[name='e-mail']")
    PHONE_NUMBER_LOCATOR = (By.CSS_SELECTOR, "[name='phone']")
    ZIP_CODE_INPUT_LOCATOR = (
        By.CSS_SELECTOR,
        "[name='zip-code']",
    )  # Локатор для input перед нажатием кнопки
    ZIP_CODE_ALERT_LOCATOR = (
        By.CSS_SELECTOR,
        "#zip-code.alert-danger",
    )  # Локатор для div после нажатия кнопки
    CITY_LOCATOR = (By.CSS_SELECTOR, "[name='city']")
    COUNTRY_LOCATOR = (By.CSS_SELECTOR, "[name='country']")
    JOB_POSITION_LOCATOR = (By.CSS_SELECTOR, "[name='job-position']")
    COMPANY_LOCATOR = (By.CSS_SELECTOR, "[name='company']")
    SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'button[type="submit"]')

    # Универсальная функция для поиска и заполнения элементов
    def find_and_send_keys(self, locator, text):
        element = WebDriverWait(
            self.driver, 20
        ).until(  # Увеличили время ожидания до 20 секунд
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    # Методы для ввода значений в поля
    def enter_first_name(self, first_name):
        self.find_and_send_keys(self.FIRST_NAME_LOCATOR, first_name)

    def enter_last_name(self, last_name):
        self.find_and_send_keys(self.LAST_NAME_LOCATOR, last_name)

    def enter_address(self, address):
        self.find_and_send_keys(self.ADDRESS_LOCATOR, address)

    def enter_email(self, email):
        self.find_and_send_keys(self.EMAIL_LOCATOR, email)

    def enter_phone_number(self, phone_number):
        self.find_and_send_keys(self.PHONE_NUMBER_LOCATOR, phone_number)

    def enter_zip_code(self, zip_code):
        self.find_and_send_keys(self.ZIP_CODE_INPUT_LOCATOR, zip_code)

    def enter_city(self, city):
        self.find_and_send_keys(self.CITY_LOCATOR, city)

    def enter_country(self, country):
        self.find_and_send_keys(self.COUNTRY_LOCATOR, country)

    def enter_job_position(self, job_position):
        self.find_and_send_keys(self.JOB_POSITION_LOCATOR, job_position)

    def enter_company(self, company):
        self.find_and_send_keys(self.COMPANY_LOCATOR, company)

    # Метод для нажатия кнопки Submit
    def click_submit_button(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON_LOCATOR)
        )
        submit_button.click()

    # Проверка подсветки поля zip_code
    def is_zip_code_highlighted_red(self):
        # Проверяем наличие элемента с классом 'alert-danger' для поля zip_code
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ZIP_CODE_ALERT_LOCATOR)
        )

    # Проверка успешной валидации полей
    def validate_successful_fields(self):
        successful_fields = [
            (By.CSS_SELECTOR, "#first-name.alert-success"),
            (By.CSS_SELECTOR, "#last-name.alert-success"),
            (By.CSS_SELECTOR, "#address.alert-success"),
            (By.CSS_SELECTOR, "#e-mail.alert-success"),
            (By.CSS_SELECTOR, "#phone.alert-success"),
            (By.CSS_SELECTOR, "#city.alert-success"),
            (By.CSS_SELECTOR, "#country.alert-success"),
            (By.CSS_SELECTOR, "#job-position.alert-success"),
            (By.CSS_SELECTOR, "#company.alert-success"),
        ]

        for field_selector in successful_fields:
            field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(field_selector)
            )
            print(
                f"Поле '{field_selector[1].split('.')[0]} "
                f"успешно валидировано: "
                f"{field.text} (цвет фона: зеленый)"
            )
