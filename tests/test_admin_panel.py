from page_objects.AdminPanelPage import AdminPanel
import os


def test_add_delete_product(browser):
    AdminPanel(browser).login_with("user", os.getenv("admin_password"))
    AdminPanel(browser).add_product(product_name="Test_name", model="Test_model", tag="test")
    AdminPanel(browser).delete_product(product_name="Test_name")


def test_check_page_admin(browser):
    AdminPanel(browser).check_elements()
