from ..pages.Shop import Shop
from ..pages.ProductPage import ProductPage
from ..pages.CartPage import CartPage
from ..pages.CheckoutPage import CheckoutPage
from allure import title, description, feature, severity, step
from selenium import webdriver


@title("Тестирование процесса покупки")
@description("Тестирует полный процесс покупки от выбора товара до оплаты.")
@feature("Покупка")
@severity(severity_level="critical")
def test_shopping_flow(browser):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # Создание экземпляров классов страниц
    shop = Shop(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with step("Открытие главной страницы и авторизация"):
        shop.go_to_shop()
        shop.login("standard_user", "secret_sauce")

    with step("Добавление товаров в корзину"):
        product_page.add_backpack_to_cart()
        product_page.add_t_shirt_to_cart()
        product_page.add_onesie_to_cart()

    with step("Переход в корзину"):
        cart_page.go_to_cart()

    with step("Нажатие на Checkout"):
        cart_page.click_checkout()

    with step("Заполнение формы своими данными"):
        checkout_page.fill_information("John", "Doe", "12345")

    with step("Получение итоговой стоимости"):
        total_cost = checkout_page.get_total_cost()

    with step("Проверка итоговой суммы"):
        assert (
            total_cost == "Total: $58.29"
        ), f"Итоговая сумма не совпадает. Ожидается: Total: $58.29, Фактическая: {total_cost}"