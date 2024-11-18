from pages.base_page import BasePage
from locators.download_page_locators_heroku import DownLoadLocators

class DownLoadPage(BasePage):
    locators = DownLoadLocators()
    
    def download_file(self):
        self.element_is_visible(self.locators.DOWNLOAD_LOCATOR).click()