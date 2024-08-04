""" POM Base class for all other Page classes. """
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from test_data.constants import URL


class BasePage:
    """ Page class. """
    def __init__(self, driver):
        self.driver = driver
        self.url = URL

    def open(self):
        """ Initialize the URL. """
        self.driver.get(self.url)

    def click_element(self, selector, wait_time=5):
        """
        Click on aan element identified by 'selector'
        :param selector: The selector of the element to click
        :param wait_time: Time to wait before timing out, default 5 seconds
        :return: None
        """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.click()

    def send_keys_to_element(self, selector, text, wait_time=5):
        """ Enter a username into the username textbox. """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.send_keys(text)

    def element_is_present(self, method, locator):
        try:
            self.driver.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    # TODO: Implement saving screenshot functionality
    # def save_screenshot(self, filename=None):
    #     """
    #     Saves the screenshot of the current window. Returns False if there is
    #        any IOError, else returns True. Filename can be full path, path name or empty.
    #     """
    #     def __find_unused_file_name():
    #       pass
    #
    #     if not filename:
    #         filename = __find_unused_file_name()
    #         logging.info(f"Saving image <a href='{filename}'>{filename}</a>")
    #
    #     return self.driver.save_screenshot(file)
