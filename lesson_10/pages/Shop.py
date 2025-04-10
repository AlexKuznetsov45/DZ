from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Shop:
    def __init__(self, driver):
        """
        Конструктор класса страницы магазина.

        :param driver: Экземпляр веб-драйвера Selenium
        :type driver: WebDriver
        """
        self.driver = driver

    # Локаторы элементов
    USERNAME_INPUT_LOCATOR = (By.ID, "user-name")  # Локатор поля ввода имени пользователя
    PASSWORD_INPUT_LOCATOR = (By.ID, "password")  # Локатор поля ввода пароля
    LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")  # Локатор кнопки входа

    # Методы для взаимодействия с элементами
    def go_to_shop(self):
        """
        Переход на страницу магазина.

        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")  # Перейти на сайт SauceDemo

    def login(self, username: str, password: str):
        """
        Авторизация на сайте.

        :param username: Имя пользователя для авторизации
        :type username: str
        :param password: Пароль для авторизации
        :type password: str
        :return: None
        """
        # Ожидание загрузки элементов
        username_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.USERNAME_INPUT_LOCATOR)
        )
        password_input = self.driver.find_element(*self.PASSWORD_INPUT_LOCATOR)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR)

        # Ввод данных и клик по кнопке
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()