'''Тесты элементов в хэдере web-сервиса «Яндекс.Самокат».'''
import allure
import pytest

from data import MAIN_PAGE, ORDER_PAGE, REDIRECT
from pages.header_page import HeaderPage


class TestHeaderPage:
    @allure.title('Редирект по клику на лого «Яндекс» и «Самокат»')
    @pytest.mark.parametrize(
        'name, url',
        [pytest.param('yandex', REDIRECT, id='Logo Yandex'),
         pytest.param('scooter', MAIN_PAGE, id='Logo Scooter')]
    )
    def test_logo_click_redirect(self, driver, name, url):
        '''По клику на логотип «Яндекс» открывается страница «Дзен».
        По клику на логотип «Самокат» открывается главная страница.'''
        header_page = HeaderPage(driver)
        header_page.order_button_click()
        assert header_page.get_current_url() == ORDER_PAGE
        getattr(header_page, f'{name}_logo_click')()
        header_page.switch_window(url)
        assert header_page.get_current_url() == url
