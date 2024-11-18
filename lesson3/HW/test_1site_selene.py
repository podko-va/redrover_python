from selene import browser, be, have
from selene.support.shared import browser

# Инициализация браузера
browser.config.browser_name = 'chrome'
browser.open('https://www.selenium.dev/selenium/web/dynamic.html')

# Тест 1: Проверка загрузки страницы
browser.should(have.title('Dynamic Controls'))

# Тест 2: Проверка наличия кнопки "Remove"
remove_button = browser.element('//button[text()="Remove"]')
remove_button.should(be.visible)

# Тест 3: Проверка удаления элемента
remove_button.click()
browser.element('#checkbox').should(be.not_.visible)
browser.should(have.text("It's gone!"))

# Тест 4: Проверка добавления элемента
add_button = browser.element('//button[text()="Add"]')
add_button.click()
browser.element('#checkbox').should(be.visible)
browser.should(have.text("It's back!"))

# Тест 5: Проверка включения поля ввода
enable_button = browser.element('//button[text()="Enable"]')
enable_button.click()
browser.element('//input[@type="text"]').should(be.enabled)

# Тест 6: Проверка отключения поля ввода
disable_button = browser.element('//button[text()="Disable"]')
disable_button.click()
browser.element('//input[@type="text"]').should(be.disabled)

# Закрытие браузера
browser.quit()