from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.XPATH, "//*[@id=\"default\"]/header/div[1]/div/div[2]/span/a")


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    MESSAGE_ADD_TO_BASKET = (By.XPATH, "//*[@id=\"messages\"]/div[1]")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div.alertinner strong")

    MESSAGE_PRICE_IN_BASKET = (By.XPATH, "//*[@id=\"messages\"]/div[3]")
    PRODUCT_PRICE = (By.XPATH, "//*[@id=\"content_inner\"]/article/div[1]/div[2]/p[1]")
    PRICE_IN_MESSAGE = (By.XPATH, "//*[@id=\"messages\"]/div[3]/div/p[1]/strong")
