from selenium.webdriver.common.by import By


class GoogleFinancePage:

    def __init__(self, driver):
        self.driver = driver
        self.smart_watchlist = (
            By.XPATH,
            '//section[@aria-labelledby="smart-watchlist-title"]/ul',
        )

    def get_page_title(self):
        return self.driver.title

    def get_smart_watchlist(self):
        smart_watchlist = self.driver.find_element(*self.smart_watchlist)
        items = smart_watchlist.find_elements(By.TAG_NAME, "li")
        watchlist_items = [item.text.split()[0] for item in items]
        return watchlist_items
