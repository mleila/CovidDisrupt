"""
Entry point to the Dash application
"""
from dash.dependencies import Input, Output

from app import app
import layouts as lyt
import callbacks

# get frame layout
app.layout = lyt.get_frame_layout()

# define the main router as a callback
@app.callback(Output('page', 'children'),
              [Input('url', 'pathname')])
def router_page(pathname):
    """
    This is the main router for the single page Dash App.
    """
    if pathname in [None, '/']:
        return lyt.get_main_layout()
    return '404'


if __name__ == "__main__":
    app.run_server(debug=True)
