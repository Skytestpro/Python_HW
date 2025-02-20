from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_form():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )
    from classes.main_page_class import MainPage
    main = MainPage(browser)
    main.get_page()
    main.find_and_send_elements()
    main.find_and_click_btn()

    from classes.result_page_class import ResultPage
    result = ResultPage(browser)

    for m in result.class_result_form():
        assert m == 'alert py-2 alert-success'

    assert result.class_zip_code() == 'alert py-2 alert-danger'
