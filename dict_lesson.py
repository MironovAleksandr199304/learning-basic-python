# ✅ Задача 1 — Маска email из словаря
# Дан словарь:
user = {
    "username": "sasha_qa",
    "email": "admin@example.com",
    "active": True
}

login,dmn = user["email"].split("@")
login = login[0] + "*" * (len(login) - 2) + login[-1]
masked_email = login + "@" + dmn

user["email"] = masked_email
print(user)

# Выведи email в маске, как "a***n@example.com":
#
# Оставь первую и последнюю буквы до @, остальное замени *
#
# Используй .split("@"), срезы, +, не replace
#
# ✅ Задача 2 — Проверка булевого значения
# Если active в словаре user = True, выведи "Пользователь активен"
# Иначе — "Пользователь не активен"
user = {
    "username": "sasha_qa",
    "email": "admin@example.com",
    "active": True
}

if user["active"]:
    print("Пользователь активен")
else:
    print("Пользователь не активен")

#
# ✅ Задача 3 — Удаление ключа и безопасный доступ
# Удалите ключ "email"
# Затем получите его через .get() — если нет, выведи "Email отсутствует"
user = {
    "username": "sasha_qa",
    "email": "admin@example.com",
    "active": True
}

del user["email"]

print(user.get("email", "Email отсутствует"))

#
# ✅ Задача 4 — Список ключей с True в другом словаре
# Есть фичи:
features = {
    "dark_mode": True,
    "beta_user": False,
    "multi_lang": True
}

for k,v in features.items():
    if v == True:
        print(k)
# Выведи список включённых фич (где значение True)
#
# ✅ Задача 5 — Обновление
# Есть:
profile = {
    "name": "Саша",
    "city": "Самара"
}

profile["city"] = "Санкт-Петербург"
profile["email"] = "test@sasha.ru"

print(profile)
# Обнови city до "Санкт-Петербург"
# Добавь "email": "test@sasha.ru"