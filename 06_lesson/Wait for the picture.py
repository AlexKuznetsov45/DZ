from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Инициализируем драйвер
driver = webdriver.Chrome(service=Service())

# Переходим на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидаем полной загрузки всех изображений
wait = WebDriverWait(driver, 60)
wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//img[@id='award']")))

# Находим третье изображение по xpath
third_image = driver.find_element(By.XPATH, "//img[@id='award']")

# Получаем значение атрибута src
third_image_src = third_image.get_attribute("src")

# Выводим значение в консоль
print(f"Третье изображение: {third_image_src}")

# Закрываем браузер
driver.quit()