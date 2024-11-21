from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.item_page_locators import ItemPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def check_product_page_name(self, product_name):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(ItemPageLocators.ITEM_NAME))
        assert product_name == self.find_element(ItemPageLocators.ITEM_NAME).text
