import pytest
from selenium import webdriver
import config
from pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config.Urls.base_url)
    yield driver
    driver.quit()

@pytest.fixture
def controller(driver):
    controller = MainPage(driver)
    return controller
