from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages import common

class QuandooLogin(object):
    def __init__(self, driver):
        self.driver = driver

    def input_username(self, value):
        common.input_text(self.driver, 'id', 'username', value)

    def input_password(self, value):
        common.input_text(self.driver, 'id', 'password', value)

    def click_login(self):
        common.click_button(self.driver, 'xpath', 
            "//button/i[contains(text(),'Login')]")
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "flash")))

    def is_login_message_shown(self, message):
        elements = self.driver.find_elements_by_xpath(
            "//div[contains(text(),'" + message + "')]")
        if len(elements) == 0:
            found = False
        else:
            found = True
        return found
