# 🧪 Задача 1 — Перевод оценки в балл
# Напиши функцию grade_to_score(grade), которая:
# "отлично" → 5
# "хорошо" → 4
# "удовлетворительно" → 3
# всё остальное → 2
# Напиши функцию is_passed(grade), которая возвращает True, если балл ≥ 3, иначе False.
# Используй внутри неё grade_to_score.

def grade_to_score(grade):
    if grade == "отлично":
        return 5
    elif grade == "хорошо":
        return 4
    elif grade == "удовлетворительно":
        return 3
    else:
        return 2

def is_passed(grade):
    score = grade_to_score(grade)
    return score >= 3




#
# 🧪 Задача 2 — Цена со скидкой и НДС
# Напиши функцию final_price(price, discount, vat_percent), которая:
# сначала применяет скидку
# потом добавляет НДС (например, 20%)
# Внутри используй:
# def apply_discount(price, discount):
#     return price * (1 - discount / 100)
def apply_discount(price, discount):
    return price * (1 - discount / 100)

def final_price(price, discount, vat_percent):
    discounted = apply_discount(price, discount)
    return discounted * (1 + vat_percent / 100)

print(final_price(10, 20, 20))



#
# 🧪 Задача 3 — Результат теста
# Есть функция count_correct(answers), которая возвращает число правильных ответов:
# def count_correct(answers):
#     return answers.count("OK")
# Напиши функцию test_result(answers, total_questions), которая:
# возвращает процент правильных
# возвращает строку "Сдано" если процент ≥ 70, иначе "Не сдано"
# Пример:
# answers = ["OK", "FAIL", "OK", "OK", "FAIL"]
# print(test_result(answers, 5))  # 60% → "Не сдано"

def count_correct(answers):
    return answers.count("OK")

def check_test_result(answers, total_questions):
    percent_correct = (count_correct(answers) / total_questions) * 100
    if percent_correct >= 70:
        return "Сдано"
    else:
        return "Не сдано"

answers = ["OK", "OK", "FAIL", "FAIL", "FAIL"]
print(check_test_result(answers, 5))



