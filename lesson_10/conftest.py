import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    """Фикстура для запуска браузера в режиме инкогнито."""
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Включаем режим инкогнито
    driver = webdriver.Chrome(options=chrome_options)  # Используем настроенные опции
    yield driver
    driver.quit()