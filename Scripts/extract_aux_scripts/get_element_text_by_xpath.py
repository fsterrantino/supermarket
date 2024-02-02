from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def get_element_text_by_xpath(parent_element, xpath):
    try:
        element = parent_element.find_element(By.XPATH, xpath)
        return element.text
    except NoSuchElementException:
        return ""