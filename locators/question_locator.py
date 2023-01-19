from selenium.webdriver.common.by import By

class QuestionPartLocators:
    question_how_much = [By.ID, "accordion__heading-0"]
    answer_how_much = [By.ID, "accordion__panel-0"]
    question_need_several = [By.ID, "accordion__heading-1"]
    answer_need_several = [By.ID,"accordion__panel-1"]
    question_time_of_rent = [By.ID, "accordion__heading-2"]
    answer_time_of_rent = [By.ID, "accordion__panel-2"]
    question_order_for_today = [By.ID,"accordion__heading-3"]
    answer_order_for_today = [By.ID, "accordion__panel-3"]
    question_use_longer_return_earlier = [By.ID, "accordion__heading-4"]
    answer_use_longer_return_earlier = [By.ID, "accordion__panel-4"]
    question_about_charger = [By.ID, "accordion__heading-5"]
    answer_about_charger = [By.ID, "accordion__panel-5"]
    question_cancel_order = [By.ID, "accordion__heading-6"]
    answer_cancel_order = [By.ID, "accordion__panel-6"]
    question_live_behind_MKAD = [By.ID, "accordion__heading-7"]
    answer_live_behind_MKAD = [By.ID, "accordion__panel-7"]