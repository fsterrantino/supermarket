from psycopg2 import Error
from console_colors.console_colors import print_colored
from load_aux_scripts.psycopg_connection import psycopg_connection, psycopg_disconnection
import sys

def merge_products():

    cursor, connection = psycopg_connection()

    merge_products_query = f'''
        INSERT INTO 
            supermarket_products (sku, product_brand, product_description, timestamp)
        SELECT 
            tsp.sku,
            tsp.brand, 
            tsp.description,
            CAST(tsp.timestamp as timestamp)
        FROM 
            temporary_supermarket_products tsp
        WHERE NOT EXISTS (
            SELECT sp.sku
            FROM supermarket_products sp
            WHERE 
                tsp.sku = sp.sku
        );
    '''
    delete_temporary_table_query = f'''
        DROP TABLE temporary_supermarket_products;
    '''

    try:
        cursor.execute(merge_products_query)
        connection.commit()

        message = f"Data merged successfully from temporary table to the original table."
        print_colored(message, 'PURPLE')
        
        cursor.execute(delete_temporary_table_query)
        connection.commit()
        # print(f'Temporary table dropped.')
        psycopg_disconnection(cursor, connection)

    except Error as e:
        print(f"Error merging temporary table with original table: {e}.")
        sys.exit()