from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.maximize_window()
        self.browser.implicitly_wait(4)

    def get_page(self):
        self.browser.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    def find_and_send_elements(self):
        self.browser.find_element(By.CSS_SELECTOR,
                                  '[name="first-name"]').send_keys('Иван')
        self.browser.find_element(By.CSS_SELECTOR,
                                  '[name="last-name"]').send_keys('Петров')
        self.browser.find_element(By.CSS_SELECTOR,
                                  '[name="address"]').send_keys('Ленина, 55-3')
        self.browser.find_element(By.CSS_SELECTOR,
                                  '[name="e-mail"]').send_keys(
                                                            'test@skypro.com')
        self.browser.find_element(By.CSS_SELECTOR,
                                  '[name="phone"]').send_keys('+7985899998787')
        self.browser.find_element(By.CSS_SELECTOR,
                                  '[name="city"]').send_keys('Москва')
        self.browser.find_element(By.CSS_SELECTOR,
                                  '[name="country"]').send_keys('Россия')
        self.browser.find_element(By.CSS_SELECTOR,
                                  '[name="job-position"]').send_keys('QA')
        self.browser.find_element(By.CSS_SELECTOR,
                                  '[name="company"]').send_keys('SkyPro')

    def find_and_click_btn(self):
        self.browser.find_element(By.CSS_SELECTOR,
                                  '.btn-outline-primary').click()
