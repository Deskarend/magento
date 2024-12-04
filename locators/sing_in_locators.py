from selenium.webdriver.common.by import By


class SignInLocators:
    TITLE = (By.XPATH, '//*[@class="base" and contains(text(), "Customer Login")]')
