import pandas as pd
from datetime import datetime

def read_df_to_insert():
    current_date = datetime.now()
    # formatted_date = current_date.strftime("%d.%m.%Y")
    formatted_date = '29.12.2023'
    csv_name = './Archives/Transformed_products - ' + formatted_date + '.csv'

    df = pd.read_csv(csv_name, index_col=False, sep=';')
    df.columns = df.columns.str.lower()

    return df