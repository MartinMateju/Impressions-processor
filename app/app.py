from flask import Flask
import config as CONFIG
# import json

from utils import test_db_connection, load_csv, db_import, run_io_tasks_in_parallel


app = Flask(__name__)


@app.route('/')
def hello():
    data_impr = load_csv('impressions.csv')
    data_clicks = load_csv('clicks.csv')
    run_io_tasks_in_parallel([
        lambda: db_import(data_impr['rows'], 'impressions', CONFIG.QUERY_INSERT_IMPRESSION),
        lambda: db_import(data_clicks['rows'], 'clicks', CONFIG.QUERY_INSERT_CLICK),
    ])
    return 'Done'
    # return test_db_connection()

if __name__ == '__main__':
    app.run(host='0.0.0.0')