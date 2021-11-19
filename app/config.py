USER = 'root'    
PASSWORD = 'seznam123'
HOST = 'db'
PORT = '3306'
DB_TEST = 'MYSQLTEST'

QUERY_INSERT_CLICK = """INSERT INTO clicks (clickTimestamp, impressionId) VALUES (%s, %s) """
QUERY_INSERT_IMPRESSION = """INSERT INTO impressions (impressionTime, impressionId, adId, visitorHash) VALUES (%s, %s, %s, %s) """