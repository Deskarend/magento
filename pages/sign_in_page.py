from pages.base_page import BasePage
from locators.sing_in_locators import SignInLocators


class SignInPage(BasePage):
    def check_is_this_sign_in_page(self):
        self.check_page_title(SignInLocators.TITLE)
