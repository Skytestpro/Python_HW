import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.test_2
def test_calc():
    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    driver.maximize_window()
    input = driver.find_element(By.CSS_SELECTOR, '#delay')
    input.clear()
    input.send_keys('45')

    driver.find_element(By.XPATH,
                        "//div[@class='keys']//span[text()='7']").click()
    driver.find_element(By.XPATH,
                        "//div[@class='keys']//span[text()='+']").click()
    driver.find_element(By.XPATH,
                        "//div[@class='keys']//span[text()='8']").click()
    driver.find_element(By.XPATH,
                        "//div[@class='keys']//span[text()='=']").click()

    WebDriverWait(driver, 45).until_not(
        EC.visibility_of(driver.find_element(By.CSS_SELECTOR, '#spinner'))
    )

    assert '15' in driver.find_element(By.CSS_SELECTOR, '.screen').text
