import pytest

from helper.diff import get_diff


def test_page_load(google_finance_page):
    title = google_finance_page.get_page_title()
    # Assert the page title is correct
    assert (
        title
        == "Google Finance - Stock Market Prices, Real-time Quotes & Business News"
    )


def test_smart_watchlist(current_watchlist):
    watchlist_items = current_watchlist
    # Assert that the watchlist is non empty
    assert len(watchlist_items) > 0


def test_compare_stocks(current_watchlist, test_stocks):
    # Assert the lists we get back are not non empty
    assert len(current_watchlist) > 0
    assert len(test_stocks) > 0
    print(f"\nCurrent Stock Watchlist: {current_watchlist}")
    print(f"Test Data Stocks: {test_stocks}")
    # Assert that both do not completely equal each other
    assert current_watchlist != test_stocks


@pytest.mark.custom56
def test_print_diff_one(current_watchlist, test_stocks):
    diff = get_diff(current_watchlist, test_stocks)
    # Assert diff is >= 2 because there will be at least 2 watchlist stocks not in
    # test stocks
    assert len(diff) >= 2
    print("\nStocks in current watchlist, but not in test data:")
    print(f"{diff}")


@pytest.mark.custom56
def test_print_diff_two(current_watchlist, test_stocks):
    diff = get_diff(test_stocks, current_watchlist)
    # Assert diff is >= 0 because possibilty that all test stocks can be in
    # the watchlist
    assert len(diff) >= 0
    print("\nStocks in test data, but not in current watchlist:")
    print(f"{diff}")
