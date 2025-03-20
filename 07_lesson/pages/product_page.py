from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    ADD_TO_CART_BACKPACK_LOCATOR = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_T_SHIRT_LOCATOR = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_TO_CART_ONESIE_LOCATOR = (By.ID, "add-to-cart-sauce-labs-onesie")

    # Методы для взаимодействия с элементами
    def add_backpack_to_cart(self):
        """Добавление рюкзака в корзину."""
        backpack_add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BACKPACK_LOCATOR))
        backpack_add_to_cart_button.click()

    def add_t_shirt_to_cart(self):
        """Добавление футболки в корзину."""
        t_shirt_add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_T_SHIRT_LOCATOR))
        t_shirt_add_to_cart_button.click()

    def add_onesie_to_cart(self):
        """Добавление комбинезона в корзину."""
        onesie_add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_ONESIE_LOCATOR))
        onesie_add_to_cart_button.click()