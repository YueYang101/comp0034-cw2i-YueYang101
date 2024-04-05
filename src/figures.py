import sqlite3
from pathlib import Path
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import html

# Path to the csv files
sales_data = Path(__file__).parent.parent.joinpath("PastaSalesData", "hierarchical_sales_data.csv")
sum_samles_data = Path(__file__).parent.parent.joinpath("PastaSalesData", "sum_stats.csv")


# Function to create a line chart
def line_chart_1(feature):
    """ Creates a line chart with data from paralympics_events.csv

    Data is displayed over time from 1960 onwards.
    The figure shows separate trends for the winter and summer events.

     Parameters
     feature: events, sports or participants

     Returns
     fig: Plotly Express line figure
     """

    # take the feature parameter from the function and check it is valid
    if feature not in ["sum_stats", "brand_1", "brand_2", "brand_3", "brand_4"]:
        raise ValueError(
            'Invalid value for "feature". Must be one of ["sum_stats", "brand_1", "brand_2", "brand_3", "brand_4"]')
    else:
        # Make sure it is lowercase to match the dataframe column names
        feature = feature.lower()

    # Read the data from pandas into a dataframe
    cols = ["date", "sum_stats", "brand_1", "brand_2", "brand_3", "brand_4"]
    line_chart_data = pd.read_csv(sum_samles_data, usecols=cols)

    fig = px.line(line_chart_data,
                  x="date",
                  y=feature,
                  title='The sales data of all pasta brands changed over time',
                  labels={'date': 'Date', feature: '', 'type': ''},
                  template="simple_white"
                  )
    return fig


# Function to create a line chart
def line_chart_2(product):
    base_cols = ["DATE"]
    brand_1_cols = [f"QTY_B1_{i}" for i in range(1, 43)]
    brand_2_cols = [f"QTY_B2_{i}" for i in range(1, 46)]
    brand_3_cols = [f"QTY_B3_{i}" for i in range(1, 22)]
    brand_4_cols = [f"QTY_B4_{i}" for i in range(1, 11)]
    cols = base_cols + brand_1_cols + brand_2_cols + brand_3_cols + brand_4_cols
    line_chart_2_data = pd.read_csv(sales_data, usecols=cols)
    fig = px.line(line_chart_2_data,
                  x="DATE",
                  y=product,
                  title='The sales data of all pasta brands changed over time',
                  labels={'date': 'Date', product: '', 'type': ''},
                  template="simple_white"
                  )
    fig.update_layout(showlegend=True)  # Add this line to show the legend
    return fig


# Function to create a bar chart
def bar_gender():
    
    cols = ["date", "sum_stats", "brand_1", "brand_2", "brand_3", "brand_4"]
    bar_chart_data = pd.read_csv(sum_samles_data, usecols=cols)
    # Add new columns that each contain the result of calculating the % of male and female participants
    bar_chart_data['Brand_1%'] = bar_chart_data['brand_1'] / bar_chart_data['sum_stats']
    bar_chart_data['Brand_2%'] = bar_chart_data['brand_2'] / bar_chart_data['sum_stats']
    bar_chart_data['Brand_3%'] = bar_chart_data['brand_3'] / bar_chart_data['sum_stats']
    bar_chart_data['Brand_4%'] = bar_chart_data['brand_4'] / bar_chart_data['sum_stats']
    
    fig = px.bar(bar_chart_data,
                 x='date',
                 y=['Brand_1%', 'Brand_2%', 'Brand_3%', 'Brand_4%'],
                 title='The ratio of sales of each pasta brand over time',
                 labels={'xlabel': '', 'value': '', 'variable': ''},
                 color_discrete_map={'Brand_1%': '#000080', 'Brand_2%': '#006400','Brand_3%': '#800000','Brand_4%': '#4B0082'},
                 template="simple_white"
                 )
    fig.update_xaxes(ticklen=0, rangeslider_visible=True, range=['2018-01-01', '2018-01-31'])
    return fig