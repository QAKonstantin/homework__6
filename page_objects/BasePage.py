from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    FOOTER = (By.ID, "footer")
    BREAD_CRUMBS = (By.CSS_SELECTOR, "[class='breadcrumb']")
    SEARCH = (By.CSS_SELECTOR, "[id='search']")
    ITEMS = (By.CSS_SELECTOR, "[id='cart-total']")
    LOGO = (By.ID, "logo")
    CONTENT = (By.ID, "content")
    TOP = (By.CSS_SELECTOR, "[id='top']")

    def __init__(self, browser):
        self.browser = browser

    def _input_text(self, web_element, text):
        web_element.clear()
        web_element.send_keys(text)

    def _search_element(self, locator: tuple, timeout=2):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _search_link_text(self, link_text, timeout=2):
        try:
            return WebDriverWait(self.browser, timeout) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _wait_text_element(self, locator, goal, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, goal))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _click_link(self, link_text):
        self._click((By.LINK_TEXT, link_text))
        return self

    def _click(self, locator: tuple):
        self.element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(self.element).click().perform()
        return self.element

    def _element(self, locator: tuple):
        return self._search_element(locator)

    def open(self, path):
        self.browser.get(self.browser.current_url + path)
        return self
