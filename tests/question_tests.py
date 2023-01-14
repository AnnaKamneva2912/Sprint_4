from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.question_locator import QuestionPartLocators
from pages.question_part_pages import QuestionPartPage

class TestQuestionPart():
    def test_question_how_much(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        question_how_much = QuestionPartPage(driver)
        question_how_much.scroll_to_question_how_much()
        question_how_much.click_question_how_much()
        WebDriverWait(driver, 13).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.answer_how_much))
        element_answer_how_much = driver.find_element(*QuestionPartLocators.answer_how_much)
        assert element_answer_how_much.is_displayed()

    def test_question_need_several(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        question_need_several = QuestionPartPage(driver)
        question_need_several.scroll_to_question_need_several()
        question_need_several.click_question_need_several()
        WebDriverWait(driver, 13).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.answer_need_several))
        element_answer_need_several = driver.find_element(*QuestionPartLocators.answer_need_several)
        assert element_answer_need_several.is_displayed()

    def test_question_time_of_rent(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        question_time_of_rent = QuestionPartPage(driver)
        question_time_of_rent.scroll_to_question_time_of_rent()
        question_time_of_rent.click_question_time_of_rent()
        WebDriverWait(driver, 13).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.answer_time_of_rent))
        element_answer_time_of_rent = driver.find_element(*QuestionPartLocators.answer_time_of_rent)
        assert element_answer_time_of_rent.is_displayed()

    def test_question_order_for_today(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        question_order_for_today = QuestionPartPage(driver)
        question_order_for_today.scroll_to_question_order_for_today()
        question_order_for_today.click_question_order_for_today()
        WebDriverWait(driver, 13).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.answer_order_for_today))
        element_answer_order_for_today = driver.find_element(*QuestionPartLocators.answer_order_for_today)
        assert element_answer_order_for_today.is_displayed()

    def test_question_use_longer_return_earlier(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        question_use_longer_return_earlier = QuestionPartPage(driver)
        question_use_longer_return_earlier.scroll_to_question_use_longer_return_earlier()
        question_use_longer_return_earlier.click_question_use_longer_return_earlier()
        WebDriverWait(driver, 13).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.answer_use_longer_return_earlier))
        element_answer_use_longer_return_earlier = driver.find_element(*QuestionPartLocators.answer_use_longer_return_earlier)
        assert element_answer_use_longer_return_earlier.is_displayed()

    def test_question_about_charger(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        question_about_charger = QuestionPartPage(driver)
        question_about_charger.scroll_to_question_about_charger()
        question_about_charger.click_question_about_charger()
        WebDriverWait(driver, 13).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.answer_about_charger))
        element_answer_about_charger = driver.find_element(*QuestionPartLocators.answer_about_charger)
        assert element_answer_about_charger.is_displayed()

    def test_question_cancel_order(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        question_cancel_order = QuestionPartPage(driver)
        question_cancel_order.scroll_to_question_cancel_order()
        question_cancel_order.click_question_cancel_order()
        WebDriverWait(driver, 13).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.answer_cancel_order))
        element_answer_cancel_order = driver.find_element(*QuestionPartLocators.answer_cancel_order)
        assert element_answer_cancel_order.is_displayed()

    def test_question_live_behind_MKAD(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        question_live_behind_MKAD = QuestionPartPage(driver)
        question_live_behind_MKAD.scroll_to_question_live_behind_MKAD()
        question_live_behind_MKAD.click_question_live_behind_MKAD()
        WebDriverWait(driver, 13).until(expected_conditions.visibility_of_element_located(QuestionPartLocators.answer_live_behind_MKAD))
        element_answer_live_behind_MKAD = driver.find_element(*QuestionPartLocators.answer_live_behind_MKAD)
        assert element_answer_live_behind_MKAD.is_displayed()