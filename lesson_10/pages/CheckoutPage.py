from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        """
        Конструктор класса страницы оформления заказа.

        :param driver: Экземпляр веб-драйвера Selenium
        :type driver: WebDriver
        """
        self.driver = driver

    # Локаторы элементов
    FIRST_NAME_INPUT_LOCATOR = (By.ID, "first-name")  # Локатор поля ввода имени
    LAST_NAME_INPUT_LOCATOR = (By.ID, "last-name")  # Локатор поля ввода фамилии
    POSTAL_CODE_INPUT_LOCATOR = (By.ID, "postal-code")  # Локатор поля ввода почтового индекса
    CONTINUE_BUTTON_LOCATOR = (By.CLASS_NAME, "cart_button")  # Локатор кнопки Продолжить

    # Методы для взаимодействия с элементами
    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполняет форму личной информацией.

        :param first_name: Имя покупателя
        :type first_name: str
        :param last_name: Фамилия покупателя
        :type last_name: str
        :param postal_code: Почтовый индекс
        :type postal_code: str
        :return: None
        """
        # Заполнить поле имени
        first_name_input = self.driver.find_element(*self.FIRST_NAME_INPUT_LOCATOR)
        first_name_input.send_keys(first_name)
        # Заполнить поле фамилии
        last_name_input = self.driver.find_element(*self.LAST_NAME_INPUT_LOCATOR)
        last_name_input.send_keys(last_name)
        # Заполнить поле почтового индекса
        postal_code_input = self.driver.find_element(*self.POSTAL_CODE_INPUT_LOCATOR)
        postal_code_input.send_keys(postal_code)
        # Нажать кнопку Продолжить
        continue_button = self.driver.find_element(*self.CONTINUE_BUTTON_LOCATOR)
        continue_button.click()

    def get_total_cost(self) -> str:
        """
        Получает общую стоимость заказа.

        :return: Общая стоимость заказа
        :rtype: str
        """
        # Получить текст общей стоимости
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