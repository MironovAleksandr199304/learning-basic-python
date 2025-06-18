import pytest
import requests
# ✅ Задача 1 — Проверка GET /users/{id}
# Условие:
# Напиши параметризованный тест, который:
# делает GET запрос к /users/{id} (например, 1, 2, 3)
# проверяет, что:
# status_code == 200
# поле id в ответе совпадает с user_id
# в ответе есть поле email и оно — строка
# На выходе:
# Параметризованный тест-функция с 3–5 user_id и проверками выше.

@pytest.mark.parametrize("id",[
    (1),
    (2),
    (3),
    (4),
    (5)
])

def test_get_users(user_id):
    response = get_users(user_id)
    assert response.status_code == 200
    data = response.json()
    assert user_id == data["id"]
    assert "email" in data
    assert isinstance(data["email"],str)


#
# ✅ Задача 2 — Проверка POST /posts
# Условие:
# Сделай тест, который:
# создаёт новый пост через POST /posts
# использует фикстуру sample_post_payload
# проверяет:
# status_code == 201
# title, body, userId в ответе совпадают с отправленными
# в ответе есть поле id и это число
def test_post_new(base_url, sample_post_payload): #допустим мы используем фикстуру base_url еще
    response = requests.post(f"{base_url}/posts/", json=sample_post_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == sample_post_payload["title"] ##допустим в sample_post_payload такие значения
    assert data["body"] == sample_post_payload["body"]
    assert data["userId"] == sample_post_payload["userId"]
    assert "id" in data
    assert isinstance(data["id"],int)
# ✅ Задача 3 — Проверка PUT /posts/1
# Условие:
# Создай тест, который:
# полностью обновляет пост с id=1 через PUT
# использует фикстуру put_post_payload
# проверяет:
# status_code == 200
# title, body, userId совпадают с теми, что в payload
# id остаётся 1

def test_put_post(base_url, put_post_payload):
    response = requests.put(f"{base_url}/posts/1", json=put_post_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == put_post_payload["title"]
    assert data["body"] == put_post_payload["body"]
    assert data["userId"] == put_post_payload["userId"]
    assert data["id"] == 1

#
# ✅ Задача 4 — Проверка PATCH /posts/1
# Условие:
# Тестирует частичное обновление title поста:
# использует фикстуру patch_post_payload
# проверяет:
# status_code == 200
# title обновился
# остальные поля (body, userId, id) остались, и имеют корректные типы

def test_patch_post(base_url, patch_post_payload):
    patch_response = requests.patch(f"{base_url}/posts/1", json=patch_post_payload)
    assert patch_response.status_code == 200
    data = patch_response.json()
    assert data["title"] == patch_post_payload["title"] #а блин, реально можно было же так
    assert "body" in data
    assert "userId" in data
    assert "id" in data
    assert isinstance(data["body"],str)
    assert isinstance(data["userId"],int) #пускай будет int
    assert isinstance(data["id"],int)

#
# ✅ Задача 5 — Проверка DELETE /posts/1
# Условие:
# Тестирует удаление поста:
# отправляет DELETE на /posts/1
# проверяет:
# status_code == 200
# тело ответа пустое ({})

def test_delete_post(base_url):
    response_delete = requests.delete(f"{base_url}/posts/1")
    assert response_delete.status_code == 200
    data = response_delete.json()
    assert data == {}