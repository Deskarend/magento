from locators.women_sale_locators import WomenSaleLocators
from pages.base_page import BasePage


class WomenSalePage(BasePage):
    def check_is_this_women_sale_page(self):
        self.check_page_title(WomenSaleLocators.TITLE)
