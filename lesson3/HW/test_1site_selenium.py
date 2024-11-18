from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

    # Тест 1: Проверка загрузки страницы
    assert "Dynamic Controls" in driver.title

    # Тест 2: Проверка наличия кнопки "Remove"
    remove_button = driver.find_element(By.XPATH, "//button[text()='Remove']")
    assert remove_button.is_displayed()

    # Тест 3: Проверка удаления элемента
    remove_button.click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "checkbox")))
    assert "It's gone!" in driver.page_source

    # Тест 4: Проверка добавления элемента
    add_button = driver.find_element(By.XPATH, "//button[text()='Add']")
    add_button.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "checkbox")))
    assert "It's back!" in driver.page_source

    # Тест 5: Проверка включения поля ввода
    enable_button = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enable_button.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
    input_field = driver.find_element(By.XPATH, "//input[@type='text']")
    assert input_field.is_enabled()

    # Тест 6: Проверка отключения поля ввода
    disable_button = driver.find_element(By.XPATH, "//button[text()='Disable']")
    disable_button.click()
    WebDriverWait(driver, 10).until(EC.not_(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))))
    assert not input_field.is_enabled()

finally:
    # Закрытие браузера
    driver.quit()