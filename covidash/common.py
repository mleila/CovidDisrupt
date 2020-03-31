"""
This module hosts common components
"""
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq

from covidash.constants import *
from covidash.figures import plotly_wordcloud
from covidash.data import (
    load_processed_dataset,
    load_topic_comprehend,
    load_topics,
    general_sentiment)


def make_header():
    """
    Universal header.
    """
    div = html.Div(BANNER_TITLE, className='banner')
    return dbc.Row(children=[div], className='main-header')


def make_page():
    """
    Main page.
    """
    main_div = html.Div(id='page', className='page')
    row = dbc.Row(main_div, className='main-page')
    return dbc.Container(row, style={"height": "100vh"})


def make_control_panel():
    """
    """
    topics = load_topics()

    dropdown_label = html.Div(
        'Choose a Topic',
        className='dropdown-label')
    dropdown = dcc.Dropdown(
        id='topic_dropdown',
        className='dropdown',
        options=[{'label': t, 'value': t} for t in topics],
        value=DEFAULT_TOPIC)

    buttons = [
        html.Button('TSNE', id='tsne-button', className='button'),
        html.Button('Sentiment', id='sentiment-button', className='button'),
    ]

    return dbc.Container([
        dbc.Row([
            dbc.Col(dbc.Row([
                dropdown_label,
                dropdown
            ]), width=12)
        ]),
        dbc.Row([
            dbc.Col(buttons, width=12)
        ])
    ], className='control-panel')


def make_wordcloud_graph(id: str, topic: str):
    """
    Create a wordcloud graph based on a topic.
    """
    articles = load_processed_dataset(topic)

    # combine articles
    text = ' '.join(articles)

    # create plotly figure
    fig = plotly_wordcloud(text, max_font_size=20)

    # style figure
    fig.update_layout(
        title={
            'text': WORDCLOUD_TITLE,
            'y': 0.9,
            'x': 0.25,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                "color": "white"
            }
        },
        margin={
            't': 50,
            'b': 0,
            'r': 0,
            'l': 0
        },
        font_size=10,
        width=450,
        height=350,
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    # retrun graph
    return dcc.Graph(id=id, figure=fig)


def make_sentiment_gauge(label, value):
    return daq.Gauge(
        label=label,
        min=0,
        max=1,
        value=value,
        color={"gradient": True, "ranges": {
            "green": [0, 0.6], "yellow": [0.6, 0.8], "red": [0.8, 1]}},
        size=120)


def make_sentiment_dashboard(topic):
    """
    Make a sentiment analysis dashboard for a given topic.
    """
    data = load_topic_comprehend(topic)
    sent_res = general_sentiment(data)
    gauge1 = make_sentiment_gauge(
        'Positive Sentiment', sent_res['mean_pos_sent'])
    gauge2 = make_sentiment_gauge(
        'Negative Sentiment', sent_res['mean_neg_sent'])
    gauge3 = make_sentiment_gauge(
        'Neutral Sentiment', sent_res['mean_neutral_sent'])
    gauge4 = make_sentiment_gauge(
        'Mixed Sentiment', sent_res['mean_mixed_sent'])
    return dbc.Container([
        dbc.Row([
            dbc.Col(gauge1),
            dbc.Col([gauge2])
        ]),
        dbc.Row([
            dbc.Col([gauge3]),
            dbc.Col([gauge4])
        ]),
    ])
