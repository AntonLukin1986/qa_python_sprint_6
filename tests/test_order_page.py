'''Тесты страницы создания заказа web-сервиса «Яндекс.Самокат».'''
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
from pages.order_page import OrderPage
from pages.base_page import BasePageHeader


class TestOrderPage:
    '''Тесты процесса создания заказа.'''
    @classmethod
    def setup_class(cls):
        '''Создание драйвера браузера.'''
        options = webdriver.FirefoxOptions()
        options.add_argument(argument='--window-size=1920,1080')
        service = Service(executable_path=data.FIREFOX_PATH)
        cls.driver = webdriver.Firefox(service=service, options=options)

    def fill_order_form(self, customer, rent):
        '''Заполнение двух частей формы заказа.'''
        assert self.main_page.get_form_title() == data.SCOOTER_FOR
        self.main_page.fill_customer_form(**customer)
        assert self.main_page.get_form_title() == data.RENT
        self.main_page.fill_rent_form_and_confirm(**rent)
        assert data.CONFIRM_ORDER in self.main_page.get_confirmation_title()
        self.main_page.yes_btn_click()
        assert data.BOOKED in self.main_page.get_order_confirmed_title()
        self.main_page.status_btn_click()

    def test_create_order(self, scenario):
        '''Успешное создание заказа через кнопку «Заказать» в хэдере
        или в мэйне.'''
        self.driver.get(data.MAIN_PAGE)
        self.main_page = OrderPage(self.driver)
        self.main_page.order_button_click(scenario['button'])
        self.fill_order_form(scenario['customer'], scenario['rent'])
        logo, url = scenario['logo']
        getattr(BasePageHeader(self.driver), f'{logo}_logo_click')()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 5).until(
            expected_conditions.url_to_be(url)
        )
        assert self.driver.current_url == url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
