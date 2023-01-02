from selenium.webdriver.common.by import By

LANGUAGE_MAP = {
    "es": "Añadir al carrito",
    "ru": "Добавить в корзину",
    "fr": "Ajouter au panier",
    "en": "Add to basket",
}


def test_guest_should_see_login_link(browser, browser_language):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    basket_button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert basket_button.text == LANGUAGE_MAP.get(browser_language)
