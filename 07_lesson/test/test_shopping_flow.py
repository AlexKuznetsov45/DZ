import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.shop import Shop
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def browser():
    """Фикстура для запуска браузера."""
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_shopping_flow(browser):
    """Тестовая функция для проверки процесса покупки."""
    # Создание экземпляров классов страниц
    shop = Shop(browser)
    product_page = ProductPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)

    # Открытие главной страницы и авторизация
    shop.go_to_shop()
    shop.login("standard_user", "secret_sauce")

    # Добавление товаров в корзину
    product_page.add_backpack_to_cart()
    product_page.add_t_shirt_to_cart()
    product_page.add_onesie_to_cart()

    # Переход в корзину
    cart_page.go_to_cart()

    # Нажатие на Checkout
    cart_page.click_checkout()

    # Заполнение формы своими данными
    checkout_page.fill_information("John", "Doe", "12345")

    # Получение итоговой стоимости
    total_cost = checkout_page.get_total_cost()

    # Проверка итоговой суммы
    assert total_cost == "Total: $58.29", f"Итоговая сумма не совпадает. Ожидается: Total: $58.29, Фактическая: {total_cost}"