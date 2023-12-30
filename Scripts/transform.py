import pandas as pd
from datetime import datetime
import os
from transform_aux_scripts.add_timestamp_column import add_timestamp_column

current_date = datetime.now()
formatted_date = current_date.strftime("%d.%m.%Y")
# formatted_date = '08.12.2023'
csv_name_input = '/Products - ' + formatted_date + '.csv'

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
target_folder = os.path.join(parent_dir, 'Archives')

df = pd.read_csv(target_folder + csv_name_input, sep=';')

df['Brand'] = df['Brand'].str.replace('SIN MARCA', '')
df['Brand'] = df['Brand'].fillna('SIN MARCA')

df['Regular_price'] = df['Regular_price'].str.replace('Precio regular: $', '')
df['Regular_price'] = df['Regular_price'].str.replace(' x ', ' ')

expanded_precio_regular = df['Regular_price'].str.split(' ', expand = True)
df['Regular_price'] = expanded_precio_regular[0]
expanded_precio_regular[2] = expanded_precio_regular[2].str.replace('.', '')

def format_regular_price_measure(row):
    if row[2]:
        return row[1], row[2]
    else:
        return str(1), row[1]

df[['Regular_price_measure', 'Regular_price_un']] = expanded_precio_regular.apply(lambda row: pd.Series(format_regular_price_measure(row)), axis=1)

def format_price_columns(column):
    column = column.str.replace('$', '')
    column = column.str.replace('.', '')
    column = column.str.replace(',', '.')

    column = pd.to_numeric(column, errors='coerce')
    return column

df['Final_price'] = format_price_columns(df['Final_price'])
df['Original_price'] = format_price_columns(df['Original_price'])
df['Regular_price'] = format_price_columns(df['Regular_price'])

csv_name_output = '/Transformed_products - ' + formatted_date + '.csv'

add_timestamp_column(df)

column_to_move = 'sku'
if column_to_move in df.columns:
    columns = [column_to_move] + [col for col in df if col != column_to_move]
    df = df[columns]

df.to_csv(target_folder + csv_name_output, index=False, sep=';')
print('Transformed Csv generated correctly.')