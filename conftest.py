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