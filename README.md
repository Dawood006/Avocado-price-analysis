# Avocado Price Analysis Dashboard

This project is a simple web-based dashboard built using Dash, a Python framework for building analytical web applications. The dashboard visualizes the average price of avocados over time for different regions based on the dataset provided in `avocado.csv`.

## Features

- **Interactive Dropdown**: Select a region from the dropdown menu to view the average avocado prices for that region.
- **Bar Chart Visualization**: Displays the average avocado prices over time in a bar chart format.
- **Dynamic Updates**: The chart updates automatically based on the selected region.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Dash
- Pandas
- Plotly

You can install the required packages using pip:

```bash
pip install dash pandas plotly
```

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Dawood006/avocado-price-analysis.git
   cd avocado-price-analysis
   ```

2. **Place the dataset**:

   Ensure that the `avocado.csv` file is placed in the same directory as the `new.py` script.

3. **Run the application**:

   ```bash
   python new.py
   ```

4. **Access the dashboard**:

   Open your web browser and navigate to `http://127.0.0.1:8050/` to view the dashboard.

## Project Structure

- `new.py`: The main script that initializes and runs the Dash application.
- `avocado.csv`: The dataset containing avocado price information.

## Code Overview

### Data Loading

The dataset is loaded using Pandas:

```python
import pandas as pd

file_path = "avocado.csv"
df = pd.read_csv(file_path)
```

### Dash Application

The Dash app is initialized and the layout is defined:

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Avocado Price Analysis"),
    
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in df['region'].unique()],
        value=df['region'].unique()[0]  # Default value
    ),
    
    dcc.Graph(id='price-graph'),
])
```

### Callback Function

A callback function is defined to update the graph based on the selected region:

```python
@app.callback(
    Output('price-graph', 'figure'),
    Input('region-dropdown', 'value')
)
def update_graph(selected_region):
    filtered_data = df[df['region'] == selected_region]
    
    figure = {
        'data': [{ 'x': filtered_data['Date'],'y': filtered_data['AveragePrice'], 'type': 'bar','name': selected_region}],
        'layout': {
            'title': f'Average Avocado Price in {selected_region}',
            'xaxis': {'title': 'Date'},
            'yaxis': {'title': 'Average Price'},
        }
    }

    return figure
```

### Running the App

The app is run with debug mode enabled:

```python
if __name__ == '__main__':
    app.run_server(debug=True)
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset: [avocado.csv](https://www.kaggle.com/neuromusic/avocado-prices)
- Dash: [Dash Documentation](https://dash.plotly.com/)

---

This README provides an overview of the Avocado Price Analysis Dashboard. For more details, refer to the code and comments in `new.py`.
![image](https://github.com/user-attachments/assets/7571df8e-e2f5-4b15-962f-cbdd3ac3ecd9)

