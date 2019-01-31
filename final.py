# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 02:39:01 2019

@author: Admin
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader.data import DataReader
import time
from collections import deque
import plotly.graph_objs as go
import random
import pandas as pd
import webbrowser

#conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
#cursor = conn.cursor()
#cursor.execute('SELECT asin, stars FROM reviews');

#rows = cursor.fetchall()
#str(rows)[0:300]

#print(rows)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    html.H1(children='Bang & Olufsen'),

    html.Div(children='''
        Amazon B&O product rating
    '''),
             

    dcc.Dropdown(
        options=[
            {'label': 'A1', 'value': 'A1'},
            {'label': 'A6', 'value': 'A6'},
            {'label': 'A9', 'value': 'A9'},
            {'label': 'B17', 'value': 'B17'},
            {'label': 'E4', 'value': 'E4'},
            {'label': 'H3', 'value': 'H3'},
            {'label': 'H4', 'value': 'H4'},
            {'label': 'H5', 'value': 'H5'},
            {'label': 'H7', 'value': 'H7'},
            {'label': 'H8', 'value': 'H8'},
            {'label': 'H9', 'value': 'H9'},
            {'label': 'M5', 'value': 'M5'},
            {'label': 'P2', 'value': 'P2'},

        ],
        value=['A1'],
        multi=True
    ),
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 5, 4, 3], 'type': 'bar', 'name': ''},
            ],
            'layout': {
                'title': 'A1'
            }
        }
    )
])

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_css:
    app.scripts.append_script({'external_url': js})
    
url = 'http://127.0.0.1:8050/'
webbrowser.open_new(url)

if __name__ == '__main__':
    app.run_server(debug=True)