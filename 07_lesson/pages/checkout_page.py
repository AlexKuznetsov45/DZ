from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    FIRST_NAME_INPUT_LOCATOR = (By.ID, "first-name")
    LAST_NAME_INPUT_LOCATOR = (By.ID, "last-name")
    POSTAL_CODE_INPUT_LOCATOR = (By.ID, "postal-code")
    CONTINUE_BUTTON_LOCATOR = (By.CLASS_NAME, "cart_button")

    # Методы для взаимодействия с элементами
    def fill_information(self, first_name, last_name, postal_code):
        """Заполнение формы информацией."""
        first_name_input = self.driver.find_element(
            *self.FIRST_NAME_INPUT_LOCATOR
        )
        first_name_input.send_keys(first_name)
        last_name_input = self.driver.find_element(
            *self.LAST_NAME_INPUT_LOCATOR
        )
        last_name_input.send_keys(last_name)
        postal_code_input = self.driver.find_element(
            *self.POSTAL_CODE_INPUT_LOCATOR
        )
        postal_code_input.send_keys(postal_code)
        continue_button = self.driver.find_element(
            *self.CONTINUE_BUTTON_LOCATOR
        )
        continue_button.click()

    def get_total_cost(self):
        """Получение итоговой стоимости."""
        total_cost = (
            WebDriverWait(self.driver, 10)
            .until(
                EC.visibility_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "div.summary_total_label[data-test='total-label']",
                    )
                )
            )
            .text
        )
        return total_cost
