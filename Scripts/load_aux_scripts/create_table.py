from load_aux_scripts.psycopg_connection import psycopg_connection, psycopg_disconnection

def create_table(name, type, columns_definition):

    cursor, connection = psycopg_connection()
    expected_table_type = ['normal', 'temporary']
    if type not in expected_table_type:
        raise ValueError(f"Unexpected parameter '{type}'. Allowed parameters are 'normal' and 'temporary'.")
    
    if type == 'normal':
        type = ''

    if type == 'temporary':
        name = 'temporary_' + name

    create_table_query = f'''
        CREATE {type} TABLE IF NOT EXISTS {name} (
            {columns_definition}
        );
    '''

    cursor.execute(create_table_query)
    connection.commit()
    psycopg_disconnection


