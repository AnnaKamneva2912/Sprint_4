import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()