# ✅ Задача 1 — Доступ к вложенному полю
# Дан словарь:
user = {
    "username": "sasha_qa",
    "profile": {
        "email": "sasha@example.com",
        "city": "Самара"
    },
    "active": True
}

print(f"Email: {user['profile']['email']}, город: {user['profile']['city']}")
# Выведи:
# email пользователя
# город пользователя
# (оба поля находятся внутри "profile")

# ✅ Задача 2 — Проверка и вывод
# Проверь:
# если пользователь активен ("active": True)
# и у него есть "email" в "profile"
# → выведи: Почта подтверждённого пользователя: <email>
# Иначе: Нет данных
#
user = {
    "username": "sasha_qa",
    "profile": {
        "email": "sasha@example.com",
        "city": "Самара"
    },
    "active": True
}

if user["active"] and "email" in user["profile"]:
    print(f"Почта подтвержденного пользователя: {user['profile']['email']}")
else:
    print("Нет данных")


# ✅ Задача 3 — Обновление вложенного словаря
# Измени:
# "city" на "Санкт-Петербург"
# Добавь в "profile" ключ "telegram" со значением "@sasha_qa"

user = {
    "username": "sasha_qa",
    "profile": {
        "email": "sasha@example.com",
        "city": "Самара"
    },
    "active": True
}

user["profile"]["city"] = "Санкт-Петербург"
user["profile"]["telegram"] = "@sasha_qa"

print(user["profile"])

# 🧪 Массивы словарей: блок 1
# ✅ Задача 1 — Перебор и вывод
# Дан список:
users = [
    {"name": "Саша", "active": True},
    {"name": "Алина", "active": False},
    {"name": "Макс", "active": True}
]

for user in users:
    if user["active"]:
        print(f"Имя: {user['name']}")

# Выведи имена только активных пользователей.
#
# ✅ Задача 2 — Подсчёт
# Подсчитай, сколько пользователей всего и сколько из них активны.
# 📌 Вывод должен быть, например:
# Всего пользователей: 3
# Активных: 2

users = [
    {"name": "Саша", "active": True},
    {"name": "Алина", "active": False},
    {"name": "Макс", "active": True}
]
total_user = 0
active_user = 0

for user in users:
    total_user += 1
    if user["active"]:
        active_user += 1
print(f"Всего пользователей: {total_user}\nАктивных: {active_user}")
#думал сделать через .count() но что-то не пошло

#
# ✅ Задача 3 — Маскировка email
# Список пользователей:
users = [
    {"name": "Саша", "email": "sasha@example.com"},
    {"name": "Алина", "email": "alina@example.com"}
]

for user in users:
    login,dmn = user["email"].split("@")
    mask_login = login[0] + "*" * (len(login)-2) + login[-1]
    mask_email = mask_login + "@" + dmn
    user["email"] = mask_email
    print(user)

# Выведи:
# Имя: Саша, email: s***a@example.com
# Имя: Алина, email: a***a@example.com
# 📌 Логика маски — оставить первую и последнюю букву имени до @, остальное заменить *.



