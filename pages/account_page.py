import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step('Проверка нахождения на странице аккаунта')
    def check_is_this_account_page(self):
        WebDriverWait(self.driver, self.wait).until(
            EC.visibility_of_element_located(AccountPageLocators.TITLE_MY_ACCOUNT_TAB)
        )

    @allure.step('Проверка наличия плажки нового аккаунта')
    def check_creating_new_account(self, creating_new_account_text):
        self.check_is_this_account_page()
        self.check_element_text(AccountPageLocators.SUCCESSFUL_CREATING_ALERT, creating_new_account_text)
