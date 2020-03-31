import dash_html_components as html
from dash.dependencies import Input, Output

from common import make_sentiment_dashboard
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
    tsne_clicks = 0 if tsne_clicks is None else tsne_clicks
    sentiment_clicks = 0 if sentiment_clicks is None else sentiment_clicks
    print(input_value, tsne_clicks, sentiment_clicks)
    if tsne_clicks > sentiment_clicks:
        tsne_clicks = sentiment_clicks + 1
        return [html.Div('tsne!')]
    # default behaviour
    sentiment_clicks = tsne_clicks + 1
    return make_sentiment_dashboard(topic=input_value)
