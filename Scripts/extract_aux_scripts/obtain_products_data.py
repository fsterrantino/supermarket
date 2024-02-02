from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from extract_aux_scripts.get_element_text_by_xpath import get_element_text_by_xpath

def obtain_products_data(product_container_list, driver):
    products_list = []
    for (i, product) in enumerate(product_container_list):
        try:
            product_dict = {} 
            parent_wait = WebDriverWait(product, 3)
            product_section = parent_wait.until(EC.presence_of_element_located((By.TAG_NAME, 'section')))

            product_section_text_list = product_section.text.splitlines()
            if 'Ver Producto' in product_section_text_list:
                product_section_text_list.remove('Ver Producto')

            print('Index:', i, '-', product_section_text_list)

            product_dict['id'] = product.get_attribute("id")
            product_dict['brand'] = get_element_text_by_xpath(product, './/section/a/article/div[3]/span')
            product_dict['description'] = get_element_text_by_xpath(product, './/section/a/article/div[4]/h2/span')
            product_dict['final_price'] = get_element_text_by_xpath(product, './/section/a/article/div[5]/div/div/div/div[1]/div/span/div[1]/div')
            product_dict['discount'] = get_element_text_by_xpath(product, './/section/a/article/div[5]/div/div/div/div[1]/div/span/div[2]/div/span')
            product_dict['original_price'] = get_element_text_by_xpath(product, './/section/a/article/div[5]/div/div/div/div[1]/div/div[2]')
            product_dict['regular_price'] = get_element_text_by_xpath(product, './/section/a/article/div[5]/div/div/div/div[1]/div/div[3]/span')

            products_list.append(product_dict)
        
        except Exception as e:
            print(f"Caught error: {e}")
            pass
    
    return products_list