from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Инициализируем драйвер
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Переходим на сайт
driver.get("http://uitestingplayground.com/textinput")

# Ожидаем полной загрузки страницы
wait = WebDriverWait(driver, 4)
wait.until(EC.presence_of_element_located((By.ID, 'newButtonName')))

# Вводим текст в поле ввода
input_field = driver.find_element(By.ID, 'newButtonName')
input_field.send_keys("SkyPro")

# Нажимаем на кнопку
submit_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
submit_button.click()

# Получаем новый текст кнопки и выводим его в консоль
new_button_text = submit_button.text
print(new_button_text)

# Закрываем браузер
driver.quit()