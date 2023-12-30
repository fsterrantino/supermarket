products_table_columns = '''
    sku INTEGER PRIMARY KEY,
    brand VARCHAR(100),
    description VARCHAR(200),
    timestamp TIMESTAMP
'''

prices_table_columns = '''
    sku INTEGER,
    final_price FLOAT,
    original_price FLOAT,
    discount VARCHAR(50),
    regular_price FLOAT,
    regular_price_measure VARCHAR(10),
    regular_price_un VARCHAR(10),
    timestamp TIMESTAMP,
    PRIMARY KEY (sku, timestamp)
'''