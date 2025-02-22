from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Шаг 1: Откройте страницу http://the-internet.herokuapp.com/login.
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

# Шаг 2: В поле username введите значение "tomsmith".
try:
    # Используем CSS-селектор для поиска поля ввода username
    username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("tomsmith")
    print("Ввели текст 'tomsmith' в поле username.")
except TimeoutException:
    print("Поле username не найдено или не стало кликабельным в течение 10 секунд.")

# Шаг 3: В поле password введите значение "SuperSecretPassword!".
try:
    # Используем CSS-селектор для поиска поля ввода password
    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password")))
    password_field.send_keys("SuperSecretPassword!")
    print("Ввели текст 'SuperSecretPassword!' в поле password.")
except TimeoutException:
    print("Поле password не найдено или не стало кликабельным в течение 10 секунд.")

# Шаг 4: Нажмите кнопку Login.
try:
    # Используем CSS-селектор для поиска кнопки Login
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()
    print("Нажали кнопку Login.")
except TimeoutException:
    print("Кнопка Login не найдена или не стала кликабельной в течение 10 секунд.")

# Шаг 5: Нажмите кнопку Logout.
try:
    # Используем CSS-селектор для поиска кнопки Logout
    logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.icon-2x.icon-signout")))
    logout_button.click()
    print("Нажали кнопку Logout.")
except TimeoutException:
    print("Кнопка Logout не найдена или не стала кликабельной в течение 10 секунд.")




sleep(200)