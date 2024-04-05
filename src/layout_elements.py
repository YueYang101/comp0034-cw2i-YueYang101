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

row_1 = html.Div(
    dbc.Row([
        dbc.Col([
            html.H1("Pasta Sales Dashboard", id='heading-one'), 
            html.P("Make smarter strategy with Pasta Sales Dashboard !!!", style={'font-size': '20px', 'word-wrap': 'break-word'}),  # adjust the font size and enable word wrapping
            html.P("Sales data is from a grocery store records the sales of different pasta brands everyday.", style={'font-size': '15px', 'word-wrap': 'break-word'}),  # adjust the font size and enable word wrapping
        ], width=8, align="center"),
        dbc.Col([
            html.Img(src='/assets/PastaPic2.jpg', 
                     style={'width': '100%', 'height': '100%', 'object-fit': 'cover', 'margin-left': '-200px','margin-top': '+30px'})  # adjust the image size and position
        ], width=4),
    ]),
)

row_2 = dbc.Row([
    dbc.Col([
        html.P("With the following checkboxex, you can select the brands you want to see on the line chart.",
               )
    ], width=12, className="text-center"),  # center the text horizontally
])

row_3 = dbc.Row([
    dbc.Col(children=[
        checklist,
    ], width={"size": 6}),
], align="start")

row_4 = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id="line", figure=line),
    ], width=12)])

row_5 = dbc.Row([
    dbc.Col([
        html.P("The bar chart shows the percentage of sales of each brand over time. You can select the time period you want to see by using the scroll bar.",
               )
    ], width=12, className="text-center"),  # center the text horizontally
])

row_6 = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id="bar", figure=bar),
    ], width=12),
], align="start")

row_7 = dbc.Row([
    dbc.Col([
        html.P("(The scroll bar is enabled and it takes some time to react to the changes in the data. Please be patient.)", 
               style={'margin-top': '-5px'})  # adjust the position of the text
    ], width=12, className="text-center"),  # center the text horizontally
])

row_8 = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id="map", figure=map)
    ], width=8, align="start"),
    dbc.Col(children=[
        html.Br(),
        html.Div(id='card'),
    ], width=4, align="start"),
])
