from datetime import datetime

def add_timestamp_column(df):
    current_local_timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    current_date = datetime.now().strftime("%Y-%m-%d")

    df['timestamp'] = str(current_date) + ' ' + str(current_local_timestamp)
