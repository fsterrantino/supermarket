import json
from extract_aux_scripts.safe_find_element import safe_find_element

def add_skus_column(df):

    products_script_xpath = '/html/body/div[2]/div/div[1]/div/script'
    products_script = safe_find_element(products_script_xpath, 'xpath')
    script_text = products_script.get_attribute('text')
    parsed_json = json.loads(script_text)
    skus_list = []

    for element in parsed_json['itemListElement']:
        sku = element['item']['sku']
        skus_list.append(sku)
        
    df['sku'] = skus_list[:len(df)]
    return df