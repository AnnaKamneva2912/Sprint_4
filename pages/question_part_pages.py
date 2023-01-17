from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
from locators.question_locator import QuestionPartLocators

class QuestionPartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_question_how_much(self):
        self.driver.find_element(*QuestionPartLocators.question_how_much).click()

    def click_question_need_several(self):
        self.driver.find_element(*QuestionPartLocators.question_need_several).click()

    def click_question_time_of_rent(self):
        self.driver.find_element(*QuestionPartLocators.question_time_of_rent).click()

    def click_question_order_for_today(self):
        self.driver.find_element(*QuestionPartLocators.question_order_for_today).click()

    def click_question_use_longer_return_earlier(self):
        self.driver.find_element(*QuestionPartLocators.question_use_longer_return_earlier).click()

    def click_question_about_charger(self):
        self.driver.find_element(*QuestionPartLocators.question_about_charger).click()

    def click_question_cancel_order(self):
        self.driver.find_element(*QuestionPartLocators.question_cancel_order).click()

    def click_question_live_behind_MKAD(self):
        self.driver.find_element(*QuestionPartLocators.question_live_behind_MKAD).click()

    def scroll_to_question_how_much(self):
        accordion = self.driver.find_element(*QuestionPartLocators.question_how_much)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.question_how_much))

    def scroll_to_question_need_several(self):
        accordion_1 = self.driver.find_element(*QuestionPartLocators.question_need_several)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_1)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.question_need_several))

    def scroll_to_question_time_of_rent(self):
        accordion_2 = self.driver.find_element(*QuestionPartLocators.question_time_of_rent)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_2)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.question_time_of_rent))

    def scroll_to_question_order_for_today(self):
        accordion_3 = self.driver.find_element(*QuestionPartLocators.question_order_for_today)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_3)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.question_order_for_today))

    def scroll_to_question_use_longer_return_earlier(self):
        accordion_4 = self.driver.find_element(*QuestionPartLocators.question_order_for_today)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_4)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.question_use_longer_return_earlier))

    def scroll_to_question_about_charger(self):
        accordion_5 = self.driver.find_element(*QuestionPartLocators.question_order_for_today)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_5)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.question_about_charger))

    def scroll_to_question_cancel_order(self):
        accordion_6 = self.driver.find_element(*QuestionPartLocators.question_order_for_today)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_6)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.question_cancel_order))

    def scroll_to_question_live_behind_MKAD(self):
        accordion_7 = self.driver.find_element(*QuestionPartLocators.question_order_for_today)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_7)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.question_live_behind_MKAD))


