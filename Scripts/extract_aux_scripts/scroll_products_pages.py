from extract_aux_scripts.safe_find_element import safe_find_element

def scroll_products_pages(pages, driver, wait):
    total_products = 0
    while total_products == 0:
        products_shown_and_total_xpath = '/html/body/div[2]/div/div[1]/div/div[11]/div/div[2]/section/div[2]/div/div[3]/section/div/div/div/div/div[2]/div/div[5]/div/div/p/strong'
        products_shown_and_total = safe_find_element(products_shown_and_total_xpath, 'xpath', wait)
        
        total_products = int(products_shown_and_total.text.split(' ')[2])

    view_more_button_xpath = '/html/body/div[2]/div/div[1]/div/div[11]/div/div[2]/section/div[2]/div/div[3]/section/div/div/div/div/div[2]/div/div[6]/div/div/div/div/div/button/div'
    pages = 40

    for i in range(pages):
        view_more_button = safe_find_element(view_more_button_xpath, 'xpath', wait)    
        driver.execute_script("arguments[0].click();", view_more_button)