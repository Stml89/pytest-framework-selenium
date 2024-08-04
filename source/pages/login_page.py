""" POM of the Login page. """
from test_data.constants import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from source.pages.base import BasePage


class LoginPage(BasePage):
    """ Login page class. """

    def __init__(self, driver):
        super().__init__(driver)
        self.username_input_selector = (By.ID, "user-name")
        self.password_input_selector = (By.ID, "password")
        self.login_button_selector = (By.CLASS_NAME, "btn_action")
        self.error_message_selector = (By.XPATH, '//*[@id="login_button_container"]/div/form')
        self.login_form = (By.CLASS_NAME, 'login_wrapper-inner')
        self.open()
        self.should_be_login_page()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert self.driver.current_url == URL, "Should be on the login page"

    def should_be_login_form(self):
        assert self.element_is_present(*self.login_form)

    def perform_complete_login(self, username, password):
        """ Perform a complete login using username and password. """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def click_login(self):
        """ Click the login button. """
        self.click_element(self.login_button_selector)
        WebDriverWait(self.driver, 5).until(EC.url_changes)

    def enter_password(self, password):
        """ Enter a password into the password textbox. """
        self.send_keys_to_element(self.password_input_selector, password)

    def enter_username(self, username):
        """ Enter a username into the username textbox. """
        self.send_keys_to_element(self.username_input_selector, username)

    def error_message_exists(self):
        """ Returns true if an error message exists on the page, false otherwise. """
        error_message = self.driver.find_elements(*self.error_message_selector)
        return len(error_message) > 0

    def get_error_message_text(self):
        """ Returns the text of the error message on the page, if one exists.
        Returns None otherwise. """
        if self.error_message_exists():
            return self.driver.find_elements(*self.error_message_selector)[0].text
        return None
