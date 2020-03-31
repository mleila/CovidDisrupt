import os

import dash
import dash_bootstrap_components as dbc

BASE = 'covidash'


def load_html(BASE):
    """
    Retrieve a list of HTML file paths.
    """
    directory = os.path.join(BASE, 'assets/html')
    files = [f for f in os.listdir(directory) if f.endswith('.html')]
    return [os.path.join(directory, f) for f in files]


def load_javascript(BASE):
    """
    Retrieve a list of javascript script paths.
    """
    directory = os.path.join(BASE, 'assets/js')
    files = [f for f in os.listdir(directory) if f.endswith('.js')]
    return [os.path.join(directory, f) for f in files]


def load_stylesheets(BASE):
    """
    Retrieve a list of CSS paths.
    """
    directory = os.path.join(BASE, 'assets/css')
    files = [f for f in os.listdir(directory) if f.endswith('.css')]
    return [os.path.join(directory, f) for f in files]


# order matters
external_stylesheets = [dbc.themes.BOOTSTRAP] + load_javascript(BASE)
external_scripts = load_stylesheets(BASE)

# init app object
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts)

# use custom html
html_files = load_html(BASE)
index_fp = [f for f in html_files if 'index.html' in f][0]
with open(index_fp, 'r') as file:
    app.index_string = file.read()

# init server object
server = app.server

# extra config
app.config.suppress_callback_exceptions = True
