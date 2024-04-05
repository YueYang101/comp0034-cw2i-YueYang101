import os
from selenium.webdriver.chrome.options import Options
from dash.testing.application_runners import import_app
import requests
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

# Add the current directory to the system path
os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
# get the current directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# create the path to the chromedriver
# The chromedriver version is 123.0.6312.105 version win 64 platform.
# The version of the chromedriver should be compatible with the version of the Chrome browser installed on your machine.
path_to_chromedriver = os.path.join(current_directory,'chromedriver.exe')  # add .exe for Windows

# create a new Chrome browser instance
s=Service(path_to_chromedriver)
driver = webdriver.Chrome(service=s)


def test_1_server_live(dash_duo):
    # Create the app
    app = import_app(app_file="PastaSales_dash")
    # Start the server with the app using the dash_duo fixture
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Get the url for the web app root
    url = dash_duo.driver.current_url

    # Requests is a python library and here is used to make a HTTP request to the sever url
    response = requests.get(url)

    # Finally, use the pytest assertion to check that the status code in the HTTP response is 200
    assert response.status_code == 200

    
def test_2_home_h1textequals(dash_duo):

    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading text should be "Paralympics Dashboard"
    """
    app = import_app(app_file="PastaSales_dash")
    dash_duo.start_server(app)

    # Wait for the H1 heading to be visible, timeout if this does not happen within 4 seconds
    dash_duo.wait_for_element("h1", timeout=4)

    # Find the text content of the H1 heading element
    h1_text = dash_duo.find_element("h1").text

    # Check the heading has the text we expect
    assert h1_text == "Pasta Sales Dashboard"


def test_3_bar_chart_exists(dash_duo):
    app = import_app(app_file="PastaSales_dash")
    dash_duo.start_server(app)

    # Wait for the specific element to be visible, timeout if this does not happen within 20 seconds
    dash_duo.wait_for_element("#bar", timeout=20)

    # Check if the element exists
    assert dash_duo.find_element("#bar") is not None


def test_4_line_chart_1_exists(dash_duo):
    app = import_app(app_file="PastaSales_dash")
    dash_duo.start_server(app)

    # Wait for the specific element to be visible, timeout if this does not happen within 20 seconds
    dash_duo.wait_for_element("#line_1", timeout=20)

    # Check if the element exists
    assert dash_duo.find_element("#line_1") is not None


def test_5_line_chart_2_exists(dash_duo):
    app = import_app(app_file="PastaSales_dash")
    dash_duo.start_server(app)

    # Wait for the specific element to be visible, timeout if this does not happen within 20 seconds
    dash_duo.wait_for_element("#line_2", timeout=20)

    # Check if the element exists
    assert dash_duo.find_element("#line_2") is not None


def test_6_button_click_changes_page(dash_duo):
    app = import_app(app_file="PastaSales_dash")
    dash_duo.start_server(app)

    # Wait for the button to be visible, timeout if this does not happen within 20 seconds
    dash_duo.wait_for_element("#checklist-input", timeout=20)

    # Click the button
    dash_duo.find_element("#checklist-input").click()

    # Wait for the new element to be visible, timeout if this does not happen within 20 seconds
    dash_duo.wait_for_element("#line_1", timeout=20)

    # Check if the new element exists
    assert dash_duo.find_element("#line_1") is not None


def test_7_dropdown_has_correct_options(dash_duo):
    app = import_app(app_file="PastaSales_dash")
    dash_duo.start_server(app)

    # Wait for the dropdown to be visible, timeout if this does not happen within 20 seconds
    dash_duo.wait_for_element("#type-dropdown_1", timeout=20)

    # Get the dropdown options
    dropdown = dash_duo.find_element("#type-dropdown_1")
    options = [option.text for option in dropdown.find_elements_by_tag_name("option") if option.text.strip() != ""]

    # Check if the options are correct
    assert options == ["Brand 1", "Brand 2", "Brand 3", "Brand 4"]
