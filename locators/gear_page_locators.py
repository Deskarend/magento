from selenium.webdriver.common.by import By


class GearPageLocators:
    TITLE = (By.XPATH, '//*[@class="base" and contains(text(), "Gear")]')
