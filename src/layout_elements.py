import dash_bootstrap_components as dbc
from dash import html, dcc

from figures import line_chart_1, bar_gender, scatter_geo

# Figures
map = scatter_geo()
line = line_chart_1("sum_stats")
bar = bar_gender()

# Layout variables
dropdown_1 = dbc.Select(
    id="type-dropdown",
    options=[
        {"label": "Sales stats of all brands", "value": "sum_stats"},
        {"label": "Sales stats of brand 1", "value": "brand_1"},
        {"label": "Sales stats of brand 2", "value": "brand_2"},
        {"label": "Sales stats of brand 3", "value": "brand_3"},
        {"label": "Sales stats of brand 4", "value": "brand_4"},
    ],
    value="sum_stats"
)

chart_type_colors = {
    "sum_stats": "blue",
    "brand_1": "green",
    "brand_2": "red",
    "brand_3": "purple",
    "brand_4": "orange",
}

checklist = dbc.Checklist(
    options=[
        {"label": "All Brands", "value": "sum_stats"},
        {"label": "Brand 1", "value": "brand_1"},
        {"label": "Brand 2", "value": "brand_2"},
        {"label": "Brand 3", "value": "brand_3"},
        {"label": "Brand 4", "value": "brand_4"},
    ],
    value=["sum_stats"],
    id="checklist-input",
    inline=True,
)

row_one = html.Div(
    dbc.Row([
        dbc.Col([html.H1("Pasta Sales Dashboard", id='heading-one'), html.P(
            "Sales data for four brands of pasta from 2010 to 2020")
                 ], width=12, align="center"),
    ]),
)

row_two = dbc.Row([
    dbc.Col(children=[
        checklist,
    ], width={"size": 6}),
], align="start")

row_three = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id="line", figure=line),
    ], width=12)])

row_four = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id="bar", figure=bar),
    ], width=12),
], align="start")

row_five = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id="map", figure=map)
    ], width=8, align="start"),
    dbc.Col(children=[
        html.Br(),
        html.Div(id='card'),
    ], width=4, align="start"),
])
