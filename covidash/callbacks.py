import dash_html_components as html
from dash.dependencies import Input, Output

from covidash.common import make_sentiment_dashboard, make_tsne_plot
from covidash.figures import plotly_wordcloud
from covidash.data import load_embeddings, load_processed_dataset
from covidash.constants import WORDCLOUD_TITLE
from app import app

store = {}
store['current_button'] = 'tsne'


@app.callback(
    Output(component_id='right-dashboard', component_property='children'),
    [
        Input(component_id='topic_dropdown', component_property='value'),
        Input(component_id='tsne-button', component_property='n_clicks'),
        Input(component_id='sentiment-button', component_property='n_clicks')
    ]
)
def update_output_div(input_value, tsne_clicks, sentiment_clicks):
    """
    """
    tsne_clicks = 0 if tsne_clicks is None else tsne_clicks
    sentiment_clicks = 0 if sentiment_clicks is None else sentiment_clicks
    if tsne_clicks > sentiment_clicks:
        tsne_clicks = sentiment_clicks + 1
        return make_tsne_plot(topic=input_value)

    # default behaviour
    sentiment_clicks = tsne_clicks + 1
    return make_sentiment_dashboard(topic=input_value)


@app.callback(
    Output(component_id='wc_graph', component_property='figure'),
    [
        Input(component_id='topic_dropdown', component_property='value'),
    ]
)
def update_wordcloud(input_value):
    """
    """
    articles = load_processed_dataset(input_value)

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

    return fig
