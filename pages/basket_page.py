from selenium.webdriver.remote.webdriver import WebDriver

from pages.locators import BasketPageLocators
from pages.base_page import BasePage


class BasketPage(BasePage):

    def __init__(self, browser: WebDriver, url="http://selenium1py.pythonanywhere.com/en-gb/basket/"):
        super().__init__(browser, url)

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, f"invalid url [{self.browser.current_url}] in basket page"

    def get_product_list(self):
        self.browser.implicitly_wait(time_to_wait=2)
        list_of_items = self.browser.find_elements(*BasketPageLocators.ITEMS_LIST)
        self.browser.implicitly_wait(time_to_wait=self.default_implicitly_timeout)
        return list_of_items

    def should_be_empty(self):
        assert len(self.get_product_list()) == 0
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE)
        message_element = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE)
        print(message_element.text)
