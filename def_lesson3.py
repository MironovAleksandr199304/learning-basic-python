#  Задача: parse_user_data
# У тебя есть строка с данными пользователя:
# "login=alex;email=alex@test.com;id=42"
# Нужно написать функцию:
# def parse_user_data(data_str): ...
# которая вернёт словарь:
# {
#   "login": "alex",
#   "email": "alex@test.com",
#   "id": "42"
# }
# ⚠️ Условия:
# поля могут быть в разном порядке;
# лишние пробелы — нужно убрать;
# если поле дублируется, оставить последнее значение;
# если строка пустая или без =, вернуть пустой словарь {}.
# 📌 Подсказки (не код!):
# Разбей по ; → получишь пары;
# Каждую пару разбей по =;
# Используй strip() — он тебе поможет;
# Можно копить данные в словарь — dict[key] = value.



def parse_user_data(data_str):
    data_str = data_str.replace(" ","").split(";")  #Разбей по ; → получишь пары;
    dict_user = {}
    for pair in data_str:
        key_value = pair.split("=")
        if len(key_value) == 2:
            key,value = key_value
            dict_user[key] = value
        else:
            continue
    return dict_user
print(parse_user_data("login=alex;email=alex@test.com;id=42"))
