from def_lesson_ch2 import grade_to_score, is_passed, final_price, apply_discount, check_test_result
from def_lesson3 import parse_user_data
from def_lesson4 import get_user_by_id
from pytest import approx
import requests
import pytest
# ### 2. ✅ `parse_user_data(data_str)`
#
# * Логическая проверка: словарь, строки, ключи
# * Хороший пример для `assert result == {...}`

def test_check_test_result():
    assert check_test_result(["OK", "OK", "OK", "OK", "FAIL"],5) == "Сдано"
    assert check_test_result(["OK", "OK", "OK", "FAIL", "FAIL"],5) == "Не сдано"
    assert check_test_result(["OK", "OK", "FAIL", "FAIL", "FAIL"],5) == "Не сдано"
    assert check_test_result(["OK", "OK", "OK", "OK", "OK"], 5) == "Сдано"
    assert check_test_result(["FAIL", "FAIL", "FAIL", "FAIL", "FAIL"], 5) == "Не сдано"


def test_parse_user_data():
    assert parse_user_data("login=alex;email=alex@test.com;id=42") == {'login': 'alex', 'email': 'alex@test.com', 'id': '42'}

def test_grade_to_score():
    assert grade_to_score("отлично") == 5
    assert grade_to_score("хорошо") == 4
    assert grade_to_score("удовлетворительно") == 3
    assert grade_to_score("что-то левое") == 2

def test_is_passed():
    assert is_passed("отлично") is True
    assert is_passed("хорошо") is True
    assert is_passed("удовлетворительно") is True
    assert is_passed("плохо") is False
    assert is_passed("неизвестно") is False

@pytest.mark.parametrize("grade,expected",[
    ("отлично", True),
    ("хорошо", True),
    ("удовлетворительно", True),
    ("плохо", False),
    ("неизвестно", False)
])
def test_is_passed_parametrize(grade,expected):
        assert is_passed(grade) is expected


# 👉 Следующий шаг (по желанию)
# Если хочешь — давай протестируем:
# final_price(price, discount, vat)
# Там надо быть аккуратным с float, потому что pytest может ругаться на погрешность в 0.000001.
# Могу показать:
# как сравнивать через round(...);
# или через pytest.approx() — как делают в реальных проектах.
# Готов двигаться дальше?
def test_final_price():
    assert final_price(1000, 20, 20) == approx(960.0)
    assert final_price(200, 10, 10) == approx(198.0)
    assert final_price(500, 0, 0) == approx(500.0)

# Отлично, Саша! 🔥 Рад тебя видеть в боевом духе. Раз ты вернулся — значит, дело пойдёт.

# ---

## 🧪 Что можно сейчас покрыть автотестами (из уже написанного):

### 1. ✅ `apply_discount(price, discount)`

def test_apply_discount():
    assert apply_discount(1000,20) == approx(800.0)
    assert apply_discount(3333, 10) == approx(2999.7)
    assert apply_discount(60343, 40) == approx(36205.8)

def test_get_user_by_id():
    assert get_user_by_id(1)["name"] == "Alice"
    assert get_user_by_id(999) is None
    assert get_user_by_id(2)["name"] == "Bob"
    assert get_user_by_id(2)["email"] == "bob@test.com"

@pytest.mark.parametrize("user_id,field,expected",
                         [
                             (1,"email","alice@test.com"),
                             (2,"name","Bob"),
                             (1,"name","Alice"),
                             (2, "email","bob@test.com")
                         ])
def test_get_user_by_id_parametrize(user_id,field,expected):
    assert get_user_by_id(user_id)[field] == expected

def test_post_then_get(base_url, headers, sample_post_payload):
    """
    Тест: создаем пост - получаем его по id, сверяем содержимое(в mock API это просто тренировка
    логики)
    """
#1. Создаем пост
    post_response = requests.post(f"{base_url}/posts",json=sample_post_payload)
    assert  post_response.status_code == 201

    post_data = post_response.json()
    created_id = post_data["id"]

#2. Получаем пост по id
    get_response = requests.get(f"{base_url}/posts/{created_id}")
    assert get_response.status_code == 200

    get_data = get_response.json()

    #сравниваем поля. совпадения не будет и это ок
    assert "title" in get_data
    assert isinstance(get_data["userId"],int)


