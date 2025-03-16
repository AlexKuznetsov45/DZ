import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def browser():
    """Фикстура для запуска браузера."""
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def enter_delay(browser, delay_value):
    """Функция для ввода значения задержки."""
    input_delay = browser.find_element(By.CSS_SELECTOR, "#delay")
    input_delay.clear()
    input_delay.send_keys(delay_value)

def press_buttons(browser, buttons):
    """Функция для последовательного нажатия на кнопки калькулятора."""
    for button in buttons:
        btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[contains(@class, 'btn')][normalize-space(text())='{button}']"))
        )
        btn.click()

def wait_for_spinner_disappear(browser):
    """Функция для ожидания исчезновения спинора."""
    WebDriverWait(browser, 50).until_not(  # Ожидание до 50 секунд для исчезновения спинора
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#spinner"))
    )

def get_result(browser):
    """Функция для получения результата вычислений."""
    result = WebDriverWait(browser, 60).until(  # Увеличили время ожидания до 60 секунд
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".screen"))
    )
    return result.text

def test_calculator(browser):
    """Тестовая функция для проверки калькулятора."""
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Вводим значение задержки
    enter_delay(browser, "45")
    
    # Нажимаем на кнопки
    press_buttons(browser, ["7", "+", "8"])
    
    # Нажимаем на кнопку =
    equals_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'btn')][normalize-space(text())='=']"))
    )
    equals_btn.click()
    
    # Ожидаем исчезновения спинора
    wait_for_spinner_disappear(browser)
    
    # Проверяем результат
    result = get_result(browser)
    assert result == "15", f"Результат не совпадает. Ожидается: 15, Фактический: {result}"