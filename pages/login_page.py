from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        pass_field.send_keys(password)
        confirm_pass_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_pass_field.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()