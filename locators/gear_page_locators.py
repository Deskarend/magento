from selenium.webdriver.common.by import By


class GearLocators:
    TITLE = (By.XPATH, '//*[@class="base" and contains(text(), "Gear")]')
