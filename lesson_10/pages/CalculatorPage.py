from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса страницы калькулятора.

        :param driver: Веб-драйвер Selenium
        :type driver: WebDriver
        """
        self.driver = driver

    # Локаторы элементов
    DELAY_FIELD_LOCATOR = (By.CSS_SELECTOR, "#delay")
    SPINNER_LOCATOR = (By.CSS_SELECTOR, "#spinner")
    SCREEN_RESULT_LOCATOR = (By.CSS_SELECTOR, ".screen")
    BUTTON_7_LOCATOR = (By.XPATH, "//*[@id='calculator']/div[2]/span[1]")
    BUTTON_PLUS_LOCATOR = (By.XPATH, "//*[@id='calculator']/div[2]/span[4]")
    BUTTON_8_LOCATOR = (By.XPATH, "//*[@id='calculator']/div[2]/span[2]")
    BUTTON_EQUALS_LOCATOR = (By.XPATH, "//*[@id='calculator']/div[2]/span[15]")

    # Методы для взаимодействия с элементами
    def open(self):
        """
        Открывает страницу калькулятора.

        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, delay_value: int):
        """
        Устанавливает задержку перед выполнением операций.

        :param delay_value: Величина задержки в миллисекундах
        :type delay_value: int
        :return: None
        """
        delay_field = self.driver.find_element(*self.DELAY_FIELD_LOCATOR)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    def press_button(self, button_locator: tuple):
        """
        Нажимает на кнопку калькулятора.

        :param button_locator: Локатор кнопки
        :type button_locator: tuple
        :return: None
        """
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def wait_for_spinner_disappear(self):
        """
        Ожидает исчезновения индикатора загрузки.

        :return: None
        """
        WebDriverWait(self.driver, 50).until_not(
            EC.visibility_of_element_located(self.SPINNER_LOCATOR)
        )

    def get_result(self) -> str:
        """
        Получает результат вычислений с экрана калькулятора.

        :return: Строка с результатом вычислений
        :rtype: str
        """
        result = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.SCREEN_RESULT_LOCATOR)
        )
        return result.text