import pytest
from selenium import webdriver

from factories.google_finance_factory import GoogleFinanceFactory
from pages.google_finance_page import GoogleFinancePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/finance/")
    yield driver
    driver.close()


@pytest.fixture
def google_finance_page(driver):
    google_finance_page = GoogleFinancePage(driver)
    return google_finance_page


@pytest.fixture
def test_stocks():
    google_finance_factory = GoogleFinanceFactory()
    return google_finance_factory.test_stocks


@pytest.fixture
def current_watchlist(driver):
    google_finance_page = GoogleFinancePage(driver)
    current_watchlist = google_finance_page.get_smart_watchlist()
    return current_watchlist
