from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, browser):
        self.browser = browser

    def class_zip_code(self):
        zip_class = self.browser.find_element(
            By.CSS_SELECTOR, '#zip-code').get_attribute('class')
        return zip_class

    def class_result_form(self):
        result_form = [
            self.browser.find_element(
                By.CSS_SELECTOR, '#first-name').get_attribute('class'),
            self.browser.find_element(
                By.CSS_SELECTOR, '#last-name').get_attribute('class'),
            self.browser.find_element(
                By.CSS_SELECTOR, '#address').get_attribute('class'),
            self.browser.find_element(
                By.CSS_SELECTOR, '#city').get_attribute('class'),
            self.browser.find_element(
                By.CSS_SELECTOR, '#country').get_attribute('class'),
            self.browser.find_element(
                By.CSS_SELECTOR, '#e-mail').get_attribute('class'),
            self.browser.find_element(
                By.CSS_SELECTOR, '#phone').get_attribute('class'),
            self.browser.find_element(
                By.CSS_SELECTOR, '#job-position').get_attribute('class'),
            self.browser.find_element(
                By.CSS_SELECTOR, '#company').get_attribute('class')
        ]
        return result_form
