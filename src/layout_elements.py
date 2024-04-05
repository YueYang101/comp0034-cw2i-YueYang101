import dash_bootstrap_components as dbc
from dash import html, dcc

from figures import line_chart_1, line_chart_2, bar_gender

# Figures Initial setup
line_1 = line_chart_1("sum_stats")
line_2 = line_chart_2("QTY_B1_1")
bar = bar_gender()

# Layout variables
dropdown_1 = dbc.Select(
    id="type-dropdown_1",
    options=[
        {"label": "Brand 1", "value": "brand_1"},
        {"label": "Brand 2", "value": "brand_2"},
        {"label": "Brand 3", "value": "brand_3"},
        {"label": "Brand 4", "value": "brand_4"},
    ],
    value="brand_1"
)


dropdown_2 = dbc.Select(
    id="type-dropdown_2",
        options=[
            {"label": "Product #1", "value": "QTY_B1_1"},
            {"label": "Product #2", "value": "QTY_B1_2"},
    ],
    value="QTY_B1_1"
)


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


# Rows Layout
row_1 = html.Div(
    dbc.Row([
        dbc.Col([
            html.H1("Pasta Sales Dashboard", id='heading-one'), 
            html.P("Make smarter strategy with Pasta Sales Dashboard !!!", style={'font-size': '20px', 'word-wrap': 'break-word'}),  # adjust the font size and enable word wrapping
            html.P("Sales data is from a grocery store records the sales of different pasta brands everyday.", style={'font-size': '15px', 'word-wrap': 'break-word'}),  # adjust the font size and enable word wrapping
        ], width=8, align="center"),
        dbc.Col([
            html.Img(src='/assets/PastaPic2.jpg', 
                     style={'width': '100%', 'height': '100%', 'object-fit': 'cover', 'margin-left': '-200px','margin-top': '+0px'})  # adjust the image size and position
        ], width=4),
    ]),
)


row_2 = dbc.Row([
    dbc.Col([
        html.P("Chart 1: With the following checkboxes, you can select the brands you want to see on the line chart.",
               style={'font-size': '25px'})  # adjust the font size
    ], width=12)
])


row_3 = dbc.Row([
    dbc.Col(children=[
        checklist,
    ], width={"size": 6}),
], align="start")


row_4 = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id="line_1", figure=line_1),
    ], width=12)])


row_5 = dbc.Row([
    dbc.Col([
        html.P("Chart 2: This bar chart shows the percentage of sales of each brand over time. You can select the time period you want to see by using the scroll bar.",
               style={'font-size': '25px'}
               )
    ], width=12, ),  # center the text horizontally
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
    dbc.Col([
        html.P("Chart 3: The following two dropdowns allow you to select the brand and the product you want to see on the line chart.",
               style={'font-size': '25px'}
        ),
        html.P("Select the brand from the left dropdown and the product from the right dropdown to see the sales data of the selected product of the selected brand over time.",
               style={'font-size': '20px'}
               )
    ], width=12, ),  # center the text horizontally
])


row_9 = dbc.Row([
    dbc.Col(children=[
        dropdown_1
    ], width=2),
    dbc.Col(children=[
        dropdown_2,
    ], width={"size": 2, "offset": 1}),  # Changed offset from 4 to 1
], align="start")


row_10 = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id="line_2", figure=line_2),
    ], width=12),
], align="start")