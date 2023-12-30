from load_aux_scripts.psycopg_connection import psycopg_connection, psycopg_disconnection

def count_db_table_rows(table_name):

    cursor, connection = psycopg_connection()
    check_query = f'''
        SELECT count(*)
        FROM {table_name}
    '''

    cursor.execute(check_query)
    connection.commit()

    count_result = cursor.fetchone()[0] 
    psycopg_disconnection(cursor, connection)

    return count_result

