import bokeh
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

import sqlite3
import pandas as pd

def visualization():

    cnx = sqlite3.connect('../data/testdb.db')

    df = pd.read_sql_query("SELECT * FROM browser_frequency", cnx)

    fig = figure(plot_width=600, plot_height=600)
    users = df.last_name
    num_sites_visited = df.num_sites_visited
    
    output_file("bar_colormapped.html")


    source = ColumnDataSource(data=dict(users=users, num_sites_visted=num_sites_visited))

    p = figure(x_range=users, plot_height=350, toolbar_location=None, title="Browser Frequency")
    p.vbar(x='users', top='number of sites visited', width=0.9, source=source,
        line_color='white')

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 9
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    show(p)

if __name__ == '__main__':
    visualization()