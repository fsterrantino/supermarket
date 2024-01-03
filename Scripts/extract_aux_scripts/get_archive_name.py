import datetime
import os

def get_archive_name():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%d.%m.%Y")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_dir = os.path.dirname(current_dir)
    project_dir = os.path.dirname(scripts_dir)
    target_folder = os.path.join(project_dir, 'Archives')
    csv_name = '/Products - ' + formatted_date + '.csv'

    return target_folder, csv_name