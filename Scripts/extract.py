import pandas as pd
from extract_aux_scripts.obtain_products_data import obtain_products_data
from extract_aux_scripts.preload_products_webElements import preload_products_webElements
from extract_aux_scripts.scroll_products_pages import scroll_products_pages
from extract_aux_scripts.enter_warehouse_section import enter_warehouse_section
from extract_aux_scripts.initiate_driver import initiate_driver
from extract_aux_scripts.add_skus_column import add_skus_column
from extract_aux_scripts.get_archive_name import get_archive_name

driver, wait = initiate_driver()
enter_warehouse_section(wait)

pages_to_scroll = 40
scroll_products_pages(pages_to_scroll, driver, wait)

products_container = preload_products_webElements(driver, wait)
products_list = obtain_products_data(products_container)

df = pd.DataFrame(products_list)
df = add_skus_column(df)

target_folder, csv_name = get_archive_name()
df.to_csv(target_folder + csv_name, index = False, sep=';')

print('Csv generated.')
driver.quit()