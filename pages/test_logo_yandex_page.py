from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from locators.test_logo_yandex_locator import LogoYandexLocators

class LogoYandexPage:
    def __init__(self, driver):
        self.driver = driver

    def click_logo_yandex(self):
        self.driver.find_element(*LogoYandexLocators.logo_yandex).click()

    def switch_to_window(self, number):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[number])

    def get_current_url(self):
        return self.driver.current_url
