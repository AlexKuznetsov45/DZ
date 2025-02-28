import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    """Фикстура для запуска браузера."""
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def login(browser, username, password):
    """Функция для авторизации на сайте."""
    browser.get("https://www.saucedemo.com/")
    username_input = browser.find_element(By.ID, "user-name")
    username_input.send_keys(username)
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()

def add_items_to_cart(browser, items):
    """Функция для добавления товаров в корзину."""
    for item in items:
        add_to_cart_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button"))
        )
        add_to_cart_button.click()

def go_to_cart(browser):
    """Функция для перехода в корзину."""
    cart_link = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

def click_checkout(browser):
    """Функция для нажатия на кнопку Checkout."""
    checkout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "checkout_button"))
    )
    checkout_button.click()

def fill_information(browser, first_name, last_name, postal_code):
    """Функция для заполнения формы информацией."""
    first_name_input = browser.find_element(By.ID, "first-name")
    first_name_input.send_keys(first_name)
    last_name_input = browser.find_element(By.ID, "last-name")
    last_name_input.send_keys(last_name)
    postal_code_input = browser.find_element(By.ID, "postal-code")
    postal_code_input.send_keys(postal_code)
    continue_button = browser.find_element(By.CLASS_NAME, "cart_button")
    continue_button.click()

def get_total_cost(browser):
    """Функция для получения итоговой стоимости."""
    total_cost = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.summary_total_label[data-test='total-label']"))
    ).text
    return total_cost

def test_shopping_flow(browser):
    """Тестовая функция для проверки процесса покупки."""
    # Авторизация
    login(browser, "standard_user", "secret_sauce")

    # Добавление товаров в корзину
    items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    add_items_to_cart(browser, items)

    # Переход в корзину
    go_to_cart(browser)

    # Нажатие на Checkout
    click_checkout(browser)

    # Заполнение формы
    fill_information(browser, "John", "Doe", "12345")

    # Получение итоговой стоимости
    total_cost = get_total_cost(browser)

    # Проверка итоговой суммы
    assert total_cost == "Total: $58.29", f"Итоговая сумма не совпадает. Ожидается: Total: $58.29, Фактическая: {total_cost}"