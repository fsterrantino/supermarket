import json
from extract_aux_scripts.safe_find_element import safe_find_element

def obtain_skus_list(wait):
    products_script_xpath = '/html/body/div[2]/div/div[1]/div/script'
    products_script = safe_find_element(products_script_xpath, 'xpath', wait)
    script_text = products_script.get_attribute('text')
    parsed_json = json.loads(script_text)
    page_skus_list = []

    for element in parsed_json['itemListElement']:
        sku = element['item']['sku']
        page_skus_list.append(sku)
        
    return page_skus_list