from selenium.webdriver.common.action_chains import ActionChains

def input_text(driver, selector_type, selector, value):
    element = get_element(driver, selector_type, selector)
    element.send_keys(value)

def hover(driver, selector_type, selector):
    element = get_element(driver, selector_type, selector)
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()

def click_button(driver, selector_type, selector):
    element = get_element(driver, selector_type, selector)
    element.click()

def get_element(driver, selector_type, selector):
    if selector_type == 'id':
        element = driver.find_element_by_id(selector)
    else:
        element = driver.find_element_by_xpath(selector)

    # Make sure element is visible before returning
    driver.execute_script("arguments[0].scrollIntoView();", element)
    return element
