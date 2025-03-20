import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage

@pytest.fixture
def browser():
    """Фикстура для запуска браузера."""
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_calculator_flow(browser):
    """Тестовая функция для проверки калькулятора."""
    calculator_page = CalculatorPage(browser)
    calculator_page.open()
    calculator_page.set_delay(45)
    
    # Последовательное нажатие на кнопки калькулятора
    calculator_page.press_button(calculator_page.BUTTON_7_LOCATOR)
    calculator_page.press_button(calculator_page.BUTTON_PLUS_LOCATOR)
    calculator_page.press_button(calculator_page.BUTTON_8_LOCATOR)
    calculator_page.press_button(calculator_page.BUTTON_EQUALS_LOCATOR)

    # Ожидание исчезновения спинора
    calculator_page.wait_for_spinner_disappear()

    # Получение и проверка результата
    result = calculator_page.get_result()
    assert result == "15", f"Результат не совпадает. Ожидается: 15, Фактический: {result}"