from page_objects.MainPage import MainPage


def test_check_main_page(browser):
    MainPage(browser).check_elements()
