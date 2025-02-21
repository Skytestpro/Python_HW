from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from classes.auth_page_class import Authorization
from classes.products_page_class import Products
from classes.your_Information_class import Information


def test_shop():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    auth = Authorization(browser)
    auth.get_page()
    auth.log_pass()

    products = Products(browser)
    products.add_to_cart()
    products.go_to_cart()

    inf = Information(browser)
    inf.form('Имя', 'Фамилия', '543167')
    assert '$58.29' in inf.total()
