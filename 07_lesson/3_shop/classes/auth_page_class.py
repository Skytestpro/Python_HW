from selenium.webdriver.common.by import By


class Authorization:

    def __init__(self, browser):
        self.browser = browser
        self.browser.maximize_window()

    def get_page(self):
        self.browser.get('https://www.saucedemo.com/')
        self.browser.implicitly_wait(4)

    def log_pass(self):
        self.browser.find_element(
            By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        self.browser.find_element(
            By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self.browser.find_element(By.CSS_SELECTOR, '#login-button').click()
