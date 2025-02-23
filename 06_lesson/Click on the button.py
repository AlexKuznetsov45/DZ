from selenium import webdriver                  # Импортируем модуль webdriver из библиотеки Selenium
from selenium.webdriver.common.by import By      # Импортируем класс By для определения локаторов элементов
from selenium.webdriver.support.ui import WebDriverWait  # Импортируем модуль для ожидания элементов
from selenium.webdriver.support import expected_conditions as EC  # Импортируем набор условий ожидания

# Инициализация драйвера для браузера Chrome
driver = webdriver.Chrome()

# Открытие веб-сайта
driver.get("http://uitestingplayground.com/ajax")

# Ожидание появления кнопки с классом btn-primary
button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))  # Ожидаем кнопку, которая должна быть кликбельной
)

# Нажатие на кнопку
button.click()

# Ожидание появления параграфа с классом bg-success
text = WebDriverWait(driver, 16).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))  # Ожидаем параграф с определенным стилем
).text  # Получаем текст из найденного элемента

# Печать текста
print(text)

# Закрытие браузера
driver.quit()