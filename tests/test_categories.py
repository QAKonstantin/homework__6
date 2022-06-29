from page_objects.CategoryPage import CategoryPage


def test_elements_laptops_category(browser):
    user = CategoryPage(browser)
    user.move_to_categories("Desktops", "Show All Desktops")
    user.check_elements_laptops()


def test_elements_phones_category(browser):
    user = CategoryPage(browser)
    user.move_to_categories("Phones & PDAs")
    user.check_elements_phones()


def test_elements_monitors_category(browser):
    user = CategoryPage(browser)
    user.move_to_categories("Components", "Monitors (2)")
    user.check_elements_monitors()
