from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def obtain_products_data(product_container_list):
    products_list = []
    for (i, product) in enumerate(product_container_list):
        try:
            product_dict = {} 
            parent_wait = WebDriverWait(product, 3)
            product_section = parent_wait.until(EC.presence_of_element_located((By.TAG_NAME, 'section')))
        
            product_section_text_list = product_section.text.splitlines()
            print('Index:', i, '-', product_section_text_list)
        
            match len(product_section_text_list):
                case 7:
                    product_dict['brand'] = product_section_text_list[0]
                    product_dict['description'] = product_section_text_list[1]
                    product_dict['final_price'] = product_section_text_list[2]
                    product_dict['original_price'] = product_section_text_list[3]
                    product_dict['discount'] = product_section_text_list[4]
                    product_dict['regular_price'] = product_section_text_list[5]
                case 5:
                    product_dict['brand'] = product_section_text_list[0]
                    product_dict['description'] = product_section_text_list[1]
                    product_dict['final_price'] = product_section_text_list[2]
                    product_dict['original_price'] = None
                    product_dict['discount'] = None
                    product_dict['regular_price'] = product_section_text_list[3]    

            products_list.append(product_dict)
        
        except Exception as e:
            print(f"Caught error: {e}")
            pass
    
    return products_list