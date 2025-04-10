class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса главной страницы.

        :param driver: Экземпляр веб-драйвера Selenium
        :type driver: WebDriver
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )  # URL главной страницы

    def load(self):
        """
        Загружает главную страницу.

        :return: None
        """
        self.driver.get(self.url)