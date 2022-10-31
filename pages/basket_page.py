from .base_page import BasePage
from .locators import BasketPageLocators, Text


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOK_IN_BASKET), \
            "Basket is not empty"

    def should_be_empty_basket_message(self, text_locale):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert text == Text.YOUR_BASKET_IS_EMPTY[text_locale], \
            "No empty basket message"
