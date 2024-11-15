'''Page object главной страницы web-сервиса «Яндекс.Самокат».'''
from selenium.webdriver.common.by import By


class MainPageQuestions:
    '''Локаторы и методы раздела «Вопросы о важном» на главной странице.'''
    QUESTION = (By.ID, 'accordion__heading-{}')
    ANSWER = (By.XPATH, '//div[@id="accordion__panel-{}"]/p')

    def __init__(self, driver, num):
        self.driver = driver
        self.question = self.QUESTION[0], self.QUESTION[1].format(num)
        self.answer = self.ANSWER[0], self.ANSWER[1].format(num)

    def question_button(self):
        '''Получение элемента "кнопка-вопрос".'''
        return self.driver.find_element(*self.question)

    def get_question_button_text(self):
        '''Получение текста кнопки-вопроса.'''
        return self.question_button().text

    def question_button_click(self):
        '''Нажатие на кнопку-вопрос.'''
        self.question_button().click()

    def answer_field(self):
        '''Получение элемента "ответ на вопрос".'''
        return self.driver.find_element(*self.answer)

    def get_answer_field_text(self):
        '''Получение текста ответа на вопрос.'''
        return self.answer_field().text

    def check_answer_field_is_shown(self):
        '''Проверка отображения ответа на вопрос.'''
        return self.answer_field().is_displayed()
