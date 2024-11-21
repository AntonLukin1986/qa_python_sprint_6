'''Фикстуры для тестов web-сервиса «Яндекс.Самокат».'''
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from data import FIREFOX_PATH, MAIN_PAGE


@pytest.fixture(scope='function')
def driver():
    '''Создание драйвера браузера.'''
    options = webdriver.FirefoxOptions()
    options.add_argument(argument='--window-size=1920,1080')
    service = Service(executable_path=FIREFOX_PATH)
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()
