from selenium.webdriver.support import expected_conditions
from locators.test_order_locator import OrderPartLocators
from pages.test_order_part_pages import OrderPartPage
from selenium.webdriver.support.wait import WebDriverWait

class TestOrderPart():
    def test_order_upper_button(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_upper_button = OrderPartPage(driver)
        order_upper_button.click_upper_button_order()
        order_upper_button.set_first_order_page()
        order_upper_button.click_button_continue()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(OrderPartLocators.field_date_of_start_using))
        order_upper_button.set_second_order_page()
        order_upper_button.click_lower_button_order()
        order_upper_button.click_yes_button()
        element_window_order_is_successful = driver.find_element(*OrderPartLocators.window_order_is_successful)
        assert element_window_order_is_successful.is_displayed()

    def test_order_lower_button(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_lower_button = OrderPartPage(driver)
        order_lower_button.scroll_to_lower_button_order()
        order_lower_button.click_lower_button_order()
        order_lower_button.set_first_order_page_order_lower_button()
        order_lower_button.click_button_continue()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(OrderPartLocators.field_date_of_start_using))
        order_lower_button.set_second_order_page_order_lower_button()
        order_lower_button.click_lower_button_order()
        order_lower_button.click_yes_button()
        element_window_order_is_successful = driver.find_element(*OrderPartLocators.window_order_is_successful)
        assert element_window_order_is_successful.is_displayed()