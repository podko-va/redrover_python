from selene import browser, be, have
from selene.support.shared import browser

# Инициализация браузера
browser.config.browser_name = 'chrome'
browser.open('https://the-internet.herokuapp.com/dynamic_loading/1')

# Тест 1: Проверка загрузки страницы
browser.should(have.title('The Internet'))

# Тест 2: Проверка кнопки "Start"
start_button = browser.element('//div[@id="start"]/button')
start_button.should(be.visible)

# Тест 3: Проверка загрузки элемента после нажатия кнопки "Start"
start_button.click()
browser.element('#finish').should(be.visible)
browser.element('#finish').should(have.text('Hello World!'))

# Закрытие браузера
browser.quit()

