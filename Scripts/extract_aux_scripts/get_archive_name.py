import datetime
import os

def get_archive_name():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d.%m.%Y")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    target_folder = os.path.join(parent_dir, 'Archives')
    csv_name = '/Products - ' + formatted_date + '.csv'

    return target_folder + csv_name