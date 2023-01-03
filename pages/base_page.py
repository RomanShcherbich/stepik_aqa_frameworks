import math

from selenium.common import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from locators import BasePageLocators


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

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, by_locator: By, locator: str, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by_locator, locator)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, by_locator: By, locator: str, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((by_locator, locator)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK,
            implicitly_timeout=5
        ), "Login link is not presented"
