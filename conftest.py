import pytest
from faker import Faker
from selenium import webdriver

from pages.create_account_page import CreateAccount
from pages.eco_friendly_page import EcoFriendlyPage
from pages.sale_page import SalePage

fake = Faker()


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


@pytest.fixture
def create_account(driver):
    return CreateAccount(driver)


@pytest.fixture
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture
def first_name():
    return fake.first_name()


@pytest.fixture
def last_name():
    return fake.last_name()


@pytest.fixture
def email():
    return fake.email()


@pytest.fixture
def password():
    return fake.password()
