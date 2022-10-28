from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "No message about adding to basket"

    def compare_product_name_in_message(self):
        product_name_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name_text == message_product_name_text, "Product name is different"

    def should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE_IN_BASKET), "No price message"

    def compare_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_product_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert product_price == message_product_price, "Different prices"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message should disappear"
