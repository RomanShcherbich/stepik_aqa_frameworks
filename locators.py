from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > .btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_LIST = (By.CSS_SELECTOR, "#content_inner .basket-items > .row")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class GoodPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    GOOD_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    GOOD_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")
