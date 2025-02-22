from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Шаг 1: Откройте страницу http://the-internet.herokuapp.com/inputs.
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")

# Шаг 2: Введите в поле текст "1000".
try:
    # Используем CSS-селектор для поиска поля ввода
    input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='number']")))
    input_field.send_keys("1000")
    print("Ввели текст '1000' в поле ввода.")
except TimeoutException:
    print("Поле ввода не найдено или не стало кликабельным в течение 10 секунд.")

# Шаг 3: Очистите это поле (метод clear).
try:
    input_field.clear()
    print("Поле ввода успешно очищено.")
except:
    print("Не удалось очистить поле ввода.")

# Шаг 4: Введите в это же поле текст "999".
try:
    input_field.send_keys("999")
    print("Ввели текст '999' в поле ввода.")
except TimeoutException:
    print("Поле ввода не найдено или не стало кликабельным в течение 10 секунд.")

# Шаг 5: Закройте браузер
driver.quit()