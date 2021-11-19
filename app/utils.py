import mysql.connector
import json
import csv
import config as CONFIG

from concurrent.futures import ThreadPoolExecutor

def get_db_connecetion():
    """Returns db-connection"""
    try:
        config = {
            'user': CONFIG.USER,
            'password': CONFIG.PASSWORD,
            'host': CONFIG.HOST,
            'port': CONFIG.PORT,
            'database': CONFIG.DB_TEST
        }
        connection = mysql.connector.connect(**config)
    except Exception as exc:
        print('DB-connection failed due to err: %s', repr(exc))
    return connection


def run_io_tasks_in_parallel(tasks):
    """Execute tasks in parallel"""
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()


def test_db_connection():
    """Validates db connection"""
    status = 'Failed'
    try:
        connection = get_db_connecetion()
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
    except Exception as exc:
        print("Error while connecting to MySQL. err: %s", repr(exc))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            status = 'Success'

    return status


def load_csv(path):
    """Load csv data"""
    rows = []
    with open(path, 'r') as file:
        csvreader = csv.reader(file)
        headers = next(csvreader)
        for row in csvreader:
            rows.append(tuple(row))
    file.close()
    return {'rows': rows, 'headers': headers}


def db_import(data, table, query):
    """Imports data to mySql-db"""
    try:
        print('sql query: %s', query)
        connection = get_db_connecetion()
        cursor = connection.cursor()
        cursor.executemany(query, data)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into %s table", table)
    except Exception as exc:
        print("Failed to insert record into MySQL table %s, err %s", table, repr(exc))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")