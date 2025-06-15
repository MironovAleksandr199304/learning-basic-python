from def_lesson_ch2 import grade_to_score,is_passed,final_price,check_test_result, apply_discount
from def_lesson3 import parse_user_data
import requests


import pytest
from pytest import approx
# ✅ Задача 1: Проверка функции grade_to_score
# Условие:
# Есть функция grade_to_score(grade), возвращающая балл:
# "отлично" → 5
# "хорошо" → 4
# "удовлетворительно" → 3
# всё остальное → 2
# Напиши тест, который проверяет все 4 случая.
# Ожидание:
# Обычные assert, каждый кейс проверяется отдельно.

def test_grade_to_score():
    assert grade_to_score("отлично") == 5
    assert grade_to_score("хорошо") == 4
    assert grade_to_score("удовлетворительно") == 3
    assert grade_to_score("неизвестно") == 2

#
# ✅ Задача 2: Проверка is_passed с параметризацией
# Условие:
# Есть функция is_passed(grade), которая возвращает True, если балл ≥ 3
# Используй @pytest.mark.parametrize, чтобы протестировать такие кейсы:
# "отлично" → True
# "хорошо" → True
# "удовлетворительно" → True
# "плохо" → False
# "что-то непонятное" → False
# Ожидание:
# Один параметризованный тест с assert.

@pytest.mark.parametrize("grade, expected",[
    ("отлично",True),
    ("хорошо",True),
    ("удовлетворительно",True),
    ("плохо",False)
])

def test_is_passed(grade,expected):
    assert is_passed(grade) == expected


#
# ✅ Задача 3: Проверка final_price с approx
# Условие:
# Есть функция final_price(price, discount, vat), которая:
# применяет скидку
# затем добавляет НДС
# Протестируй 3 кейса с approx, например:
# 1000, 20, 20 → 960.0
# 200, 10, 10 → 198.0
# 500, 0, 0 → 500.0
# Ожидание:
# Обычные тесты с approx(...).
def test_final_price():
    assert final_price(1000,20,20) == approx(960.0)
    assert final_price(0,20,20) == approx(0.0)
    assert final_price(10,20,20) == approx(9.6)



#
# ✅ Задача 4: Тест функции parse_user_data
# Условие:
# Есть функция parse_user_data(data_str), парсит строку вроде:
# "login=alex;email=alex@test.com;id=42"
# → в словарь: {"login": ..., "email": ..., "id": ...}
# Проверь:
# обычный случай
# пустую строку
# лишний = (например: login=alex=email → должен игнорировать)
# Ожидание:
# Обычные assert, желательно с описанием ожидаемого словаря.

def test_parse_user_data():
    """
    проверка, что строка парсится нормально
    """
    assert parse_user_data("login=alex;email=alex@test.com;id=42") == {"login": "alex",
                                                                       "email": "alex@test.com",
                                                                       "id": "42"} #почему тут проходит, если id имеет значение только строку, а если число то не проходит?
    assert parse_user_data ("") == {} #OK
    assert parse_user_data("login=alex=email=alex@test.com;id=42") == {"id":"42"} #OK



#
# ✅ Задача 5: Проверка test_result — "Сдано" / "Не сдано"
# Условие:
# Есть функция test_result(answers, total_questions)
# Она возвращает "Сдано" если ≥ 70% OK, иначе "Не сдано"
# Проверь такие кейсы:
# ["OK", "OK", "OK", "FAIL", "FAIL"], 5 → "Сдано"
# ["OK", "OK", "FAIL", "FAIL", "FAIL"], 5 → "Не сдано"
# Ожидание:
# Обычные assert, минимум 2–3 кейса.

def test_check_test_result():
    assert check_test_result(["OK", "OK", "OK", "OK", "FAIL"],5) == "Сдано"
    assert check_test_result(["OK", "OK", "FAIL", "FAIL", "FAIL"],5) == "Не сдано"

#
# ✅ Задача 6: apply_discount + параметризация
# Условие:
# Есть функция apply_discount(price, discount)
# Протестируй её с параметризацией на 3 кейсах:
# 1000, 20 → 800.0
# 5000, 50 → 2500.0
# 600, 0 → 600.0
# Ожидание:
# Параметризованный тест, используешь approx(...) при необходимости.

@pytest.mark.parametrize("price,discount,expected",[
    (1000, 20, 800.0),
    (5000, 50, 2500.0),
    (600, 0, 600.0)
])

def test_apply_discount(price,discount,expected):
    assert apply_discount(price,discount) == approx(expected)