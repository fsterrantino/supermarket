import pandas as pd
from datetime import datetime
import os
from transform_aux_scripts.add_timestamp_column import add_timestamp_column

current_date = datetime.now()
formatted_date = current_date.strftime("%d.%m.%Y")

csv_name_input = '/Products - ' + formatted_date + '.csv'

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
target_folder = os.path.join(parent_dir, 'Archives')

df = pd.read_csv(target_folder + csv_name_input, sep=';')

df = df.drop('id', axis=1)

df['brand'] = df['brand'].str.replace('SIN MARCA', 'NO BRAND')
df['brand'] = df['brand'].fillna('NO BRAND')

df['original_price'] = df['original_price'].fillna(df['final_price'])
df['discount'] = df['discount'].fillna('0%')

# Fromatting string like: 'Precio regular: $3.950 x kg.'

df['regular_price'] = df['regular_price'].str.replace('Precio regular: $', '')
# 3.950 x kg.

expanded_precio_regular = df['regular_price'].str.split(' ', expand = True)
# [3.950, x, kg.]

df['regular_price'] = expanded_precio_regular[0]
# 3.950

expanded_precio_regular[2] = expanded_precio_regular[2].str.replace('.', '')
expanded_precio_regular[3] = expanded_precio_regular[3].str.replace('.', '')
# kg

# [3.950, x, kg, None] or [1.200, x, 100, gr]
def format_regular_price_measure_and_unit(row):
    if row[3]:
        return row[2], row[3]
    else:
        return 1, row[2]

df[['regular_price_measure', 'regular_price_un']] = expanded_precio_regular.apply(lambda row: pd.Series(format_regular_price_measure_and_unit(row)), axis=1)

def format_price_columns(column):
    column = column.str.replace('$', '')
    column = column.str.replace('.', '')
    column = column.str.replace(',', '.')

    column = pd.to_numeric(column, errors='coerce')
    return column

df['final_price'] = format_price_columns(df['final_price'])
df['original_price'] = format_price_columns(df['original_price'])
df['regular_price'] = format_price_columns(df['regular_price'])

csv_name_output = '/Transformed_products - ' + formatted_date + '.csv'

add_timestamp_column(df)

column_to_move = 'sku'
if column_to_move in df.columns:
    columns = [column_to_move] + [col for col in df if col != column_to_move]
    df = df[columns]

df.to_csv(target_folder + csv_name_output, index=False, sep=';')
print('Transformed Csv generated correctly.')