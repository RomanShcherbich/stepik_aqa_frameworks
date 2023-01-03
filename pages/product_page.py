from selenium.webdriver.remote.webdriver import WebDriver

from pages.locators import GoodPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, browser: WebDriver, url):
        super().__init__(browser, url)
        self.name = "not loaded"
        self.price = "not loaded"

    def load_goods_data(self):
        self.name = self.browser.find_element(*GoodPageLocators.GOOD_NAME).text.strip()
        self.price = self.browser.find_element(*GoodPageLocators.GOOD_PRICE).text.strip()
        print(f"\nname: {self.name}")
        print(f"price: {self.price}")

    def add_to_basket(self):
        self.load_goods_data()
        self.browser.find_element(*GoodPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def validate_good_added_to_basket(self):
        basket_messages = self.browser.find_elements(*GoodPageLocators.SUCCESS_MESSAGE)
        basket_message = basket_messages[0]
        assert (
            self.name in basket_message.text,
            f"Good is not added or invalid good [{basket_message.text}] is added"
        )

    def validate_price_of_basket(self, expected_price: float):
        basket_messages = self.browser.find_elements(*GoodPageLocators.SUCCESS_MESSAGE)
        basket_message = basket_messages[-1]
        assert (
            self.price in basket_message.text,
            f"Price is invalid [{basket_message.text}]"
        )

    def should_not_be_success_message(self):
        assert self.is_element_present(*GoodPageLocators.SUCCESS_MESSAGE, implicitly_timeout=4), \
            "Success message is presented, but should not be"

