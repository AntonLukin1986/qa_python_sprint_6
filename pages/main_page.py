'''Page object главной страницы web-сервиса «Яндекс.Самокат».'''
import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage
from locators.patterns import BUTTON, DIV_CLS_CONTAINS


class MainPage(BasePage):
    ANSWER = By.XPATH, '//div[@id="accordion__panel-{}"]/p'
    QUESTION = By.ID, 'accordion__heading-{}'
    ORDER_BTN = (
        By.XPATH,
        DIV_CLS_CONTAINS.format('FinishButton') + BUTTON.format('Заказать')
    )

    def format_locator(self, num, locator):
        '''Получение форматированного локатора элемента.'''
        method, pattern = locator
        return method, pattern.format(num)

    @allure.step('Клик по кнопке «Заказать».')
    def order_button_click(self):
        '''Клик по кнопке «Заказать».'''
        self.scroll_to_element(self.ORDER_BTN)
        self.click_element(self.ORDER_BTN)

    @allure.step('Получение текста кнопки-вопроса.')
    def get_question_text(self, num):
        '''Получение текста кнопки-вопроса.'''
        return self.get_element(self.format_locator(num, self.QUESTION)).text

    @allure.step('Клик по кнопке-вопросу.')
    def question_click(self, num):
        '''Клик по кнопке-вопросу.'''
        self.scroll_to_element(self.format_locator(num, self.QUESTION))
        self.click_element(self.format_locator(num, self.QUESTION))

    @allure.step('Получение текста ответа на вопрос.')
    def get_answer_text(self, num):
        '''Получение текста ответа на вопрос.'''
        return self.get_element(self.format_locator(num, self.ANSWER)).text

    @allure.step('Проверка отображения ответа на вопрос.')
    def check_answer_field_is_shown(self, num):
        '''Проверка отображения ответа на вопрос.'''
        return self.get_element(
            self.format_locator(num, self.ANSWER)
        ).is_displayed()
