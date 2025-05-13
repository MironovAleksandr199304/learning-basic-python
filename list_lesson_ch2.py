
# 🔹 Сумма всех чисел от 1 до 10
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for i in nums:
    result += i
print(result)

# 🔹 Удаление всех 5-к из списка
nums = [2, 5, 4, 5, 3, 5, 1]
while 5 in nums:
    nums.remove(5)
print(nums)

# 🔹 Поиск max и min вручную
nums = [13, 8, 21, 3, 17, 0, 44, -1]
min_num = nums[0]
max_num = nums[0]
for num in nums:
    if num < min_num:
        min_num = num
    else:
        max_num = num
print(min_num, max_num)

# 🔹 Сравнение первого и последнего элемента
colors = ["красный", "зелёный", "синий", "красный"]
first_color = colors[0]
last_color = colors[-1]
if first_color == last_color:
    print("Одинаковые")
else:
    print("Разные")

# 🔹 Перебор по значениям и по индексам
cities = ["Москва", "Питер", "Казань", "Томск"]
for city in cities:
    print(city)
for city in range(len(cities)):
    print(cities[city])

# 🔹 Поиск индекса "Кирилл" вручную
names = ["Андрей", "Оля", "Кирилл", "Женя"]
for name in range(len(names)):
    if names[name] == "Кирилл":
        print(name)

# 🔹 Подсчёт "ок" вручную
feedback = ["ок", "не ок", "ок", "ок", "не ок", "ок", "не ок"]
result = 0
for answer in range(len(feedback)):
    if feedback[answer] == "ок":
        result += 1
print(result)

# 🔹 Индекс "груша" вручную
fruits = ["яблоко", "банан", "груша", "слива"]
for fruit in range(len(fruits)):
    if fruits[fruit] == "груша":
        print(fruit)

# 🔹 Сортировка списка по возрастанию
nums = [10, 3, 7, 1, 9]
nums.sort()
print(nums)

# 🔹 Уникальные слова
words = ["кот", "пёс", "кот", "рыба", "пёс"]
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print(unique_words)
