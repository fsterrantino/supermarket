from console_colors.console_colors import print_colored
from load_aux_scripts.count_db_table_rows import count_db_table_rows
from load_aux_scripts.check_timestamp_already_inserted import check_timestamp_already_inserted
from load_aux_scripts.insert_records import insert_records

def update_prices_table(df_to_insert):
    # create_table(name='supermarket_prices', type='temporary', columns_definition=prices_table_columns)

    timestamp_to_be_inserted = df_to_insert['timestamp'][0]
    if check_timestamp_already_inserted(timestamp_to_be_inserted):
        raise Exception('Records with duplicated timestamp where detected. Stopping process.') 

    prices_inventoried_count = count_db_table_rows('supermarket_prices')
    message = f'Prices inventoried: {prices_inventoried_count}.'
    print_colored(message, 'YELLOW')

    message = f'Prices to insert: {df_to_insert.shape[0]}'
    print_colored(message, 'YELLOW')

    columns_to_be_inserted = [
        'sku', 
        'final_price', 
        'original_price', 
        'discount', 
        'regular_price', 
        'regular_price_measure', 
        'regular_price_un', 
        'timestamp'
    ]

    insert_records('supermarket_prices', df_to_insert[columns_to_be_inserted])