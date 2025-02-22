from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Шаг 1: открыть страницу http://uitestingplayground.com/classatt
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("http://uitestingplayground.com/classattr")

# Шаг 2: кликнуть на синюю кнопку
try:
    #  CSS-селектор для поиска кнопки по классу
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.class3.btn-primary.btn-test")))
    button.click()
    print("Кнопка успешно нажата!")
except TimeoutException:
    print("Кнопка не найдена или не стала кликабельной в течение 10 секунд.")

# Шаг 3:закрыть браузер
driver.quit()