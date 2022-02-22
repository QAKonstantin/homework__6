import pytest
import os
import random
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.0.100:8081")  #https://demo.opencart.com
    parser.addoption("--drivers", action="store", default=os.path.expanduser("C:/drivers1"))


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=drivers + "/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=drivers + "/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    else:
        driver = webdriver.Safari()

    driver.maximize_window()
    request.addfinalizer(driver.close)
    driver.get(url)
    driver.url = url
    return driver


@pytest.fixture
def create_user():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]
    email = ''
    phone = '+7'
    for i in range(10):
        email += random.sample(letters, 1)[0]
        phone += random.sample(numbers, 1)[0]
    email += '@gmail.com'
    return (email, phone)
