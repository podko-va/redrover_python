from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("https://demoqa.com/dynamic-properties")

    # Тест 1: Проверка загрузки страницы
    assert "Dynamic Properties" in driver.title

    # Тест 2: Проверка кнопки, которая становится активной через 5 секунд
    enable_after_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "enableAfter"))
    )
    assert enable_after_button.is_enabled()

    # Тест 3: Проверка кнопки, которая меняет цвет через 5 секунд
    color_change_button = driver.find_element(By.ID, "colorChange")
    WebDriverWait(driver, 10).until(
    EC.element_attribute_to_include((By.ID, "colorChange"), "class")
    )
    assert "text-danger" in color_change_button.get_attribute("class")

    # Тест 4: Проверка появления кнопки через 5 секунд
    visible_after_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "visibleAfter"))
    )
    assert visible_after_button.is_displayed()

finally:
    # Закрытие браузера
    driver.quit()