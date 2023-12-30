from sqlalchemy.exc import SQLAlchemyError
from console_colors.console_colors import print_colored
from load_aux_scripts.sqlalchemy_engine import create_sqlalchemy_engine, disconnect_sqlalchemy_engine

def insert_records(table_name, df_to_insert):

    engine = create_sqlalchemy_engine()

    try:
        df_to_insert.to_sql(table_name, engine, if_exists='append', index=False)
        
        message = f"Data inserted successfully into {table_name}."
        if table_name == 'supermarket_prices':
            color = 'YELLOW'
        else:
            color = 'PURPLE'
        print_colored(message, color)

    except SQLAlchemyError as e:
        print(f"Error inserting data into {table_name}:", e)

    disconnect_sqlalchemy_engine(engine)