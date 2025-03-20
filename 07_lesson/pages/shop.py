from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Shop:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    USERNAME_INPUT_LOCATOR = (By.ID, "user-name")
    PASSWORD_INPUT_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")

    # Методы для взаимодействия с элементами
    def go_to_shop(self):
        """Переход на страницу магазина."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """Авторизация на сайте."""
        # Ожидание загрузки элементов
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.USERNAME_INPUT_LOCATOR))
        password_input = self.driver.find_element(*self.PASSWORD_INPUT_LOCATOR)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)

        # Ввод данных и клик по кнопке
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()