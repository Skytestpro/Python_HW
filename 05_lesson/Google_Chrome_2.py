from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.get('http://uitestingplayground.com/dynamicid')

button = '//button[contains(@class,"btn btn-primary")]'
find_button = driver.find_element(By.XPATH, button)
find_button.click()

sleep(3)
