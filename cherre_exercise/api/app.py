#!/usr/bin/env python3

from flask import Flask, request, jsonify, render_template, redirect, url_for
from redis import Redis
import sqlite3
import sys
import os
import pandas as pd
import json
from db_queries import table_lengths, table_info
from query import query_top_browsers
from clear import clear_db
# from chart import visualization

app = Flask(__name__)
app.config["DEBUG"] = True
# redis = Redis(host='redis', port=6379)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/bokeh',methods=['GET'])
def bokeh():
    visualization()


@app.route('/', methods=['GET'])
def home():
    # redis.incr('hits')
    # return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')
    return render_template('home.html',name='home')

@app.route('/top_browsers', methods=['GET'])
def api_all():
    conn = sqlite3.connect('../data/testdb.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    try:
        top_browsers = cur.execute('SELECT * FROM frequent_browsers;').fetchall()
    except:
        return None
    return jsonify(top_browsers)


@app.route('/clear_database',methods=['GET'])
def clear_database():
    clear_db()
    return render_template('/clear_success.html')


@app.route('/query_top_browsers',methods=['GET'])
def query():
    query_top_browsers()
    return render_template('/query_success.html')
    

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/table_column_info', methods=['GET'])
def table_info_query():
    return table_info()

@app.route('/table_lengths', methods=['GET'])
def table_length_query():
    return table_lengths()

@app.route('/browser_frequency', methods=['GET'])
def api_top_browser_JSON():

    conn = sqlite3.connect('../data/testdb.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    query = "SELECT * FROM browser_frequency"

    results = cur.execute(query).fetchall()

    return jsonify(results)


if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 