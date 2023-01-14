
from locators.test_logo_samokat_locator import LogoSamokatLocators
from pages.test_logo_samokat_page import LogoSamokatPage


class TestLogoSamokat():
    def test_logo_samokat(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        samokat_logo = LogoSamokatPage(driver)
        samokat_logo.click_logo_samokat()
        element_scooter = driver.find_element(*LogoSamokatLocators.scooter_image)
        assert element_scooter.is_displayed()