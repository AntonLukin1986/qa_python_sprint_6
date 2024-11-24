'''Page object страницы создания заказа web-сервиса «Яндекс.Самокат».'''
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from data import CONFIRM_ORDER, RENT, SCOOTER_FOR
from locators import order_page_locators as loc
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Получение заголовка формы оформления заказа.')
    def get_form_title(self):
        '''Получение заголовка формы оформления заказа.'''
        return self.get_element(loc.ORDER_FORM_TITLE).text

    @allure.step('Заполнение поля «Имя» формы данных пользователя.')
    def set_name(self, name):
        '''Заполнение поля «Имя» формы данных пользователя.'''
        self.fill_form_field(loc.NAME_FIELD, name)

    @allure.step('Заполнение поля «Фамилия» формы данных пользователя.')
    def set_surname(self, surname):
        '''Заполнение поля «Фамилия» формы данных пользователя.'''
        self.fill_form_field(loc.SURNAME_FIELD, surname)

    @allure.step('Заполнение поля «Адрес» формы данных пользователя.')
    def set_address(self, address):
        '''Заполнение поля «Адрес» формы данных пользователя.'''
        self.fill_form_field(loc.ADDRESS_FIELD, address)

    @allure.step('Заполнение поля «Метро» формы данных пользователя.')
    def set_metro(self, metro):
        '''Заполнение поля «Метро» формы данных пользователя.'''
        self.fill_form_field(loc.METRO_FIELD, metro, Keys.DOWN, Keys.ENTER)

    @allure.step('Заполнение поля «Телефон» формы данных пользователя.')
    def set_phone(self, phone):
        '''Заполнение поля «Телефон» формы данных пользователя.'''
        self.fill_form_field(loc.PHONE_FIELD, phone)

    @allure.step('Нажатие кнопки «Далее» формы данных пользователя.')
    def next_btn_click(self):
        '''Нажатие кнопки «Далее» формы данных пользователя.'''
        self.click_element(loc.NEXT_BTN)

    def fill_customer_form(self, name, surname, address, metro, phone):
        '''Заполнение всех полей формы данных пользователя
        и нажатие кнопки «Далее».'''
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.next_btn_click()

    @allure.step('Заполнение поля «Когда привезти самокат» данных аренды.')
    def set_date(self, date):
        '''Заполнение поля «Когда привезти самокат» формы данных аренды.'''
        self.fill_form_field(loc.DELIVERY_DATE, date, Keys.ESCAPE)

    @allure.step('Заполнение поля «Срок аренды» формы данных аренды.')
    def set_days(self, days):
        '''Заполнение поля «Срок аренды» формы данных аренды.'''
        self.click_element(loc.DAYS)
        self.click_element((By.XPATH, loc.TEXT_IN_DIV.format(days)))

    @allure.step('Заполнение поля «Цвет самоката» формы данных аренды.')
    def set_color(self, color):
        '''Заполнение поля «Цвет самоката» формы данных аренды.'''
        self.click_element((By.ID, color))

    @allure.step('Заполнение поля «Комментарий для курьера» данных аренды.')
    def set_comment(self, comment):
        '''Заполнение поля «Комментарий для курьера» формы данных аренды.'''
        self.fill_form_field(loc.COMMENT_FIELD, comment)

    @allure.step('Нажатие кнопки «Заказать» формы данных аренды.')
    def confirm_btn_click(self):
        '''Нажатие кнопки «Заказать» формы данных аренды.'''
        self.click_element(loc.CONFIRM_ORDER_BTN)

    def fill_rent_form_and_confirm(self, date, days, color, comment):
        '''Заполнение всех полей формы данных аренды и нажатие кнопки
        «Заказать» для формирования заказа.'''
        self.set_date(date)
        self.set_days(days)
        self.set_color(color)
        self.set_comment(comment)
        self.confirm_btn_click()

    @allure.step('Получение заголовка окна подтверждения заказа.')
    def get_confirmation_title(self):
        '''Получение заголовка окна подтверждения заказа.'''
        return self.get_element(loc.CONFIRMATION_TITLE).text

    @allure.step('Нажатие кнопки «Да» окна подтверждения заказа.')
    def yes_btn_click(self):
        '''Нажатие кнопки «Да» окна подтверждения заказа.'''
        self.click_element(loc.YES_BTN)

    @allure.step('Получение заголовка окна заказ оформлен.')
    def get_order_confirmed_title(self):
        '''Получение заголовка окна заказ оформлен.'''
        return self.get_element(loc.ORDER_CONFIRMED_TITLE).text

    def create_order(self, customer, rent):
        '''Создание нового заказа.'''
        assert self.get_form_title() == SCOOTER_FOR
        self.fill_customer_form(**customer)
        assert self.get_form_title() == RENT
        self.fill_rent_form_and_confirm(**rent)
        assert CONFIRM_ORDER in self.get_confirmation_title()
        self.yes_btn_click()
