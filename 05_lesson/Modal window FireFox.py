from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Шаг 1: открыть страницу
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Шаг 2: В модальном окне нажмите на кнопку Close.
try:
    #  XPath для поиска кнопки Close в модальном окне
    close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Close']")))
    close_button.click()
    print("Кнопка Close успешно нажата!")
except TimeoutException:
    print("Кнопка Close не найдена или не стала кликабельной в течение 10 секунд.")

# Шаг 3: закрыть браузер
driver.quit()