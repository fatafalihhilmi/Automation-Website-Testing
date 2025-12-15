import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://indonesiaindicator.com/home"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def take_screenshot(driver, name: str):
    driver.save_screenshot(f"screenshots/{name}.png")


def switch_to_new_tab(driver):
    original = driver.current_window_handle
    windows = driver.window_handles
    for handle in windows:
        if handle != original:
            driver.switch_to.window(handle)
            return original
    return original
