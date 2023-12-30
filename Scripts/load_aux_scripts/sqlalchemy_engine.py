from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def create_sqlalchemy_engine():

    load_dotenv()
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    hostname = os.getenv('HOSTNAME')
    port = os.getenv('PORT')
    database_name = os.getenv('DATABASE_NAME')

    try:
        engine = create_engine(f'postgresql://{username}:{password}@{hostname}:{port}/{database_name}')
        # print("SQLAlchemy connection successful. Engine created.")
        return engine
    
    except SQLAlchemyError as e:
        print("Error creating SqlAlchemy engine:", e)
    
def disconnect_sqlalchemy_engine(engine):
    engine.dispose()
    # print("SQLAlchemy disconnected.")