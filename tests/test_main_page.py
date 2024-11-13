'''Тесты главной страницы web-сервиса «Яндекс.Самокат».'''
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from data import MAIN_PAGE
from pages.main_page import MainPageQuestions


class TestMainPageQuestions:
    '''Тесты раздела «Вопросы о важном» на главной странице.'''
    @classmethod
    def setup_class(cls):
        '''Создание драйвера браузера.'''
        options = webdriver.FirefoxOptions()
        options.add_argument(argument='--window-size=1920,1080')
        service = Service(
            executable_path=r'C:\DRIVERS\geckodriver-v0.35.0-win64\geckodriver.exe'
        )
        cls.driver = webdriver.Firefox(service=service, options=options)
        cls.driver.get(MAIN_PAGE)

    def test_answer_shows_after_click_on_question_button(self, faq):
        '''При нажатии на кнопку-вопрос отображается корректный ответ.'''
        num, question, answer = faq
        self.main_page = MainPageQuestions(self.driver, num)
        assert self.main_page.get_question_button_text() == question
        assert not self.main_page.check_answer_field_is_shown()
        self.driver.execute_script('arguments[0].scrollIntoView()', self.main_page.question_button())
        self.main_page.question_button_click()
        assert self.main_page.check_answer_field_is_shown()
        assert self.main_page.get_answer_field_text() == answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
