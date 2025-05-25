# ✅ Задача 1 — Маска email из лога
# Есть строка:
# log = "[2025-06-01 14:22] User: mironovAV, Email: admin@site.ru, Action: login"
# 🔹 Нужно:
# Выделить email (без регулярных выражений)
# Замаскировать его:
# оставить первую и последнюю буквы имени
# остальное до @ — заменить на *
# Вывести строку:
# Email: a***n@site.ru
# ⚠️ Ограничения:
# Никаких re
# Только split, find, replace, срезы
# Код желательно компактный, но без костылей

log = "[2025-06-01 14:22] User: mironovAV, Email: admin@site.ru, Action: login"

first_step = log.split(" ")
masked_mail = first_step[5]
name,dmn = masked_mail.split("@")
masked_name = name[0] + "*" * (len(name)-2) + name[-1]
result = first_step[4] + " " + masked_name + "@" + dmn.replace(",","")
print(result)

# ✅ Задача 2 — Проверка и извлечение из строки
# 💼 Представь, что ты валидируешь входной лог из внешней системы.
# Есть строка:
# log = "user: MironovAV | email: admin@site.ru | id: 104"
# 🔹 Твоя задача:
# Убедиться, что все три поля есть: user, email, id
# Проверить, что id — это только цифры
# Если всё ок — вывести имя пользователя и замаскированный email (оставить первую и последнюю буквы)
# Если что-то не так — вывести "Ошибка в логе"
# 🧠 Пример корректного вывода:
# User: MironovAV, Email: a***n@site.ru
# 📌 Никаких re, только split, in, isdigit(), startswith() и срезы

log = "user: MironovAV | email: admin@site.ru | id: 104"


#первая проверка, что в строке лога есть user,email и id
if "user" in log and "email" in log and "id" in log: #если в логе есть все три поля, тогда след шаг
    parts = log.split(" | ") #разбиваем на список по разделителю |
    #разбиваем 2 индекс с id
    check_id = parts[2].split(": ") #тут получается я захардкодил под текущую задачу, не универсально
    #проверяем, что 1 индекс check_id содержит только цифры
    if check_id[1].isdigit():
        #если да, то разбиваем part[1]
        parts_email = parts[1].split(": ")
        #разбиваем masked_email на name,domen
        name,domen = parts_email[1].split("@")
        #маскируем name
        name = name[0] + "*" * (len(name) - 2) + name[-1]
        #собираем email
        masked_email = parts_email[0].capitalize() + " " + name + "@" + domen
        #собираем полную строку
        masked_log = parts[0] + ", " + masked_email
    #возвращаем ошибку если id содержит не только цифры
    else:
        print("Ошибка в логе")
#возвращаем ошибку, если не все поля присутствуют
else:
    print("В логе не хватает данных. Настрой запись в логи нормально, плз")
print(masked_log)

# 🐞 Задача 3 — Валидация и защита от кривых логов
# Тебе пришёл лог от внешнего подрядчика:
# log = "user: , email: g!root$@nasa.gov, id: 10a4"
# 🔹 В чём проблема:
# user — пустой (вообще ничего)
# email — странный, с символами !, $
# id — содержит буквы
# 🔹 Что нужно сделать:
# Проверить, что все поля присутствуют (user, email, id)
# Убедиться:
# user не пустой
# email содержит @, имя до @ не короче 2 букв, и только латиница
# id содержит только цифры
# Если всё ок — маскируем email (оставить 1 и последнюю буквы имени, остальное — *)
# Если есть проблемы — вывести "Лог повреждён" и указать, что не так
# 📌 Пример вывода:
# Лог повреждён: id содержит нецифровые символы, user пустой, email некорректен
# 📌 Можно собрать ошибки в список и вывести все разом, а можно по ходу.
# 🛠 Что тебе можно использовать:
# split, in, strip, isdigit, isalpha
# .split("@"), .startswith(), .endswith(), .join()

log = "user: , email: g!root$@nasa.gov, id: 10a4"

if "user" in log and "email" in log and "id" in log:
    #разбиваем log для последующих разбитий и проверок
    parts_log = log.split(",")
    #разбиваем user на usr,usr_name
    usr, usr_name = parts_log[0].split(": ")
    #проверка, что указан юзер
    if usr_name.isalpha():
        #если логин указан, проверяем дальше
        #разбиваем email на две части
        parts_email = parts_log[1].split(": ")
        if "@" in parts_email: #проверка, что @ есть в емейле
            name,domen = parts_email.split("@")
            if len(name) > 2:
                if name.isascii() and name.isalpha(): #изначально было решено через if name.search(r'[A-Za-z]'), после ревью поменял
                    #разбиваем id: 10a4 на id и value
                    col_id, id_value = parts_log[2].split(": ")
                #проверяем, что id_value состоит только из цифр
                    if id_value.isdigit(): #если все проходит, маскируем name и собираем строку с email
                        masked_name = name[0] + "*" * (len(name)-2) + name[-1]
                        masked_email = masked_name + "@" + domen
                        print(masked_email)
                    else:
                        print(f"Лог поврежден, в поле {col_id} не могут присутствовать символы: {id_value}")
                else:
                    print(f"Лог поврежден. В логине почты присутствуют символы: {name}")
            else: print(f"Длина логина меньше 2 символов: {name}")
        else: print(f"Лог поврежден. В почте отсутствуют символ '@': {parts_email}")
    else: print(f"Лог поврежден. Не указан user: '{usr_name}'")
else:
    print(f"Лог поврежден. В логе отсутствует одно из полей: user/email/id")