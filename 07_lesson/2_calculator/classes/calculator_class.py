from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Calculator:

    def __init__(self, browser, time):
        self.browser = browser
        self.time = time
        self.browser.maximize_window()

    def get_page(self):
        self.browser.get(
            'https://bonigarcia.dev/selenium'
            '-webdriver-java/slow-calculator.html')

    def counter(self):
        counter = self.browser.find_element(By.CSS_SELECTOR, '#delay')
        counter.clear()
        counter.send_keys(self.time)

    def input(self):
        self.browser.find_element(
            By.XPATH, "//div[@class='keys']//span[text()='7']").click()
        self.browser.find_element(
            By.XPATH, "//div[@class='keys']//span[text()='+']").click()
        self.browser.find_element(
            By.XPATH, "//div[@class='keys']//span[text()='8']").click()
        self.browser.find_element(
            By.XPATH, "//div[@class='keys']//span[text()='=']").click()

        WebDriverWait(self.browser, self.time+2).until_not(
            EC.visibility_of(self.browser.find_element(
                By.CSS_SELECTOR, '#spinner')))

    def find_screen_txt(self):
        screen = self.browser.find_element(By.CSS_SELECTOR, '.screen').text
        return screen
