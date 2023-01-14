from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


from locators.test_order_locator import OrderPartLocators

class OrderPartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_upper_button_order(self):
        self.driver.find_element(*OrderPartLocators.upper_button_order).click()

    def set_first_order_page(self):
        self.driver.find_element(*OrderPartLocators.field_name).send_keys("Клава")
        self.driver.find_element(*OrderPartLocators.field_surname).send_keys("Кока")
        self.driver.find_element(*OrderPartLocators.field_address).send_keys("Москва, проспект Ленина")
        self.driver.find_element(*OrderPartLocators.field_metro_station).click()
        self.driver.find_element(*OrderPartLocators.exact_metro_station_1).click()
        self.driver.find_element(*OrderPartLocators.field_phone).send_keys(89076786677)

    def set_first_order_page_order_lower_button(self):
        self.driver.find_element(*OrderPartLocators.field_name).send_keys("Сева")
        self.driver.find_element(*OrderPartLocators.field_surname).send_keys("Новгородцев")
        self.driver.find_element(*OrderPartLocators.field_address).send_keys("Москва, проспект Луначарского")
        self.driver.find_element(*OrderPartLocators.field_metro_station).click()
        self.driver.find_element(*OrderPartLocators.exact_metro_station_2).click()
        self.driver.find_element(*OrderPartLocators.field_phone).send_keys(89229998877)

    def click_button_continue(self):
        self.driver.find_element(*OrderPartLocators.button_continue).click()

    def set_second_order_page(self):
        self.driver.find_element(*OrderPartLocators.field_date_of_start_using).send_keys("23.11.2023")
        self.driver.find_element(*OrderPartLocators.close_calendar).click()
        self.driver.find_element(*OrderPartLocators.field_period_of_using).click()
        self.driver.find_element(*OrderPartLocators.exact_period_of_using).click()
        self.driver.find_element(*OrderPartLocators.close_calendar).click()
        self.driver.find_element(*OrderPartLocators.field_black_color_of_scooter).click()

    def set_second_order_page_order_lower_button(self):
        self.driver.find_element(*OrderPartLocators.field_date_of_start_using).send_keys("27.03.2023")
        self.driver.find_element(*OrderPartLocators.close_calendar).click()
        self.driver.find_element(*OrderPartLocators.field_period_of_using).click()
        self.driver.find_element(*OrderPartLocators.exact_period_of_using).click()
        self.driver.find_element(*OrderPartLocators.close_calendar).click()
        self.driver.find_element(*OrderPartLocators.field_grey_color_of_scooter).click()

    def click_lower_button_order(self):
        self.driver.find_element(*OrderPartLocators.lower_button_order).click()

    def click_yes_button(self):
        self.driver.find_element(*OrderPartLocators.yes_button).click()

    def scroll_to_lower_button_order(self):
        accordion = self.driver.find_element(*OrderPartLocators.lower_button_order)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPartLocators.lower_button_order))













    def scroll_to_question_how_much(self):
        accordion = self.driver.find_element(*QuestionPartLocators.question_how_much)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.question_how_much))

