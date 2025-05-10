# Валидатор логина и пароля
# Проверяет:
# - логин не короче 3 символов
# - пароль не короче 8 символов
# - логин и пароль не должны совпадать

def valid():
    while True:
        name = input("Введите логин: ")
        password = input("Введите пароль: ")

        if len(name) < 3:
            print("Логин должен быть длиннее 3 символов")
            continue
        elif len(password) < 8:
            print("Пароль должен быть длиннее 8 символов")
            continue
        elif name == password:
            print("Логин и пароль не должны совпадать")
            continue
        else:
            print("Регистрация прошла успешно.")
        break


# Запуск функции
valid()
