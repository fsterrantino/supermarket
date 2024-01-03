from extract_aux_scripts.safe_find_element import safe_find_element

def enter_warehouse_section():
    categories_button_xpath = '/html/body/div[2]/div/div[1]/div/div[5]/div[1]/div/div/div[2]/section/div/div[1]/li/nav/ul/li/div/span/div'
    categories_button = safe_find_element(categories_button_xpath, 'xpath')
    categories_button.click()

    store_button_id = 'menu-item-almacen'
    store_button = safe_find_element(store_button_id, 'id')
    store_button.click()

    see_all_xpath = '/html/body/div[2]/div/div[1]/div/div[11]/div/div[2]/section/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[1]/a'
    see_all_button = safe_find_element(see_all_xpath, 'xpath')
    see_all_button.click()

    try:
        not_suscribe_button_id = 'btnNoIdWpnPush'
        not_suscribe_button = safe_find_element(not_suscribe_button_id, 'id')
        not_suscribe_button.click()
    except:
        pass