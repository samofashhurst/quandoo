from pages import common

class QuandooTables(object):
    def __init__(self, driver):
        self.driver = driver

    def click_column_heading(self, table_name, column_name):
        xpath = "//h4[text()='" + table_name + "']/following::th/span[text()='" + column_name + "']"
        common.get_element(self.driver, 'xpath', xpath).click()

    def get_column_values(self, table_name, column_name):
        # Get column index
        elements = self.driver.find_elements_by_xpath(
            "//h4[text()='" + table_name + "']/following::th")
        column_names = []
        for element in elements:
            column_names.append(element.text)
        index = column_names.index(column_name)

        # Get column values
        elements = self.driver.find_elements_by_xpath(
            "//h4[text()='" + table_name + "']/following::tbody/tr/td[" + str(index+1) + "]")
        column_values = []
        for element in elements:
            column_values.append(element.text)
        
        return column_values
