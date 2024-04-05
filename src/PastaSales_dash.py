from dash import Dash, Output, Input
import dash_bootstrap_components as dbc

from figures import line_chart_1, bar_gender_faceted, create_card
from layout_elements import row_one, row_two, row_three, row_four, row_five

import plotly.graph_objects as go

external_stylesheets = [dbc.themes.BOOTSTRAP]
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Layout variables are in layout_elements.py

app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    row_four,
    row_five
])


@app.callback(
    Output(component_id='line', component_property='figure'),
    Input(component_id='checklist-input', component_property='value')
)
def update_line_chart(chart_types):
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
    fig.update_layout(title_text='The sales data of all pasta brands changed over time')
    fig.update_layout(showlegend=True)

    return fig

'''
@app.callback(
    Output(component_id='bar', component_property='figure'),
    Input(component_id='checklist-input', component_property='value')
)
def update_line_chart(event_type):
    figure = bar_gender_faceted(event_type)
    return figure
'''


@app.callback(
    Output('card', 'children'),
    Input('map', 'hoverData'),
)
def display_card(hover_data):
    if hover_data is not None:
        event_id = hover_data['points'][0]['customdata'][0]
        if event_id is not None:
            return create_card(event_id)


if __name__ == '__main__':
    app.run(debug=True, port=8050)
    # Runs on port 8050 by default, this just shows the parameter to use to change to another port if needed
