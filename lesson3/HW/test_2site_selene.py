from selene import browser, be, have
from selene.support.conditions import have
from selene.support.shared import browser

# Инициализация браузера
browser.config.browser_name = 'chrome'
browser.open('https://demoqa.com/dynamic-properties')

# Тест 1: Проверка загрузки страницы
browser.should(have.title('Dynamic Properties'))

# Тест 2: Проверка кнопки, которая становится активной через 5 секунд
browser.element('#enableAfter').should(be.clickable)

# Тест 3: Проверка кнопки, которая меняет цвет через 5 секунд
browser.element('#colorChange').should(have.css_class('text-danger'))

# Тест 4: Проверка появления кнопки через 5 секунд
browser.element('#visibleAfter').should(be.visible)

# Закрытие браузера
browser.quit()