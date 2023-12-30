from console_colors.console_colors import print_colored
from load_aux_scripts.psycopg_connection import psycopg_connection, psycopg_disconnection

def check_timestamp_already_inserted(timestamp):
    message = 'Checking if records from this timestamp are already inserted.'
    print_colored(message, 'PURPLE')
    cursor, connection = psycopg_connection()

    check_query = f'''
        SELECT 1
        FROM supermarket_prices
        WHERE timestamp = '{timestamp}'
    '''

    cursor.execute(check_query)
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Returned {cursor.rowcount} records with the same timestamp.")
        psycopg_disconnection(cursor, connection)
        return True
    else:
        # No records found
        message = f"Records not present, they can be inserted."
        print_colored(message, 'PURPLE')
        psycopg_disconnection(cursor, connection)
        return False
