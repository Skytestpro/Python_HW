from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get('http://the-internet.herokuapp.com/login')
sleep(1)

username = driver.find_element(By.CSS_SELECTOR, 'input#username')
username.send_keys('tomsmith')
sleep(1)

password = driver.find_element(By.CSS_SELECTOR, 'input#password')
password.send_keys('SuperSecretPassword!')
sleep(1)

login = driver.find_element(By.CSS_SELECTOR, '.fa-sign-in')
login.click()

sleep(1)
driver.quit()
