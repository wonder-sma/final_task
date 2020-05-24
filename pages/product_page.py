from .base_page import BasePage
from .locators import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

    def add_product_to_basket_msg(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
            self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MSG).text, "Product name is different"

    def basket_value_msg(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
            self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MSG).text, "Product price is different"

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_MSG), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_not_be_success_message_after_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_MSG), \
            "Success message is presented, but should not be"