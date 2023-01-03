import pytest

from pages.product_page import ProductPage

SHELLCODER_S_HANDBOOK_URL = (
    "http://selenium1py.pythonanywhere.com/en-gb/"
    "catalogue/the-shellcoders-handbook_209/?promo=newYear"
)

CODER_S_AT_WORK_URL = (
    "http://selenium1py.pythonanywhere.com/en-gb/"
    "catalogue/coders-at-work_207/?promo=newYear2019"
)


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("bugged_link:?promo=offer6", marks=pytest.mark.skip),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_add_to_basket(browser, link):
    shellcoder_s_handbook_page = ProductPage(browser, link)
    shellcoder_s_handbook_page.open()
    shellcoder_s_handbook_page.add_to_basket()
    shellcoder_s_handbook_page.validate_good_added_to_basket()
    shellcoder_s_handbook_page.validate_price_of_basket(shellcoder_s_handbook_page.price)
