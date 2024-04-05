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

# Run the app with command
flask --app paralympics run --debug

# Stop the app by pressing CTRL+C

# Check if the instance folder created which contains paralympics.sqlite

# Using following input to access data
# /total_sales_each_brand/<specific_date>
# /promo_record_each_brand/<specific_date>
# Date format example: 2024-01-02


# read the pdf file 'comp0034-coursework1'