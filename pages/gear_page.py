from pages.base_page import BasePage
from locators.gear_page_locators import GearPageLocators


class GearPage(BasePage):
    def check_is_this_gear_page(self):
        self.check_page_title(GearPageLocators.TITLE)
