from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    # Тест 1: Проверка загрузки страницы
    assert "The Internet" in driver.title

    # Тест 2: Проверка кнопки "Start"
    start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
    assert start_button.is_displayed()

    # Тест 3: Проверка загрузки элемента после нажатия кнопки "Start"
    start_button.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "finish")))
    finish_text = driver.find_element(By.ID, "finish").text
    assert "Hello World!" in finish_text

finally:
    # Закрытие браузера
    driver.quit()