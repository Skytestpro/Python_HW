from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://the-internet.herokuapp.com/entry_ad')

sleep(3)

close = 'div.modal-footer > p'
find_close = driver.find_element(By.CSS_SELECTOR, close)
find_close.click()

sleep(2)
driver.quit()
