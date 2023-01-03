from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > .btn-group > a")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class GoodPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    GOOD_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    GOOD_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")
