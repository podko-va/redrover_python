import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from functions import get_root_path


download_path = get_root_path("data/download")

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.defaul_directory": download_path
    }
    options.add_argument("--window-size=1600,1000")
    # options.add_argument("--incognito")
    # options.add_argument("--ignore-cretificate-errors")
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today}", attachment_type=allure.attachment_type.PNG)
    driver.quit()