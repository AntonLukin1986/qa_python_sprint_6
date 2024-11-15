'''Page object главной страницы web-сервиса «Яндекс.Самокат».'''
from locators import base_page_locators as loc


class BasePageHeader:
    '''Общие для всех страниц методы в хэдере.'''
    def __init__(self, driver):
        self.driver = driver

    def yandex_logo_click(self):
        '''Нажатие на логотип «Яндекс».'''
        self.driver.find_element(*loc.LOGO_YANDEX).click()

    def scooter_logo_click(self):
        '''Нажатие на логотип «Самокат».'''
        self.driver.find_element(*loc.LOGO_SCOOTER).click()
