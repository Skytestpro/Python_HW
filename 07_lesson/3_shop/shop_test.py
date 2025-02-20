from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_shop():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    from classes.auth_page_class import Authorization
    auth = Authorization(browser)
    auth.get_page()
    auth.log_pass()

    from classes.products_page_class import Products
    products = Products(browser)
    products.add_to_cart()
    products.go_to_cart()

    from classes.your_Information_class import Information
    inf = Information(browser)
    inf.form('Имя', 'Фамилия', '543167')
    assert '$58.29' in inf.total()
