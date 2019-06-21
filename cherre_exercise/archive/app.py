import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h2>Cherre programming exercise</h2>
	<p>
	Instructions
	Given the attached SQLiteDB (testdb.db), make a program in any language which does the following:<br/>
	1. find the ten people who have visited the most sites<br/>
	2. list these people in descending order of the number of sites they've visited in a table called FrequentBrowsers<br/>
	3. upload your solution, along with instructions on how to run it, to a public repository on GitHub<br/>
	4. email the repository link to Cherre

	<h3>Considerations</h3>
	We'd love to see what other cool stuff you can do!  

	Possible additions . . .<br/>
	- provide a Dockerfile to run the solution in container<br/>
	- provide an API to expose the results to the world<br/>
	- unit tests<br/>
	- on-board documentation.</p>'''


@app.route('/top_browsers', methods=['GET'])
def api_all():
    conn = sqlite3.connect('testdb.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    top_browsers = cur.execute('SELECT * FROM frequent_browsers;').fetchall()

    return jsonify(top_browsers)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/browser_frequency', methods=['GET'])
def api_filter():
    # query_parameters = request.args

    # id = query_parameters.get('id')
    # # rank = query_parameters.get('browser_frequency')

    # query = "SELECT * FROM books WHERE"
    # to_filter = []

    # if id:
    #     query += ' id=? AND'
    #     to_filter.append(id)
    # if published:
    #     query += ' visits=? AND'
    #     to_filter.append(published)
    # if author:
    #     query += ' last_name=? AND'
    #     to_filter.append(author)
    # if not (id or published or author):
    #     return page_not_found(404)

    # query = query[:-4] + ';'

    conn = sqlite3.connect('testdb.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    query = "SELECT * FROM browser_frequency"

    results = cur.execute(query).fetchall()

    return jsonify(results)

app.run()