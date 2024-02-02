from selenium.webdriver.common.by import By
from extract_aux_scripts.safe_find_element import safe_find_element
from extract_aux_scripts.scroll_down_to_bottom import scroll_down_to_bottom

def preload_products_webElements(driver, wait):
    products_container_xpath = '//*[@id="gallery-layout-container"]'
    products_container = safe_find_element(products_container_xpath, 'xpath', wait)

    scroll_down_to_bottom(driver, scroll_speed=50)

    product_container_list = products_container.find_elements(By.XPATH, './div')
    
    return product_container_list