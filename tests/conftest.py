from datetime import datetime
import pytest
from pathlib import Path
from source.calculator import Calculator
import logging


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    reports_dir = Path('test-reports')
    reports_dir.mkdir(parents=True, exist_ok=True)
    report = reports_dir / f"Test_report_{now.strftime('%Y-%m-%d %H:%M:%S')}.html"
    logging.debug(f"Creating test report: {report}")
    config.option.htmlpath = report
    config.option.self_contained_html = True

@pytest.fixture
def calculator():
    calc = Calculator()
    logging.debug(f"Execute fixture before")
    yield calc
    logging.debug(f"Execute fixture after")
