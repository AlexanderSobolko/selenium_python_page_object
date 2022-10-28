import pytest

from .pages.base_page import BasePage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail),
                                         "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    solv = BasePage(browser, link)
    solv.solve_quiz_and_get_code()

    page.should_be_add_message()
    page.compare_product_name_in_message()
    page.should_be_price_message()
    page.compare_price_in_message()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_success_message()


@pytest.mark.skip(reason="no way of currently testing this")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    page.success_message_should_disappear()
