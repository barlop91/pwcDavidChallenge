from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.text_box_page import TextBoxPage
from utils.driver_factory import get_driver


def test_text_box_form():
    driver = get_driver()

    full_name = "John Doe"
    email = "john.doe@example.com"
    current_address = "123 Main St"
    permanent_address = "456 Secondary St"

    text_box_page = TextBoxPage(driver)

    text_box_page.open_page()
    text_box_page.fill_form(full_name, email, current_address, permanent_address)
    text_box_page.click_submit()


    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(text_box_page.NAME_OUTPUT)
    )

    assert text_box_page.get_name() == f"Name:{full_name}"
    assert text_box_page.get_email() == f"Email:{email}"
    assert text_box_page.get_current_address() == f"Current Address :{current_address}"
    assert text_box_page.get_permanent_address() == f"Permananet Address :{permanent_address}"

    driver.quit()