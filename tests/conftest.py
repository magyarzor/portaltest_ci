import pytest
import os
from playwright.sync_api import sync_playwright

from utils.browser_setting import start_browser, close_browser
from pages.home_page import HomePage

@pytest.fixture(scope="function")
def browser():
    playwright, context, page = start_browser()
    yield page
    close_browser(playwright, context)

@pytest.fixture(scope="function")
def home_page(browser):
    return HomePage(browser).open()
