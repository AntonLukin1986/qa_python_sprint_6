'''Локаторы, общие для всех страниц.'''
from selenium.webdriver.common.by import By

A_CLS_CONTAINS = '//a[contains(@class, "{}")]'
# ЛОГОТИПЫ в хэдере
LOGO_YANDEX = By.XPATH, A_CLS_CONTAINS.format('LogoYandex')
LOGO_SCOOTER = By.XPATH, A_CLS_CONTAINS.format('LogoScooter')
