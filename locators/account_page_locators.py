from selenium.webdriver.common.by import By


class AccountPageLocators:
    TITLE_MY_ACCOUNT_TAB = (By.CLASS_NAME, 'base')
    SUCCESSFUL_CREATING_ALERT = (By.CSS_SELECTOR, '[role="alert"]')