from dash import Dash, Output, Input
import dash_bootstrap_components as dbc

from figures import line_chart_1, line_chart_2
from layout_elements import row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10
import plotly.graph_objects as go

external_stylesheets = [dbc.themes.BOOTSTRAP]
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Layout variables are in layout_elements.py

app.layout = dbc.Container([
    row_1,
    row_2,
    row_3,
    row_4,
    row_5,
    row_6,
    row_7,
    row_8,
    row_9,
    row_10,
])


@app.callback(
    Output(component_id='line_1', component_property='figure'),
    Input(component_id='checklist-input', component_property='value')
)
def update_line_chart_1(chart_types):
    if not chart_types:  # if the list is empty, return an empty figure
        return go.Figure()

    # Create a figure with a line for each chart_type in chart_types
    fig = go.Figure()
    for chart_type in chart_types:
        if chart_type in ["sum_stats", "brand_1", "brand_2", "brand_3", "brand_4"]:
            chart = line_chart_1(chart_type)
            for trace in chart.data:
                # Create a new trace with the data and name from the original trace
                new_trace = go.Scattergl(x=trace.x, y=trace.y, name=chart_type)
                fig.add_trace(new_trace)

    # Show the legend
    fig.update_layout(title_text='The sales data of all pasta brands over time')
    fig.update_layout(showlegend=True)

    return fig


@app.callback(
    Output(component_id='line_2', component_property='figure'),
    Input(component_id='type-dropdown_2', component_property='value')
)
def update_line_chart_2(chart_type):
    figure = line_chart_2(chart_type)
    figure.update_layout(showlegend=True)
    return figure


@app.callback(
    Output('type-dropdown_2', 'options'),
    Input('type-dropdown_1', 'value')
)
def update_dropdown_2(selected_value):
    if selected_value == 'brand_1':
        return [{"label": f"Product #{i}", "value": f"QTY_B1_{i}"} for i in range(1, 43)]
    if selected_value == 'brand_2':
        return [{"label": f"Product #{i}", "value": f"QTY_B2_{i}"} for i in range(1, 46)]
    if selected_value == 'brand_3':
        return [{"label": f"Product #{i}", "value": f"QTY_B3_{i}"} for i in range(1, 22)]
    if selected_value == 'brand_4':
        return [{"label": f"Product #{i}", "value": f"QTY_B4_{i}"} for i in range(1, 11)]


if __name__ == '__main__':
    app.run(debug=True, port=8050)
    # Runs on port 8050 by default, this just shows the parameter to use to change to another port if needed
