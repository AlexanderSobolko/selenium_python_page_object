from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BUTTON = (By.XPATH, "//*[@id=\"default\"]/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")



class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    MESSAGE_ADD_TO_BASKET = (By.XPATH, "//*[@id=\"messages\"]/div[1]")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div.alertinner strong")

    MESSAGE_PRICE_IN_BASKET = (By.XPATH, "//*[@id=\"messages\"]/div[3]")
    PRODUCT_PRICE = (By.XPATH, "//*[@id=\"content_inner\"]/article/div[1]/div[2]/p[1]")
    PRICE_IN_MESSAGE = (By.XPATH, "//*[@id=\"messages\"]/div[3]/div/p[1]/strong")


class Text:
    YOUR_BASKET_IS_EMPTY = {'ru': 'Ваша корзина пуста Продолжить покупки',
                            'en': 'Your basket is empty. Continue shopping'}


class BasketPageLocators():
    BOOK_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset > div > div")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
