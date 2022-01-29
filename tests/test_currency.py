from page_objects.elements.Header import Header


def test_change_currency(browser):
    Header(browser).change_currency("EUR")
    Header(browser).change_currency("GBP")
    Header(browser).change_currency("USD")
