from selenium.webdriver.common.by import By


class SalePageLocators:
    TITLE = (By.XPATH, '//*[@class="base" and contains(text(), "Sale")]')

    BUTTON_WOMEN_DEALS = (By.CSS_SELECTOR, '.more.button')

    LINK_MEN_DEALS = (By.XPATH, '//*[@class="more icon" and contains(text(), "Shop Men’s Deals")]')
    LINK_LUMA_GEAR = (By.XPATH, '//*[@class="more icon" and contains(text(), "Luma Gear")]')
