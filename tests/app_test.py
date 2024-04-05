import os
from selenium.webdriver.chrome.options import Options
from dash.testing.application_runners import import_app
import requests
import sys
from selenium import webdriver


from selenium.webdriver.chrome.service import Service
import os
os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
# get the current directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# create the path to the chromedriver
path_to_chromedriver = os.path.join(current_directory,'chromedriver.exe')  # add .exe for Windows

# create a new Chrome browser instance
s=Service(path_to_chromedriver)
driver = webdriver.Chrome(service=s)


def test_server_live(dash_duo):
    # Create the app
    app = import_app(app_file="PastaSales_dash")
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

    
"""
def test_home_h1textequals(dash_duo):

 
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading text should be "Paralympics Dashboard"

    app = import_app(app_file="src.PastaSales_dash")
    dash_duo.start_server(app)

    # Wait for the H1 heading to be visible, timeout if this does not happen within 4 seconds
    dash_duo.wait_for_element("h1", timeout=4)

    # Find the text content of the H1 heading element
    h1_text = dash_duo.find_element("h1").text

    # Check the heading has the text we expect
    assert h1_text == "Pasta Sales Dashboard"

"""