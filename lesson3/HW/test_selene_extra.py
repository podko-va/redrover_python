from selene import be, have
from selene.support.shared import browser, config
import requests

#AddRemoveElements
class TestAddRemoveElements:
    def setup_method(self):
        browser.config.browser_name = 'chrome'
        browser.open('https://the-internet.herokuapp.com/add_remove_elements/')

    def teardown_method(self):
        browser.quit()

    def test_add_remove_elements(self):
        add_button = browser.element('button[onclick="addElement()"]')
        add_button.click()
        add_button.click()  # Добавляем два элемента

        elements = browser.all('.added-manually')
        elements.should(have.size(2))  # Проверяем, что добавлено два элемента

        elements.first.click()  # Удаляем первый элемент
        elements.should(have.size(1))  # Проверяем, что остался один элемент

        elements.first.click()  # Удаляем оставшийся элемент
        elements.should(have.size(0))  # Проверяем, что все элементы удалены

#Basic Auth
class TestBasicAuth:
    def setup_method(self):
        browser.config.browser_name = 'chrome'
        browser.open('https://admin:admin@the-internet.herokuapp.com/basic_auth')

    def teardown_method(self):
        browser.quit()

    def test_basic_auth(self):
        success_message = browser.element('p')
        success_message.should(have.text('Congratulations! You must have the proper credentials.'))

#3. Broken Images
class TestBrokenImages:
    def setup_method(self):
        browser.config.browser_name = 'chrome'
        browser.open('https://the-internet.herokuapp.com/broken_images')

    def teardown_method(self):
        browser.quit()

    def test_broken_images(self):
        original_timeout = config.timeout
        config.timeout = 10
        try:
            images = browser.all('img')
            for img in images:
                response = requests.get(img.get_attribute('src'))
                assert response.status_code == 200, f"Broken image found: {img.get_attribute('src')}"
        finally:
            config.timeout = original_timeout

# 4. Checkboxes
class TestCheckboxes:
    def setup_method(self):
        browser.config.browser_name = 'chrome'
        browser.open('https://the-internet.herokuapp.com/checkboxes')

    def teardown_method(self):
        browser.quit()

    def test_checkboxes(self):
        checkboxes = browser.all('input[type="checkbox"]')

        # Проверяем, что первый чекбокс не выбран, а второй выбран
        checkboxes.first.should_not(be.selected)
        checkboxes.last.should(be.selected)

        # Выбираем первый чекбокс и снимаем выбор со второго
        checkboxes.first.click()
        checkboxes.last.click()

        # Проверяем, что первый чекбокс выбран, а второй не выбран
        checkboxes.first.should(be.selected)
        checkboxes.last.should_not(be.selected)
