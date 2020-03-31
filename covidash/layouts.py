import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from covidash.constants import *
from covidash.common import (
    make_header,
    make_page,
    make_wordcloud_graph,
    make_sentiment_dashboard,
    make_control_panel)


def get_frame_layout():
    """
    Create basic page structure.
    """
    # link (this is required for url navigation)
    location = dcc.Location(id='url', refresh=True)

    # header
    header = make_header()

    # main page
    page = make_page()

    return html.Div([location, header, page])


def get_main_layout():
    """
    Load default layout
    """

    project_description = html.Div([
        html.H2(PROJ_TITLE),
        html.P(PROJ_DESC)])

    default_wc_graph = make_wordcloud_graph(id='wc_graph', topic=DEFAULT_TOPIC)

    # general sentiment dashboard
    sentiment_dashboard = make_sentiment_dashboard(topic=DEFAULT_TOPIC)

    # make control panel
    control_panel = make_control_panel()

    components = dbc.Container([
        dbc.Row([
            dbc.Col([
                project_description, default_wc_graph
            ], width=6),
            dbc.Col([
                control_panel,
                html.Div(id='right-dashboard')
            ], width=6)
        ])
    ])
    return components
