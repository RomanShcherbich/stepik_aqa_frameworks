import time

import pytest

from locators import GoodPageLocators
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser)
    basket_page.should_be_basket_url()
    basket_page.should_be_empty()


SHELLCODER_S_HANDBOOK_URL = (
    "http://selenium1py.pythonanywhere.com/en-gb/"
    "catalogue/the-shellcoders-handbook_209/?promo=newYear"
)


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    shellcoder_s_handbook_page = ProductPage(browser, SHELLCODER_S_HANDBOOK_URL)
    shellcoder_s_handbook_page.open()
    shellcoder_s_handbook_page.add_to_basket()
    assert shellcoder_s_handbook_page.is_not_element_present(*GoodPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    shellcoder_s_handbook_page = ProductPage(browser, SHELLCODER_S_HANDBOOK_URL)
    shellcoder_s_handbook_page.open()
    shellcoder_s_handbook_page.add_to_basket()
    assert shellcoder_s_handbook_page.is_disappeared(*GoodPageLocators.SUCCESS_MESSAGE)


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        login_page.open()
        login_page.register_new_user(email, "secret_pass")
        login_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        shellcoder_s_handbook_page = ProductPage(browser, SHELLCODER_S_HANDBOOK_URL)
        shellcoder_s_handbook_page.open()
        shellcoder_s_handbook_page.add_to_basket()
        shellcoder_s_handbook_page.validate_good_added_to_basket()
        shellcoder_s_handbook_page.validate_price_of_basket(shellcoder_s_handbook_page.price)

    def test_user_cant_see_success_message(self, browser):
        shellcoder_s_handbook_page = ProductPage(browser, SHELLCODER_S_HANDBOOK_URL)
        shellcoder_s_handbook_page.open()
        assert shellcoder_s_handbook_page.is_not_element_present(*GoodPageLocators.SUCCESS_MESSAGE)
