from datetime import datetime
import pytest
from pathlib import Path
from source.calculator import Calculator
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    reports_dir = Path('test-reports')
    reports_dir.mkdir(parents=True, exist_ok=True)
    # TODO: Create sub-folder `test_execution_<timestamp>`,
    #  put a test report and all related screenshots to this sub-folder
    report = reports_dir / f"Test_report_{now.strftime('%Y-%m-%d %H:%M:%S')}.html"
    logging.debug(f"Creating test report: {report}")
    config.option.htmlpath = report
    config.option.self_contained_html = True


def pytest_addoption(parser):
    """Fetches command line args for pytest."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser type: chrome or firefox",
        choices=("chrome", "firefox"),
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Browser runs in a headless mode or not"
    )


@pytest.fixture
def driver(request):
    """Creates test fixtures for pytest."""
    _browser = request.config.getoption("--browser").lower()
    is_headless = request.config.getoption("--headless")

    if _browser == "chrome":
        _options = webdriver.ChromeOptions()
        if is_headless:
            _options.add_argument("--headless")
            _options.add_argument("--window-size=1920,1080")
        else:
            _options.add_argument("--start-maximized")

        logging.info(f"Start Chrome Webdriver: options: {_options}")
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                      options=_options)

    elif _browser == "firefox":
        _options = webdriver.FirefoxOptions()
        if is_headless:
            _options.add_argument("--headless")
            _options.add_argument("--window-size=1920,1080")
        else:
            _options.add_argument("--start-maximized")

        logging.info(f"Start FireFox Webdriver: options: {_options}")
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                       options=_options)
    else:
        raise NameError(f"Unsupported browser: {_browser}")

    web_driver.delete_all_cookies()

    request.addfinalizer(lambda *args: finalizer(web_driver))
    return web_driver


def finalizer(web_driver):
    """Close/quit browser after the test is completed."""
    logging.info("Closing Webdriver")
    web_driver.close()
    web_driver.quit()


@pytest.fixture
def calculator():
    calc = Calculator()
    logging.debug(f"Execute fixture before")
    yield calc
    logging.debug(f"Execute fixture after")
