from def_lesson_ch2 import grade_to_score, is_passed, final_price, apply_discount, check_test_result
from def_lesson3 import parse_user_data
from pytest import approx
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

# * Чистая арифметика, без НДС
# * Идеально для закрепления `approx`
#
# ### 2. ✅ `parse_user_data(data_str)`
#
# * Логическая проверка: словарь, строки, ключи
# * Хороший пример для `assert result == {...}`



#
# ### 3. ✅ `test_result(answers, total_questions)`
#
# * Там проценты, строки — можно протестить `"Сдано"` и `"Не сдано"`
#
# ---
#
# ## 📌 Предлагаю: протестим `parse_user_data`
#
# Вот функция, которую ты писал:
#
# ```python
# def parse_user_data(data_str):
#     result = {}
#     parts = data_str.split(";")
#     for pair in parts:
#         key_value = pair.strip().split("=")
#         if len(key_value) == 2:
#             key, value = key_value
#             result[key.strip()] = value.strip()
#     return result
# ```
#
# ---
#
# ## 🔍 Что можно проверить в тестах
#
# | Вход                                     | Ожидаемый результат                                       |
# | ---------------------------------------- | --------------------------------------------------------- |
# | `"login=alex;email=alex@test.com;id=42"` | `{"login": "alex", "email": "alex@test.com", "id": "42"}` |
# | `""`                                     | `{}`                                                      |
# | `"x=1;x=2"`                              | `{"x": "2"}` (дубликат — остаётся последнее)              |
# | `"badpair;id=5"`                         | `{"id": "5"}` (мусор пропущен)                            |
#
# ---
#
# ## 💡 Твоя задача:
#
# * Создать `test_parse_user_data()`
# * Сделать хотя бы **2–3 `assert`**
# * Я посмотрю и дам ревью
#
# Готов?
