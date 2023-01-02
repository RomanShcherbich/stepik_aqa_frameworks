from selenium.webdriver.common.by import By

LANGUAGE_MAP = {
    "es": "Añadir al carrito",
    "ru": "Добавить в корзину",
    "fr": "Ajouter au panier",
    "en": "Add to basket",
}


def test_add_to_basket_button(browser, browser_language):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    basket_button_list = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert basket_button_list, "the button cannot be found by the locator"
    assert basket_button_list[0].text == LANGUAGE_MAP.get(browser_language)
