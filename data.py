'''Дополнительные данные для тестов web-сервиса «Яндекс.Самокат».'''
from pages.header_page import HeaderPage
from pages.main_page import MainPage

MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
ORDER_PAGE = MAIN_PAGE + 'order'
REDIRECT = 'https://dzen.ru/?yredirect=true'

# Вопросы и ответы в разделе «Вопросы о важном» главной страницы
QUESTION_1 = 'Сколько это стоит? И как оплатить?'
ANSWER_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
QUESTION_2 = 'Хочу сразу несколько самокатов! Так можно?'
ANSWER_2 = '''Пока что у нас так: один заказ — один самокат. \
Если хотите покататься с друзьями, можете просто сделать несколько \
заказов — один за другим.'''
QUESTION_3 = 'Как рассчитывается время аренды?'
ANSWER_3 = '''Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат \
8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы \
оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная \
аренда закончится 9 мая в 20:30.'''
QUESTION_4 = 'Можно ли заказать самокат прямо на сегодня?'
ANSWER_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
QUESTION_5 = 'Можно ли продлить заказ или вернуть самокат раньше?'
ANSWER_5 = '''Пока что нет! Но если что-то срочное — всегда можно позвонить \
в поддержку по красивому номеру 1010.'''
QUESTION_6 = 'Вы привозите зарядку вместе с самокатом?'
ANSWER_6 = '''Самокат приезжает к вам с полной зарядкой. Этого хватает на \
восемь суток — даже если будете кататься без передышек и во сне. \
Зарядка не понадобится.'''
QUESTION_7 = 'Можно ли отменить заказ?'
ANSWER_7 = '''Да, пока самокат не привезли. Штрафа не будет, объяснительной \
записки тоже не попросим. Все же свои.'''
QUESTION_8 = 'Я жизу за МКАДом, привезёте?'
ANSWER_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
FAQ = {
    0: {'q': QUESTION_1, 'a': ANSWER_1}, 1: {'q': QUESTION_2, 'a': ANSWER_2},
    2: {'q': QUESTION_3, 'a': ANSWER_3}, 3: {'q': QUESTION_4, 'a': ANSWER_4},
    4: {'q': QUESTION_5, 'a': ANSWER_5}, 5: {'q': QUESTION_6, 'a': ANSWER_6},
    6: {'q': QUESTION_7, 'a': ANSWER_7}, 7: {'q': QUESTION_8, 'a': ANSWER_8}
}
# заголовки на странице создания заказа
SCOOTER_FOR = 'Для кого самокат'
RENT = 'Про аренду'
CONFIRM_ORDER = 'Хотите оформить заказ?'
BOOKED = 'Заказ оформлен'
# наборы данных для заполнения формы
CUSTOMER_1 = {
    'name': 'Станислав', 'surname': 'Дробышевский', 'phone': '84951234567',
    'address': 'Кафедра Антропологии МГУ', 'metro': 'Охотный Ряд'
}
CUSTOMER_2 = {
    'name': 'Владимир', 'surname': 'Сурдин', 'phone': '84997654321',
    'address': 'г.Москва, отдел Звездной астрофизики ГАИШ МГУ',
    'metro': 'Университет'
}
RENT_1 = {
    'date': '31.12.2024', 'days': 'сутки', 'color': 'black', 'comment': ''
}
RENT_2 = {
    'date': '01.01.2025', 'days': 'семеро суток', 'color': 'grey',
    'comment': 'Поскорей!'
}
SCENARIO_1 = HeaderPage, CUSTOMER_1, RENT_1
SCENARIO_2 = MainPage, CUSTOMER_2, RENT_2
