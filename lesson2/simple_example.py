# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get("http://195.133.27.184/")


# element = browser.find_element(By.XPATH, "//a[@href='/2/']")
# element.is_displayed()
# element.click()
# assert browser.current_url == "http://195.133.27.184/2/", "Wrong URL"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://195.133.27.184/")

try:
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/login/']"))#изменения на странице
    )
    element.click()
    assert browser.current_url == "http://195.133.27.184/login/", "Wrong URL"
finally:
    browser.quit()