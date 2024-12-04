import pytest
from faker import Faker
from selenium import webdriver

from pages.account_page import AccountPage
from pages.create_account_page import CreateAccount
from pages.eco_friendly_page import EcoFriendlyPage
from pages.gear_page import GearPage
from pages.men_sale_page import MenSalePage
from pages.product_page import ProductPage
from pages.sale_page import SalePage
from pages.sign_in_page import SignInPage
from pages.women_sale_page import WomenSalePage

fake = Faker()


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


@pytest.fixture
def create_account(driver):
    return CreateAccount(driver)


@pytest.fixture
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture
def sing_in_page(driver):
    return SignInPage(driver)


@pytest.fixture
def women_sale_page(driver):
    return WomenSalePage(driver)


@pytest.fixture
def men_sale_page(driver):
    return MenSalePage(driver)


@pytest.fixture
def gear_page(driver):
    return GearPage(driver)


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
