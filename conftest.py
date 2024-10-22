from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser_options():
    options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--incognito")  # runs chrome in incognito mode
    options.add_argument("--start-maximized")  # Start window maximized
    options.add_argument("--no-sandbox")
    # options.add_argument("--window-size=900,600")  # window size customization
    # options.add_argument("--disable-infobars")
    return options


@pytest.fixture(scope="session")
def launch_chrome():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    return driver
