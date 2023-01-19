from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.question_locator import QuestionPartLocators

class QuestionPartPage():
    def __init__(self, driver):
        self.driver = driver
    def click_on_question(self, question):
        self.driver.find_element(*question).click()
    def scroll_to_question(self, question):
        accordion = self.driver.find_element(*question)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(question))

