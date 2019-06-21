import sqlite3
from sqlite3 import Error
import os

db_path = os.path.abspath('../data/testdb.db')
sql = f'''DELETE FROM frequent_browsers'''

def clear_frequent_browsers(conn,sql):
    cur = conn.cursor()
    cur.execute(sql)

def create_connection(database):
	try:
		conn = sqlite3.connect(database)
		return conn 
		print("Connection Successful")
	except Error as e:
		print("Connection Error "+str(e))
	return None

def clear_db():
	database = db_path
	print(database)

	conn = create_connection(database)
	print(conn)

	with conn:
		clear_frequent_browsers(conn,sql)

if __name__ == '__main__':
	clear_db()

