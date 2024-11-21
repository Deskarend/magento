from pages.base_page import BasePage
from locators.men_sale_locators import MenSaleLocators


class MenSalePage(BasePage):
    def check_is_this_men_sale_page(self):
        self.check_page_title(MenSaleLocators.TITLE)
