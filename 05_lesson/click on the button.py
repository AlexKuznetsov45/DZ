from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Шаг 2: Пять раз кликнить на кнопку Add Element.
add_element_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
for _ in range(5):
    add_element_button.click()

# Шаг 3: Посчитать со страницы список кнопок Delete.
delete_buttons = driver.find_elements(By.CSS_SELECTOR, "button[onclick='deleteElement()']")

# Шаг 4: Вывести на экран размер списка.
print(f"Количество кнопок Delete: {len(delete_buttons)}")

driver.quit()