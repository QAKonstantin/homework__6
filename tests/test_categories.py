from page_objects.CategoryPage import CategoryPage


def test_elements_laptops_category(browser):
    CategoryPage(browser).move_to_categories("Desktops", "Show All Desktops")
    CategoryPage(browser).check_elements_laptops()


def test_elements_phones_category(browser):
    CategoryPage(browser).move_to_categories("Phones & PDAs")
    CategoryPage(browser).check_elements_phones()


def test_elements_monitors_category(browser):
    CategoryPage(browser).move_to_categories("Components", "Monitors (2)")
    CategoryPage(browser).check_elements_monitors()
