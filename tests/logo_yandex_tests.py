from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.logo_yandex_page import LogoYandexPage


class TestLogoYandex():
    def test_yandex_logo(self, driver):
        click_yandex = LogoYandexPage(driver)
        click_yandex.click_logo_yandex()
        click_yandex.switch_to_window(1)
        WebDriverWait(driver, 30).until(expected_conditions.url_to_be("https://dzen.ru/?yredirect=true"))
        visible_url=click_yandex.get_current_url()
        assert visible_url == "https://dzen.ru/?yredirect=true"
