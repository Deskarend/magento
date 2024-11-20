from selenium.webdriver.common.by import By


class EcoFriendlyPageLocators:
    LINK_SALE = (By.ID, 'ui-id-8')

    PRODUCTS_NAMES = (By.CLASS_NAME, 'product-item-link')

    AUTHORIZATION_LINK = (By.CLASS_NAME, 'authorization-link')
