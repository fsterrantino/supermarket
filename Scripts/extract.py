import pandas as pd
from extract_aux_scripts.obtain_products_data import obtain_products_data
from extract_aux_scripts.preload_products_webElements import preload_products_webElements
from extract_aux_scripts.obtain_skus_list import obtain_skus_list
from extract_aux_scripts.get_archive_name import get_archive_name
from extract_aux_scripts.initiate_driver import initiate_driver

driver, wait = initiate_driver()

pages_to_scroll = 20
products_list = []
skus_list = []
for page in range(1, pages_to_scroll + 1):
        print(f'Scraping page {page}.')
        url = f'https://www.jumbo.com.ar/almacen?page={page}'
        driver.get(url)
    
        page_products_container = preload_products_webElements(driver, wait)
        page_products_list = obtain_products_data(page_products_container, driver)
        products_list += page_products_list

        skus_list += obtain_skus_list(wait)

df = pd.DataFrame(products_list)
df.insert(0, 'sku', skus_list)

target_folder, csv_name = get_archive_name()
df.to_csv(target_folder + csv_name, index = False, sep=';')

print('Csv generated.')
driver.quit()