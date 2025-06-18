import requests
import pytest

def get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url) #записываем результат запроса GET к сайту, указанному в переменной url
    return response #возвращаем весь json (ну я думаю так, что его)

print(get_user(5)) #смотрим че тут

@pytest.mark.parametrize("user_id",[1,2,5,10])

def test_get_user_success_parametrize(user_id):
    response = get_user(user_id) #получаем ответ по 1 user_id от jsonplaceholder

    assert response.status_code == 200 #проверяем, что такой user_id есть и jsonplaceholder возвращает с кодом 200 (т.е. без ошибок)
    data = response.json() #записываем json в data
    assert data["id"] == user_id

    assert "name" in data #проверка поля name в json ответе
    assert isinstance (data["email"],str) #проверяем, что в поле email строка, а не числа или еще что-то

def test_get_user_fail_parametrize():
    response = get_user(99) #пытаемся получить ответ по 99 юзеру

    assert response.status_code == 404 #проверяем, что тут 404 статус

def create_post(title, body, user_id):
    """
    Отправляет POST-запрос на создание поста.
    Возвращает объект ответа
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title" : title, #заголовок поста
        "body" : body,
        "userId" : user_id
    }
    response = requests.post(url, json=payload)
    return response


def test_create_post_success():
    response = create_post("Тестовый заголовок","Содержимое поста",1)
    assert response.status_code == 201
    data = response.json()

    assert data["title"] == "Тестовый заголовок"
    assert data["body"] == "Содержимое поста"
    assert data["userId"] == 1

    assert "id" in data
    assert isinstance(data["id"],int)

@pytest.mark.parametrize("title1, body1, user1, title2, body2, user2, title3, body3, user3",[
    ("Первый заголовок","Запоминаю параметризацию",1,
     "Пытаюсь изучить pytest","Пока дается с натяжкой, но вроде поддается",2,
     "А дальше?","как говорил классик - 'Тяжело в учении - легко в бою'",3)
])

def test_create_post_unique_id_parametrize(title1,body1,user1, title2, body2, user2, title3, body3, user3):
    response1 = create_post(title1,body1,user1)
    response2 = create_post(title2,body2,user2)
    response3 = create_post(title3, body3, user3)
    data1 = response1.json()
    data2 = response2.json()
    data3 = response3.json()
    assert data1["title"] != data2["title"]
    assert data2["body"] != data3["body"]

def test_get_fixture_status_code(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200

def test_create_post_with_fixture(base_url, headers, sample_post_payload):
    """
    тест создания поста с использованием фикстур для URL, заголовка, тела
    """
    response = requests.post(f"{base_url}/posts", json=sample_post_payload,headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == sample_post_payload["title"]
    assert data["body"] == sample_post_payload["body"]
    assert data["userId"] == sample_post_payload["userId"]

def test_put_post_with_fixture(base_url, headers, put_post_payload):
    response = requests.put(f"{base_url}/posts/1", json=put_post_payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Обновленный заголовок"
    assert data["body"] == "Обновленное тело"
    assert data["userId"] == 999
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data
    assert "id" in data

def test_patch_post_with_fixture(base_url, headers, patch_post_payload):
    response = requests.patch(f"{base_url}/posts/1", json=patch_post_payload, headers=headers)
    # Проверить:
    # status_code == 200
    # В ответе title — обновлён
    # Остальные поля(userId, body, id)
    # остались и имеют нужные типы
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "обновляем только заголовок"
    assert "body" in data
    assert "userId" in data
    assert "id" in data
    assert isinstance(data["body"],str)
    assert isinstance(data["id"],int)
    assert isinstance(data["userId"],int)

def test_delete_post(base_url):
    response = requests.delete(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert response.json() == {}