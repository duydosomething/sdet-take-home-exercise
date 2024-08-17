# SDET Take Home Exercise

This repository contains tests related to testing the Google Finance page for the SDET Take Home Exercise. It utilizes pytest as the test runner and selenium for automating the Google Finance page. 

## Folder and File Descriptions
- **`tests/`**: 
  - **`test_google_finance.py`**: Contains test cases related to the Google Finance page.
- **`factories/`**: 
  - **`google_finance_factory.py`**: Contains test stock data used to compare with real-time stock data from Google Finnace.
- **`pages/`**: 
  - **`google_finance_page.py`**: Contains page object models for the Google Finance page.
- **`helper/`**: 
  - **`diff.py`**: Contains helper function to get diff for test cases 5 and 6
- **`.github/workflows/`**: 
  - **`manual_selection.yml`**: GH Action to manually run all tests or just tests 5 and 6
  - **`nightly_regression.yml`**: GH Action to have a nightly run at 5:00 AM UTC
- **`conftest.py`**: Contains fixtures that are commonly used between test cases
- **`pytest.ini`**: Contains config for marking tests 5 and 6

## Running Locally
To run locally do the following
```bash
git clone https://github.com/duydosomething/sdet-take-home-exercise.git && cd sdet-take-home-exercise

# Recommended to create a virtual env
python3 -m venv .
source ./bin/activate  # On Windows use `.\Scripts\activate`

# Install requirements
pip install -r requirements.txt

# Run tests (-s used for printouts)
pytest tests/ -s 

# Run only tests 5 and 6
pytest tests/ -s -m custom56

# Add "-v" for more verbose output
pytest tests/ -s -v

```



