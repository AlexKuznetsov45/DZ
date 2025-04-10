from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver):
        """
        Конструктор класса страницы продукта.

        :param driver: Экземпляр веб-драйвера Selenium
        :type driver: WebDriver
        """
        self.driver = driver

    # Локаторы элементов
    ADD_TO_CART_BACKPACK_LOCATOR = (By.ID, "add-to-cart-sauce-labs-backpack")  # Локатор кнопки добавления рюкзака в корзину
    ADD_TO_CART_T_SHIRT_LOCATOR = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")  # Локатор кнопки добавления футболки в корзину
    ADD_TO_CART_ONESIE_LOCATOR = (By.ID, "add-to-cart-sauce-labs-onesie")  # Локатор кнопки добавления комбинезона в корзину

    # Методы для взаимодействия с элементами
    def add_backpack_to_cart(self):
        """
        Добавляет рюкзак в корзину.

        :return: None
        """
        backpack_add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BACKPACK_LOCATOR)
        )
        backpack_add_to_cart_button.click()

    def add_t_shirt_to_cart(self):
        """
        Добавляет футболку в корзину.

        :return: None
        """
        t_shirt_add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_T_SHIRT_LOCATOR)
        )
        t_shirt_add_to_cart_button.click()

    def add_onesie_to_cart(self):
        """
        Добавляет комбинезон в корзину.

        :return: None
        """
        onesie_add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_ONESIE_LOCATOR)
        )
        onesie_add_to_cart_button.click()