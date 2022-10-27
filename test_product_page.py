import time
from .pages.base_page import BasePage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    solv = BasePage(browser, link)
    solv.solve_quiz_and_get_code()
    time.sleep(5)
