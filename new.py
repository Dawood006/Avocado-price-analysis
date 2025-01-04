
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Load the data
file_path = "avocado.csv"
df = pd.read_csv(file_path)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Avocado Price Analysis"),
    
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in df['region'].unique()],
        value=df['region'].unique()[0]  # Default value
    ),
    
    dcc.Graph(id='price-graph'),
])

# Define callback to update graph based on selected region
@app.callback(
    Output('price-graph', 'figure'),
    Input('region-dropdown', 'value')
)
def update_graph(selected_region):
    filtered_data = df[df['region'] == selected_region]
    
    # Create a plotly figure
    figure = {
    'data': [{ 'x': filtered_data['Date'],'y': filtered_data['AveragePrice'], 'type': 'bar','name': selected_region}],
    'layout': {
        'title': f'Average Avocado Price in {selected_region}',
        'xaxis': {'title': 'Date'},
        'yaxis': {'title': 'Average Price'},
    }
}

    return figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
