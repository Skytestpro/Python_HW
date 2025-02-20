from selenium.webdriver.common.by import By


class Information:

    def __init__(self, browser):
        self.browser = browser

    def form(self, first_name, last_name, index):
        self.browser.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self.browser.find_element(
            By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.browser.find_element(
            By.CSS_SELECTOR, '#postal-code').send_keys(index)
        self.browser.find_element(By.CSS_SELECTOR, '#continue').click()

    def total(self):
        total = self.browser.find_element(
            By.CSS_SELECTOR, '[data-test="total-label"]').text
        return total
