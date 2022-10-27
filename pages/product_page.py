from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
