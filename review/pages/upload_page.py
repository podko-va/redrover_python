from pages.base_page import BasePage
from locators.upload_page_locators_heroku import UploadPageLoadLocators

class UpLoadPage(BasePage):
    locators = UploadPageLoadLocators()
    
    def upload_file(self,file_path):
        self.element_is_visible(self.locators.UPLOAD_LOCATOR).send_keys(file_path)
        self.element_is_clicable(self.locators.SUBMIT_BTN).click()

    def check_upload_file(self):
        h3_text = self.element_is_visible(self.locators.HEADER_TEXT_LOCATOR).text
        file_name = self.element_is_visible(self.locators.UPLOAD_FILE_NAME_LOCATOR).text
        return h3_text, file_name