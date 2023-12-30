from load_aux_scripts.create_table import create_table
from load_aux_scripts.read_df_to_insert import read_df_to_insert
from load_aux_scripts.update_products_table import update_products_table
from load_aux_scripts.update_prices_table import update_prices_table
from load_aux_scripts.tables_columns_definitions import prices_table_columns, products_table_columns

create_table(
    name = 'supermarket_prices', 
    type = 'normal', 
    columns_definition = prices_table_columns
    )
create_table(
    name = 'supermarket_products', 
    type = 'normal', 
    columns_definition = products_table_columns
    )

df_to_insert = read_df_to_insert()
update_products_table(df_to_insert)
update_prices_table(df_to_insert)



