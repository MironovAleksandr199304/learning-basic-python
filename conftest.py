import pytest

@pytest.fixture
def base_url():
    """Фикстура, возвращающая url"""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def headers():
    """
    Фикстура, возвращающая заголовки POST-запросов
    """

    return {
        "Content-Type" : "application/json"
    }

@pytest.fixture
def sample_post_payload():
    """
    Фикстура, возвращающая тело запроса для создания поста
    """
    return{
        "title" : "Заголовок из фикстуры",
        "body" : "тело из фикстуры",
        "userId": 777
    }

@pytest.fixture
def put_post_payload():
    """
    фикстура, возвращающая тело запроса для обновления поста
    """
    return{
        "id" : 1,
        "title" : "Обновленный заголовок",
        "body" : "Обновленное тело",
        "userId" : 999
    }

@pytest.fixture
def patch_post_payload():
    """
    фикстура, возвращающая тело запроса для обновления через patch
    """
    return{
        "title" : "обновляем только заголовок"
    }