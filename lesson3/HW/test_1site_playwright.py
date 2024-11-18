from playwright.sync_api import sync_playwright

def test_dynamic_controls():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.selenium.dev/selenium/web/dynamic.html")

        # Тест 1: Проверка загрузки страницы
        assert page.title() == "Dynamic Controls"

        # Тест 2: Проверка наличия кнопки "Remove"
        remove_button = page.locator('//button[text()="Remove"]')
        assert remove_button.is_visible()

        # Тест 3: Проверка удаления элемента
        remove_button.click()
        page.wait_for_selector('#checkbox', state='hidden')
        assert "It's gone!" in page.content()

        # Тест 4: Проверка добавления элемента
        add_button = page.locator('//button[text()="Add"]')
        add_button.click()
        page.wait_for_selector('#checkbox', state='visible')
        assert "It's back!" in page.content()

        # Тест 5: Проверка включения поля ввода
        enable_button = page.locator('//button[text()="Enable"]')
        enable_button.click()
        page.wait_for_selector('//input[@type="text"]', state='enabled')
        input_field = page.locator('//input[@type="text"]')
        assert input_field.is_enabled()

        # Тест 6: Проверка отключения поля ввода
        disable_button = page.locator('//button[text()="Disable"]')
        disable_button.click()
        page.wait_for_selector('//input[@type="text"]', state='disabled')
        assert not input_field.is_enabled()

        browser.close()

# Запуск теста
test_dynamic_controls() 