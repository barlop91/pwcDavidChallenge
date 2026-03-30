from selenium.webdriver.common.by import By


class TextBoxPage:
    URL = "https://demoqa.com/text-box"

    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    NAME_OUTPUT = (By.ID, "name")
    EMAIL_OUTPUT = (By.ID, "email")
    CURRENT_ADDRESS_OUTPUT = (By.CSS_SELECTOR, "p#currentAddress")
    PERMANENT_ADDRESS_OUTPUT = (By.CSS_SELECTOR, "p#permanentAddress")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.URL)

    def fill_form(self, full_name, email, current_address, permanent_address):
        self.driver.find_element(*self.FULL_NAME_INPUT).send_keys(full_name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.CURRENT_ADDRESS_INPUT).send_keys(current_address)
        self.driver.find_element(*self.PERMANENT_ADDRESS_INPUT).send_keys(permanent_address)

    def click_submit(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()

    def get_name(self):
        return self.driver.find_element(*self.NAME_OUTPUT).text

    def get_email(self):
        return self.driver.find_element(*self.EMAIL_OUTPUT).text

    def get_current_address(self):
        return self.driver.find_element(*self.CURRENT_ADDRESS_OUTPUT).text

    def get_permanent_address(self):
        return self.driver.find_element(*self.PERMANENT_ADDRESS_OUTPUT).text