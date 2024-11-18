from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

URL = "https://victoretc.github.io/selenium_waits/"

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

# Explicit waits
def test_registration_explicit_waits(driver, wait):
    driver.get(URL)
    
    h1_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert h1_element.text == "Практика с ожиданиями в Selenium"

    #"Начать тестирование"
    start_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Начать тестирование']")))
    start_button.click()

    # логин и пароль
    login_field = wait.until(EC.presence_of_element_located((By.ID, "login")))
    login_field.send_keys("login")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("password")

    # флажок в чекбокс
    checkbox = driver.find_element(By.ID, "agree")
    checkbox.click()

    # Клик по кнопке "Зарегистрироваться"
    register_button = driver.find_element(By.ID, "register")
    register_button.click()

    loading_indicator = wait.until(EC.visibility_of_element_located((By.ID, "loader")))
    success_message = wait.until(EC.visibility_of_element_located((By.ID, "successMessage")))
    assert success_message.text == "Вы успешно зарегистрированы!"

# Implicit waits
def test_registration_implicit_waits(driver):
    driver.implicitly_wait(10)
    driver.get(URL)

    h1_element = driver.find_element(By.TAG_NAME, "h1")
    assert h1_element.text == "Практика с ожиданиями в Selenium"

    start_button = driver.find_element(By.XPATH, "//button[text()='Начать тестирование']")
    start_button.click()

    login_field = driver.find_element(By.ID, "login")
    login_field.send_keys("login")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("password")

    checkbox = driver.find_element(By.ID, "agree")
    checkbox.click()

    register_button = driver.find_element(By.ID, "register")
    register_button.click()
    time.sleep(5)
    loading_indicator = driver.find_element(By.ID, "loader")
    success_message = driver.find_element(By.XPATH, "//*[@id='successMessage']")
    assert success_message.text == "Вы успешно зарегистрированы!"

    # success_registration = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='successMessage']")))
    # assert success_registration.is_displayed()
    # assert success_registration.text == 'Вы успешно зарегистрированы!'

# time.sleep()
def test_registration_with_sleep(driver):
    driver.get(URL)
    time.sleep(2)  
    h1_element = driver.find_element(By.TAG_NAME, "h1")
    assert h1_element.text == "Практика с ожиданиями в Selenium"
    time.sleep(5)
    start_button = driver.find_element(By.XPATH, "//button[@id='startTest']")
    start_button.click()
    time.sleep(1)
    login_field = driver.find_element(By.ID, "login")
    login_field.send_keys("login")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("password")
    checkbox = driver.find_element(By.ID, "agree")
    checkbox.click()

    register_button = driver.find_element(By.ID, "register")
    register_button.click()

    time.sleep(5)
    success_message = driver.find_element(By.XPATH, "//*[@id='successMessage']")
    assert success_message is not None, "Элемент successMessage не найден на странице"
    assert success_message.text == "Вы успешно зарегистрированы!"
    
