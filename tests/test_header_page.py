'''Тесты элементов в хэдере web-сервиса «Яндекс.Самокат».'''
import allure
import pytest

from data import MAIN_PAGE, ORDER_PAGE, REDIRECT
from pages.header_page import HeaderPage


class TestHeaderPage:
    @allure.title('Редирект по клику на лого «Яндекс» и «Самокат»')
    @pytest.mark.parametrize(
        'logo, url',
        [pytest.param('yandex', REDIRECT, id='Logo Yandex'),
         pytest.param('scooter', MAIN_PAGE, id='Logo Scooter')]
    )
    def test_logo_click_redirect(self, driver, logo, url):
        '''По клику на логотип «Яндекс» открывается страница «Дзен».
        По клику на логотип «Самокат» открывается главная страница.'''
        self.header_page = HeaderPage(driver)
        self.header_page.order_button_click()
        assert self.header_page.get_current_url() == ORDER_PAGE
        getattr(self.header_page, f'{logo}_logo_click')()
        self.header_page.switch_window(url)
        assert self.header_page.get_current_url() == url
