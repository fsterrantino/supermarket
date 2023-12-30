from load_aux_scripts.count_db_table_rows import count_db_table_rows
from load_aux_scripts.create_table import create_table
from load_aux_scripts.insert_records import insert_records
from load_aux_scripts.merge_products import merge_products
from load_aux_scripts.check_for_duplicated_products import check_for_duplicated_products
from load_aux_scripts.tables_columns_definitions import products_table_columns
from console_colors.console_colors import print_colored

def update_products_table(df_to_insert):

    print_colored('Updating products table.', 'PURPLE')
    products_inventory_count = count_db_table_rows('supermarket_products')

    message = f'Current inventoried products: {products_inventory_count}'
    print_colored(message, 'CYAN')

    today_products_count = df_to_insert.shape[0]
    message = f'Products with prices today: {today_products_count}.'
    print_colored(message, 'CYAN')  

    df_unique_products = check_for_duplicated_products(df_to_insert)
    create_table(name='supermarket_products', type='temporary', columns_definition=products_table_columns)

    insert_records('temporary_supermarket_products', df_unique_products)
    merge_products()

    products_inventory_count_update = count_db_table_rows('supermarket_products')
    message = f'Products inventory updated: {products_inventory_count_update}.'
    print_colored(message, 'CYAN')

    message = f'New products inserted: {products_inventory_count_update - products_inventory_count}.'
    print_colored(message, 'CYAN')
    