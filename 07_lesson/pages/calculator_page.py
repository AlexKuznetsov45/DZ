from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    DELAY_FIELD_LOCATOR = (By.CSS_SELECTOR, "#delay")
    SPINNER_LOCATOR = (By.CSS_SELECTOR, "#spinner")
    SCREEN_RESULT_LOCATOR = (By.CSS_SELECTOR, ".screen")
    BUTTON_7_LOCATOR = (By.XPATH, "//*[@id='calculator']/div[2]/span[1]")
    BUTTON_PLUS_LOCATOR = (
        By.CSS_SELECTOR,
        "#calculator > div.keys > span:nth-child(4)",
    )
    BUTTON_8_LOCATOR = (By.XPATH, "//*[@id='calculator']/div[2]/span[2]")
    BUTTON_EQUALS_LOCATOR = (
        By.CSS_SELECTOR,
        "#calculator > div.keys > span.btn.btn-outline-warning",
    )

    # Методы для взаимодействия с элементами
    def enter_delay(self, delay_value):
        """Функция для ввода значения задержки."""
        input_delay = self.driver.find_element(*self.DELAY_FIELD_LOCATOR)
        input_delay.clear()
        input_delay.send_keys(delay_value)

    def press_button(self, button_locator):
        """Функция для нажатия на кнопку калькулятора."""
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def wait_for_spinner_disappear(self):
        """Функция для ожидания исчезновения спинора."""
        WebDriverWait(self.driver, 50).until_not(
            EC.visibility_of_element_located(self.SPINNER_LOCATOR)
        )

    def get_result(self):
        """Функция для получения результата вычислений."""
        result = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.SCREEN_RESULT_LOCATOR)
        )
        return result.text
