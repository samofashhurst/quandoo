import common

class QuandooHovers(object):
    def __init__(self, driver):
        self.driver = driver

    def get_number_avatars(self):
        elements = self.driver.find_elements_by_xpath(
            "//div[@class='figure']/img")
        return len(elements)

    def hover(self, index):
        common.hover(self.driver, 'xpath',
                     "//div[@class='figure'][" + str(index) + "]/img")                     

    def is_username_shown(self, index):
        element = self.driver.find_element_by_xpath(
            "//div[@class='figure'][" + str(index) + "]/div")
        return element.is_displayed()
