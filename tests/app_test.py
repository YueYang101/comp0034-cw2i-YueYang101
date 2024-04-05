import os
from selenium.webdriver.chrome.options import Options
from dash.testing.application_runners import import_app
import requests


def test_server_live(dash_duo):
    # Create the app
    app = import_app(app_file="src.PastaSales_dash")
    # Start the server with the app using the dash_duo fixture
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Get the url for the web app root
    # You can print this to see what it is e.g. print(f'The server url is {url}')
    url = dash_duo.driver.current_url

    # Requests is a python library and here is used to make a HTTP request to the sever url
    response = requests.get(url)

    # Finally, use the pytest assertion to check that the status code in the HTTP response is 200
    assert response.status_code == 200