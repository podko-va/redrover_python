from playwright.sync_api import sync_playwright

def test_dynamic_properties():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://demoqa.com/dynamic-properties")

        # Тест 1: Проверка загрузки страницы
        assert page.title() == "Dynamic Properties"

        # Тест 2: Проверка кнопки, которая становится активной через 5 секунд
        enable_after_button = page.wait_for_selector("#enableAfter", state="enabled")
        assert enable_after_button.is_enabled()

        # Тест 3: Проверка кнопки, которая меняет цвет через 5 секунд
        color_change_button = page.wait_for_selector("#colorChange")
        page.wait_for_selector("#colorChange.text-danger")
        class_name = color_change_button.get_attribute("class")
        assert "text-danger" in class_name

        # Тест 4: Проверка появления кнопки через 5 секунд
        visible_after_button = page.wait_for_selector("#visibleAfter", state="visible")
        assert visible_after_button.is_visible()

        browser.close()

# Запуск теста
test_dynamic_properties()