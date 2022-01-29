import os
from page_objects.RegisterPage import RegisterPage
from page_objects.elements.Header import Header


def test_register_form(browser, create_user):
    Header(browser).click_to_register()
    RegisterPage(browser).input_personal_details(firstname="Adam", lastname="Jeferson", email=create_user[0],
                                                 phone=create_user[1], password=os.getenv("user_password"))
    RegisterPage(browser).subscribe()
    RegisterPage(browser).open_agreement()
    RegisterPage(browser).close_agreement()
    RegisterPage(browser).rules_agree()
    RegisterPage(browser).submit_register()
    RegisterPage(browser).complete_registration()
