import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def fill_form(browser):
    
    # Функция для поиска и заполнения элементов
    def find_and_send_keys(locator, text):
        element = browser.find_element(By.CSS_SELECTOR, locator)
        element.clear()
        element.send_keys(text)

    # Заполнение формы
    find_and_send_keys("[name='first-name']", "Иван")
    find_and_send_keys("[name='last-name']", "Петров")
    find_and_send_keys("[name='address']", "Ленина, 55-3")
    find_and_send_keys("[name='e-mail']", "test@skypro.com")
    find_and_send_keys("[name='phone']", "+7985899998787")
    find_and_send_keys("[name='zip-code']", "")
    find_and_send_keys("[name='city']", "Москва")
    find_and_send_keys("[name='country']", "Россия")
    find_and_send_keys("[name='job-position']", "QA")
    find_and_send_keys("[name='company']", "SkyPro")

    # Нажатие на кнопку
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

def check_validation_classes(browser):
    """Функция для проверки классов валидации."""
    print("Проверка валидации...")

    # Проверка, что поле 'zip-code' имеет класс ошибки (.alert-danger)
    zip_code = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger"))
    )
    print(f"Поле 'zip-code' помечено как ошибочное: {zip_code.text} (цвет фона: красный)")

    # Проверка, что остальные поля имеют класс успешной валидации (.alert-success)
    successful_fields = ["#first-name",
                         "#last-name",
                         "#address",
                         "#e-mail",
                         "#phone",
                         "#city",
                         "#country",
                         "#job-position",
                         "#company"]

    for field_selector in successful_fields:
        field = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, field_selector + '.alert-success'))
        )
        print(f"Поле '{field_selector}' успешно валидировано: {field.text} (цвет фона: зеленый)")

def test_fill_form(browser):
    """Тестовая функция для заполнения формы и проверки валидации."""
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    fill_form(browser)
    check_validation_classes(browser)