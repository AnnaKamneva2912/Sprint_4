from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from locators.test_logo_samokat_locator import LogoSamokatLocators

class LogoSamokatPage:
    def __init__(self, driver):
        self.driver = driver

    def click_logo_samokat(self):
        self.driver.find_element(*LogoSamokatLocators.upper_button_order).click()
        self.driver.find_element(*LogoSamokatLocators.logo_samokat).click()

