import psycopg2

def psycopg_connection():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="123456",
            host="localhost",
            port="5432",
            database="postgres"
        )
        cursor = connection.cursor()
        # print('Pyscopg connection established.')

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)

    return cursor, connection

def psycopg_disconnection(cursor, connection):
    if connection:
        cursor.close()
        connection.close()
        # print("Pyscopg connection closed.")