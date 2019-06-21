import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import json
from flask import jsonify

db_path = os.path.abspath('../data/testdb.db')
sql = " INSERT INTO frequent_browsers \
		SELECT personID, COUNT(personID) AS num_sites_visited FROM visits \
        LEFT JOIN sites ON sites.id=visits.siteId \
        LEFT JOIN people ON people.id=visits.personID \
        GROUP BY personID \
        ORDER BY num_sites_visited DESC \
        LIMIT 10 \
    "

def frequent_browsers(conn,sql):
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

def query_top_browsers():
	database = db_path
	print(database)

	conn = create_connection(database)
	print(conn)

	with conn:
		frequent_browsers(conn,sql)


if __name__ == '__main__':
	query_top_browsers()

