'''Фикстуры для тестов web-сервиса «Яндекс.Самокат».'''
import pytest
from selenium import webdriver

from data import MAIN_PAGE


@pytest.fixture(scope='function')
def driver():
    '''Создание драйвера браузера.'''
    options = webdriver.FirefoxOptions()
    options.add_argument(argument='--window-size=1920,1080')
    driver = webdriver.Firefox(options=options)
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()
