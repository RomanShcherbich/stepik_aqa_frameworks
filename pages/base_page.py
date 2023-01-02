from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, browser: WebDriver, url, implicitly_timeout=10):
        self.browser = browser
        self.url = url
        self.default_implicitly_timeout = implicitly_timeout
        self.browser.implicitly_wait(time_to_wait=self.default_implicitly_timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by_locator: By, locator: str, implicitly_timeout: float = None):
        if implicitly_timeout:
            self.browser.implicitly_wait(time_to_wait=implicitly_timeout)
        result = True
        try:
            self.browser.find_element(by_locator, locator)
        except NoSuchElementException:
            result = False
        if implicitly_timeout:
            self.browser.implicitly_wait(time_to_wait=self.default_implicitly_timeout)
        return result
