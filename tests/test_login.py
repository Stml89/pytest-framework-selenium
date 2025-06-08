"""Testing the login page of saucedemo.com"""
import pytest
import test_data.login_creds as lc
from source.pages.login_page import LoginPage
import logging


@pytest.mark.login
@pytest.mark.login_success
@pytest.mark.smoke
def test_login_valid_user(driver):
    """Test logging in with a valid username/password."""
    logging.info("Verifying that user can login with correct creds")
    login_page = LoginPage(driver)
    logging.info(f"Entering username {lc.STANDARD_USER}")
    login_page.enter_username(lc.STANDARD_USER)
    logging.info(f"Entering password {lc.STANDARD_PASSWORD}")
    login_page.enter_password(lc.STANDARD_PASSWORD)
    logging.info("Clicking on login button")
    login_page.click_login()

    assert not login_page.error_message_exists()
    logging.info("Successfully verified that user can login with correct creds")


@pytest.mark.parametrize(
    "username, password",
    [
        (lc.TEST_USER, "abc123"),
        ("notauser", lc.STANDARD_PASSWORD),
    ],
)
@pytest.mark.login
@pytest.mark.login_incorrect
@pytest.mark.smoke
def test_login_incorrect_credentials(driver, username, password):
    """Test attempting to log in with invalid credentials."""
    logging.info("Verifying that use can not login with incorrect creds")
    login_page = LoginPage(driver)
    logging.info(f"Entering username/password {lc.STANDARD_USER}/{lc.STANDARD_PASSWORD}")
    login_page.perform_complete_login(username, password)
    assert login_page.error_message_exists()
    logging.info(login_page.get_error_message_text())
    logging.info("Successfully verified that use can login with incorrect creds")


@pytest.mark.parametrize(
    "username, password",
    [
        (lc.EMPTY_STRING, lc.STANDARD_PASSWORD),
        (lc.STANDARD_USER, lc.EMPTY_STRING),
    ],
)
@pytest.mark.login
@pytest.mark.login_incorrect
@pytest.mark.smoke
def test_login_missing_username(driver, username, password):
    """Test attempting to log in with a blank username."""
    logging.info("Verifying that use can not login with empty creds")
    login_page = LoginPage(driver)
    logging.info(f"Entering username/password {lc.STANDARD_USER}/{lc.STANDARD_PASSWORD}")
    login_page.perform_complete_login(username, password)
    assert login_page.error_message_exists()
    logging.info(login_page.get_error_message_text())
    logging.info("Successfully verified that use can login with empty creds")
