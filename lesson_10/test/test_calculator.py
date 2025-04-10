from ..pages.CalculatorPage import CalculatorPage
from allure import title, description, feature, severity, step

@title("Тестирование калькулятора")
@description("Тестирует последовательность действий на калькуляторе.")
@feature("Калькулятор")
@severity(severity_level="normal")
def test_calculator_flow(browser):
    """Тестовая функция для проверки калькулятора."""
    calculator_page = CalculatorPage(browser)

    with step("Открываем страницу калькулятора"):
        calculator_page.open()

    with step("Устанавливаем задержку 45 мс"):
        calculator_page.set_delay(45)

    with step("Последовательно нажимаем на кнопки калькулятора"):
        calculator_page.press_button(calculator_page.BUTTON_7_LOCATOR)
        calculator_page.press_button(calculator_page.BUTTON_PLUS_LOCATOR)
        calculator_page.press_button(calculator_page.BUTTON_8_LOCATOR)
        calculator_page.press_button(calculator_page.BUTTON_EQUALS_LOCATOR)

    with step("Ожидаем исчезновение спинора"):
        calculator_page.wait_for_spinner_disappear()

    with step("Получаем и проверяем результат"):
        result = calculator_page.get_result()
        assert (
            result == "15"
        ), f"Результат не совпадает. Ожидается: 15, Фактический: {result}"