from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from classes.calculator_class import Calculator


def test_calculator():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )
    calc = Calculator(browser, 45)
    calc.get_page()
    calc.counter()
    calc.input()
    assert '15' in calc.find_screen_txt()
