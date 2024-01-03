from extract_aux_scripts.safe_find_element import safe_find_element, driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def preload_products_webElements():

    products_container_xpath = '//*[@id="gallery-layout-container"]'
    products_container = safe_find_element(products_container_xpath, 'xpath')
    product_container_list = products_container.find_elements(By.XPATH, './div')

    for product_container in product_container_list:
        try:
            action = ActionChains(driver)
            action.move_to_element(product_container).perform()
        except:
            pass

    product_container_list = products_container.find_elements(By.XPATH, './div')
    return product_container_list