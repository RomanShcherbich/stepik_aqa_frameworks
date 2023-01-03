from locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"invalid url [{self.browser.current_url}] in login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f"Login form element not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), f"Registration form element not found"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON).click()

