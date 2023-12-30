def check_for_duplicated_products(df):

    if df['sku'].duplicated().any():
        raise ValueError(f"Column 'sku' contains duplicated values. Please, check dataframe before inserting.")

    return df