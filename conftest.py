'''Фикстуры для тестов web-сервиса «Яндекс.Самокат».'''
import pytest

from data import FAQ


@pytest.fixture(scope='function', params=range(len(FAQ)))
def faq(request):
    '''Получение идентификатора элемента и текстов вопроса и ответа.'''
    num = request.param
    return num, *FAQ[num]
