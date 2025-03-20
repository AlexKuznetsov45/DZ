from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы элементов
    CART_LINK_LOCATOR = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON_LOCATOR = (By.CLASS_NAME, "checkout_button")

    # Методы для взаимодействия с элементами
    def go_to_cart(self):
        """Переход в корзину."""
        cart_link = self.driver.find_element(*self.CART_LINK_LOCATOR)
        cart_link.click()

    def click_checkout(self):
        """Нажатие на кнопку Checkout."""
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON_LOCATOR))
        checkout_button.click()