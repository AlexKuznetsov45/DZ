from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Инициализация драйвера
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Перейти на страницу
driver.get("http://uitestingplayground.com/ajax")

# Явное ожидание загрузки страницы
driver.implicitly_wait(20)  # Ждать до 20 секунд до нахождения элемента

# Найти и нажать на синюю кнопку
button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Button Triggering AJAX Request')]")))
button.click()

# Найти элемент с текстом
content = driver.find_element(By.CSS_SELECTOR, "#content")
paragraph = content.find_element(By.CSS_SELECTOR, "p.bg-success")

# Получить и вывести текст
text = paragraph.text
print(text)

# Закрыть браузер
driver.quit()