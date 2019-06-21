import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import json
from flask import jsonify


def table_lengths():
    cnx = sqlite3.connect('../data/testdb.db')
    table_names = list(pd.read_sql_query("SELECT name FROM sqlite_master WHERE type = 'table'", cnx)['name'])
    table_names.remove('sqlite_sequence')
    table_length_dict = {}
    for name in table_names:
        table_length = pd.read_sql_query("SELECT COUNT(*) AS 'table_length' FROM "+str(name)+"", cnx)
        table_length_dict[name] = json.loads(str(table_length.iloc[0,0]))
    db_page_size = pd.read_sql_query("PRAGMA PAGE_SIZE", cnx).iloc[0,0]
    db_page_count = pd.read_sql_query("PRAGMA PAGE_COUNT", cnx).iloc[0,0]
    db_bytes = {"Database size (bytes)": json.loads(str(db_page_size * db_page_count))}
    return jsonify(table_length_dict, db_bytes)

def table_info():
    cnx = sqlite3.connect('../data/testdb.db')
    table_names = list(pd.read_sql_query("SELECT name FROM sqlite_master WHERE type = 'table'", cnx)['name'])
    table_names.remove('sqlite_sequence')
    table_info_dict = {}
    for name in table_names:
        table_column_info = pd.read_sql("PRAGMA table_info("+str(name)+")", cnx).to_json()
        table_info_dict[name] = json.loads(table_column_info)
    return jsonify(table_info_dict)
			