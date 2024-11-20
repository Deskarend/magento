from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.account_page_locators import AccountPage
from locators.gear_page_locators import GearLocators
from locators.item_page_locators import ItemPageLocators
from locators.men_sale_locators import MenSaleLocators
from locators.sale_page_locators import SalePageLocators
from locators.sing_in_locators import SignInLocators
from locators.women_sale_locators import WomenSaleLocators


class BasePage:
    page_url = None
    wait = 5

    random_product_name = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.page_url)

    def find_element(self, element):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(element))
        return self.driver.find_element(*element)

    def find_elements(self, element):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_all_elements_located(element))
        return self.driver.find_elements(*element)

    def click_on_element(self, element):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    def fill_field(self, element, value):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(element))
        web_element = self.driver.find_element(*element)
        web_element.send_keys(value)
        assert web_element.get_attribute('value') == value

    def check_element_text(self, element, text):
        web_element = self.find_element(element)
        assert web_element.text == text

    def check_is_this_account_page(self):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(AccountPage.TITLE_MY_ACCOUNT_TAB))

    def check_is_this_sale_page(self):
        assert WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(SalePageLocators.TITLE))

    def check_is_this_random_product_page(self):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(ItemPageLocators.ITEM_NAME))
        assert self.random_product_name == self.find_element(ItemPageLocators.ITEM_NAME).text

    def check_is_this_sign_in_page(self):
        assert WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(SignInLocators.TITLE))

    def check_is_this_women_sale_page(self):
        assert WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(WomenSaleLocators.TITLE))

    def check_is_this_men_sale_page(self):
        assert WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(MenSaleLocators.TITLE))

    def check_is_this_gear_page(self):
        assert WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(GearLocators.TITLE))
