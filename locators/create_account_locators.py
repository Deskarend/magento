from selenium.webdriver.common.by import By


class CreateAccountLocators:
    FIELD_FIRST_NAME = (By.ID, 'firstname')
    FIELD_LAST_NAME = (By.ID, 'lastname')

    FIELD_EMAIL = (By.ID, 'email_address')
    EMAIL_ERROR = (By.ID, 'email_address-error')

    FIELD_PASSWORD = (By.ID, 'password')
    FIELD_CONFIRM_PASSWORD = (By.ID, 'password-confirmation')
    CONFIRM_PASSWORD_ERROR = (By.ID, 'password-confirmation-error')

    BUTTON_CREATE_ACCOUNT = (By.CLASS_NAME, 'submit')
