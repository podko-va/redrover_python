from playwright.sync_api import sync_playwright

def test_dynamic_loading():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

        # Тест 1: Проверка загрузки страницы
        assert "The Internet" in page.title()

        # Тест 2: Проверка кнопки "Start"
        start_button = page.locator('//div[@id="start"]/button')
        assert start_button.is_visible()

        # Тест 3: Проверка загрузки элемента после нажатия кнопки "Start"
        start_button.click()
        page.wait_for_selector('#finish', state='visible')
        finish_text = page.locator('#finish').inner_text()
        assert "Hello World!" in finish_text

        browser.close()

# Запуск теста
test_dynamic_loading()