from .base_page import BasePage
from .locators import *


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty"

    def basket_should_be_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text == \
               "Your basket is empty. Continue shopping", "Basket is not empty"