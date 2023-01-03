import pytest

from locators import GoodPageLocators
from pages.product_page import ProductPage

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


def test_guest_cant_see_success_message(browser):
    shellcoder_s_handbook_page = ProductPage(browser, SHELLCODER_S_HANDBOOK_URL)
    shellcoder_s_handbook_page.open()
    assert shellcoder_s_handbook_page.is_not_element_present(*GoodPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    shellcoder_s_handbook_page = ProductPage(browser, SHELLCODER_S_HANDBOOK_URL)
    shellcoder_s_handbook_page.open()
    shellcoder_s_handbook_page.add_to_basket()
    assert shellcoder_s_handbook_page.is_disappeared(*GoodPageLocators.SUCCESS_MESSAGE)
