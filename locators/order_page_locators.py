'''Локаторы для страницы создания заказа.'''
from selenium.webdriver.common.by import By

# УНИВЕРСАЛЬНЫЕ ЭЛЕМЕНТЫ
BUTTON = '//button[text()="{}"]'
TEXT_IN_DIV = '//div[text()="{}"]'
INPUT_FIELD = '//input[@placeholder="{}"]'
DIV_CLS_CONTAINS = '//div[contains(@class, "{}")]'
# ПЕРЕХОД К ФОРМЕ ЗАКАЗА
ORDER_BTN = BUTTON.format('Заказать')
ORDER_BTN_HEADER = (  # кнопка в хэдере
    By.XPATH, DIV_CLS_CONTAINS.format('Header') + ORDER_BTN
)
ORDER_BTN_MAIN = (  # кнопка в мэйн
    By.XPATH, DIV_CLS_CONTAINS.format('FinishButton') + ORDER_BTN
)
ORDER_FORM_TITLE = By.XPATH, DIV_CLS_CONTAINS.format('Order_Header')
# ФОРМА "Для кого самокат"
NAME_FIELD = By.XPATH, INPUT_FIELD.format('* Имя')
SURNAME_FIELD = By.XPATH, INPUT_FIELD.format('* Фамилия')
ADDRESS_FIELD = By.XPATH, INPUT_FIELD.format('* Адрес: куда привезти заказ')
METRO_FIELD = By.XPATH, INPUT_FIELD.format('* Станция метро')
PHONE_FIELD = (
    By.XPATH, INPUT_FIELD.format('* Телефон: на него позвонит курьер')
)
NEXT_BTN = By.XPATH, BUTTON.format('Далее')
# ФОРМА "Про аренду"
CONFIRM_ORDER_BTN = (
    By.XPATH, DIV_CLS_CONTAINS.format('Order_Buttons') + ORDER_BTN
)
DELIVERY_DATE = By.XPATH, INPUT_FIELD.format('* Когда привезти самокат')
DAYS = By.XPATH, TEXT_IN_DIV.format('* Срок аренды')
COMMENT_FIELD = By.XPATH, INPUT_FIELD.format('Комментарий для курьера')
# ОКНО ПОДТВЕРЖДЕНИЯ ЗАКАЗА
CONFIRMATION_TITLE = By.XPATH, TEXT_IN_DIV.format('Хотите оформить заказ?')
YES_BTN = By.XPATH, BUTTON.format('Да')
# ОКНО "ЗАКАЗ ОФОРМЛЕН"
ORDER_CONFIRMED_TITLE = By.XPATH, TEXT_IN_DIV.format('Заказ оформлен')
STATUS_BTN = By.XPATH, BUTTON.format('Посмотреть статус')
