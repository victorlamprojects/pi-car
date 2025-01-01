import os
import pandas as pd
from flask import current_app as app
import tempfile

TEMP_DIR = tempfile.gettempdir()
FILE = "battery_info.data"

def get_battery_info():
    data = {} 
    try:
        data = pd.read_csv(os.path.join(TEMP_DIR, FILE), index_col=False)
        data = data.to_dict('records')[0]
    except Exception as e:
        app.logger.error(str(e))
    return data
