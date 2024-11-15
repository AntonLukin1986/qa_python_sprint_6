'''Фикстуры для тестов web-сервиса «Яндекс.Самокат».'''
import pytest

from data import FAQ, SCENARIO


@pytest.fixture(scope='function', params=range(len(FAQ)))
def faq(request):
    '''Получение идентификатора элемента и текстов вопроса и ответа.'''
    num = request.param
    return num, *FAQ[num]


@pytest.fixture(scope='function', params=SCENARIO)
def scenario(request):
    '''Получение тестового сценария для создания заказа.'''
    return request.param
