from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

add_element = '[onclick="addElement()"]'
search_add = driver.find_element(By.CSS_SELECTOR, add_element)

for add in range(5):
    search_add.click()

delete = '.added-manually'

print(len(driver.find_elements(By.CSS_SELECTOR, delete)))

sleep(2)
