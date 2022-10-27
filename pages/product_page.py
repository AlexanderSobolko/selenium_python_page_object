from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def click_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def compare_product_name_in_message(self):
        product_name_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name_text = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name_text == message_product_name_text
