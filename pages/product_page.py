from .base_page import BasePage
from .locators import *


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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_MSG), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_MSG), \
            "Success message is presented, but should not be"