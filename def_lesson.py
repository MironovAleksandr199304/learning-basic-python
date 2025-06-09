# 🧪 Задачи на функции — уровень 1
# ✅ Задача 1 — Приветствие
# Напиши функцию greet(name), которая возвращает строку:
# "Привет, <name>!"
# Пример:
# print(greet("Саша"))  # Привет, Саша!
def greet(name):
    return f"Привет, {name}!"
print(greet("Саша"))
# ✅ Задача 2 — Сумма двух чисел
# Напиши функцию add(a, b), которая возвращает сумму двух чисел.
# Пример:
# print(add(3, 5))  # 8
def add(a,b):
    return a+b
print(add(3,5))
# ✅ Задача 3 — Проверка чётности
# Напиши функцию is_even(n), которая возвращает True, если число чётное, и False в противном случае.
# Пример:
# print(is_even(4))  # True
# print(is_even(7))  # False
def is_even(n):
    return n%2 == 0
print(is_even(7))
# ✅ Задача 4 — Сравнение двух чисел
# Напиши функцию compare(a, b), которая:
# возвращает 'Равно', если a == b
# 'Больше', если a > b
# 'Меньше', если a < b
def compare(a,b):
    if a == b:
        return "Равно"
    elif a > b:
        return "Больше"
    else:
        return "Меньше"
print(compare(6,6))
# ✅ Задача 5 — Количество символов
# Напиши функцию count_chars(text), которая возвращает длину строки без пробелов.
# Пример:
# print(count_chars("Саша учит Python"))  # 15

def count_chars(text):
    text = text.replace(" ","")
    return len(text)
print(count_chars("Саша учит Python"))

# 🧪 Задачи на функции — уровень 2
# ✅ Задача 6 — Квадрат числа
# Напиши функцию square(n), которая возвращает квадрат числа.
# Пример:
# print(square(5))  # 25
def square(n):
    return n**2
print(square(7))

# ✅ Задача 7 — Первая буква в верхнем регистре
# Напиши функцию capitalize_first(text), которая возвращает строку с заглавной первой буквой (только первая буква, остальное не трогай).
# Пример:
# print(capitalize_first("python"))  # Python
# print(capitalize_first("саша"))    # Саша
def capitalize_first(text):
    return text[0].upper() + text[1:].lower() if text else ""
print(capitalize_first("PYTHON"))
print(capitalize_first("Саша"))
#
# ✅ Задача 8 — Подсчёт гласных
# Напиши функцию count_vowels(text), которая возвращает количество гласных букв в строке. Считай только русские гласные: а, е, ё, и, о, у, ы, э, ю, я (регистр не важен).
# Пример:
# print(count_vowels("Саша учит Питон"))  # 6
def count_vowels(text):
    gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    count_gls = 0
    for char in text:
        if char.lower() in gls:
            count_gls += 1
    return count_gls
print(f"Всего гласных: {count_vowels("Саша учит Питон")}")

# ✅ Задача 9 — Проверка пароля
# Напиши функцию check_password(password), которая возвращает:
# 'Слабый', если пароль короче 8 символов
# 'Средний', если длина ≥8, но в нём нет цифр
# 'Сильный', если длина ≥8 и есть хотя бы одна цифра
# Подсказка: any(char.isdigit() for char in password)

def check_password(password):
    if len(password) < 8:
        return "Слабый"
    elif any(char.isdigit() for char in password):
        return "Сильный"
    else:
        return "Средний"
print(check_password("qwertyqwerty1"))

#
# ✅ Задача 10 — Калькулятор скидки
# Напиши функцию apply_discount(price, discount), которая возвращает цену с учётом скидки в процентах.
# Пример:
# print(apply_discount(1000, 20))  # 800.0

def apply_discount(price, discount):
    disc_price = price * (1 - discount/100)
    return disc_price
print(f"Ваша цена с учетом скидки: {apply_discount(10000,20)}")
