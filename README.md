# comp0034-cw2i-YueYang101
## Setup

Follow these steps to set up the project:

```bash
# Create a virtual environment
# MacOS
python3 -m venv .venv
# Windows
py -m venv .venv

# Activate the virtual environment
# MacOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# Install the requirements
pip install -r requirements.txt

# Install the Web App
pip install -e .

# Before running the pytest
# Install selenium and pytest
pip install selenium pytest

# Put the right version of the chrome driver in the tests forlder

# Run the app with command
python src/PastaSales_dash.py

# Stop the app by pressing CTRL+C

# Run tests
pytest

# read the pdf file 'comp0034-coursework2' which includes the evidance of the tests results

# Github Link
https://github.com/YueYang101/comp0034-cw2i-YueYang101
