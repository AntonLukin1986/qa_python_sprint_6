'''Page object страницы создания заказа web-сервиса «Яндекс.Самокат».'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators import order_page_locators as loc


class OrderPage:
    '''Методы страницы создания заказа.'''
    def __init__(self, driver):
        self.driver = driver

    def order_button_click(self, where):
        '''Нажатие кнопки «Заказать» в хэдере или в мэйне.'''
        if where == 'header':
            locator = loc.ORDER_BTN_HEADER
        elif where == 'main':
            locator = loc.ORDER_BTN_MAIN
        button = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView()', button)
        button.click()

    def get_form_title(self):
        '''Получение заголовка формы оформления заказа.'''
        return self.driver.find_element(*loc.ORDER_FORM_TITLE).text

    def set_name(self, name):
        '''Заполнение поля «Имя» формы данных пользователя.'''
        self.driver.find_element(*loc.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        '''Заполнение поля «Фамилия» формы данных пользователя.'''
        self.driver.find_element(*loc.SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        '''Заполнение поля «Адрес» формы данных пользователя.'''
        self.driver.find_element(*loc.ADDRESS_FIELD).send_keys(address)

    def set_metro(self, metro):
        '''Заполнение поля «Метро» формы данных пользователя.'''
        self.driver.find_element(*loc.METRO_FIELD).send_keys(
            metro, Keys.DOWN, Keys.ENTER
        )

    def set_phone(self, phone):
        '''Заполнение поля «Телефон» формы данных пользователя.'''
        self.driver.find_element(*loc.PHONE_FIELD).send_keys(phone)

    def next_btn_click(self):
        '''Нажатие кнопки «Далее» формы данных пользователя.'''
        self.driver.find_element(*loc.NEXT_BTN).click()

    def fill_customer_form(self, name, surname, address, metro, phone):
        '''Заполнение всех полей формы данных пользователя
        и нажатие кнопки «Далее».'''
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.next_btn_click()

    def set_date(self, date):
        '''Заполнение поля «Когда привезти самокат» формы данных аренды.'''
        self.driver.find_element(*loc.DELIVERY_DATE).send_keys(
            date, Keys.ESCAPE
        )

    def set_days(self, days):
        '''Заполнение поля «Срок аренды» формы данных аренды.'''
        self.driver.find_element(*loc.DAYS).click()
        self.driver.find_element(
            By.XPATH, loc.TEXT_IN_DIV.format(days)
        ).click()

    def set_color(self, color):
        '''Заполнение поля «Цвет самоката» формы данных аренды.'''
        self.driver.find_element(By.ID, color).click()

    def set_comment(self, comment):
        '''Заполнение поля «Комментарий для курьера» формы данных аренды.'''
        self.driver.find_element(*loc.COMMENT_FIELD).send_keys(comment)

    def confirm_btn_click(self):
        '''Нажатие кнопки «Заказать» формы данных аренды.'''
        self.driver.find_element(*loc.CONFIRM_ORDER_BTN).click()

    def fill_rent_form_and_confirm(self, date, days, color, comment):
        '''Заполнение всех полей формы данных аренды и нажатие кнопки
        «Заказать» для формирования заказа.'''
        self.set_date(date)
        self.set_days(days)
        self.set_color(color)
        self.set_comment(comment)
        self.confirm_btn_click()

    def get_confirmation_title(self):
        '''Получение заголовка окна подтверждения заказа.'''
        return self.driver.find_element(*loc.CONFIRMATION_TITLE).text

    def yes_btn_click(self):
        '''Нажатие кнопки «Да» окна подтверждения заказа.'''
        self.driver.find_element(*loc.YES_BTN).click()

    def get_order_confirmed_title(self):
        '''Получение заголовка окна заказ оформлен.'''
        return self.driver.find_element(*loc.ORDER_CONFIRMED_TITLE).text

    def status_btn_click(self):
        '''Нажатие кнопки «Посмотреть статус» окна заказ оформлен.'''
        self.driver.find_element(*loc.STATUS_BTN).click()
