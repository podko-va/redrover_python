from pages.upload_page import UpLoadPage
from data.urls import Urls
import time
from functions import get_root_path

class TestDownload:
    url = Urls()

    def test_upload(self,driver):
         file_path = get_root_path("review\data\uploadfile\upload_page_locators_heroku.py")
         page = UpLoadPage(driver, f"{self.url.herokuapp_base_url}upload")
         page.open()
         page.upload_file(file_path)
         h3_text, file_name = page.check_upload_file()
         print(h3_text)
         print(file_name)
         time.sleep(5)