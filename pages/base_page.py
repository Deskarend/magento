from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    page_url = None
    wait = 5

    random_product_name = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.page_url)

    def find_element(self, element):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(element))
        return self.driver.find_element(*element)

    def find_elements(self, element):
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_all_elements_located(element))
        return self.driver.find_elements(*element)

    def click_on_element(self, element):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    def fill_field(self, element, value):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(element))
        web_element = self.driver.find_element(*element)
        web_element.send_keys(value)
        assert web_element.get_attribute('value') == value

    def check_element_text(self, element, text):
        web_element = self.find_element(element)
        assert web_element.text == text

    def check_page_title(self, page_title_locator):
        assert WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(page_title_locator))
