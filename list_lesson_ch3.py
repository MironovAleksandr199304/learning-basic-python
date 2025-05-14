# 🔸 Задача 1: Все числа без повторов, отсортированные по убыванию
# nums = [2, 4, 2, 7, 9, 7, 3, 4]
nums = [2, 4, 2, 7, 9, 7, 3, 4]
unique_nums = []

for num in nums:
 if num not in unique_nums:
     unique_nums.append(num)
unique_nums = sorted(unique_nums, reverse=True)
print(unique_nums)

# # Получи список уникальных чисел в порядке убывания
# # Результат: [9, 7, 4, 3, 2]
# 🔸 Задача 2: Найти второй по величине элемент
# nums = [12, 5, 7, 23, 19, 23]
# # Найди второй максимум без использования sort()
nums = [12, 5, 7, 23, 19, 23]
max1 = 0
max2 = 0

for num in nums:
    if num > max1:
        max1 = num #23
for num in nums:
    if num < max1:
        max2 = num
print(max2)
# 💡 Что нужно:
# Найти максимум
# Затем снова пройтись и найти второй максимум, не равный первому
# 📌 Подумай: сначала max1, потом снова проход → if num < max1 and num > max2.

# 🔸 Задача 3: Переместить все 0 в конец списка
# nums = [0, 2, 0, 5, 0, 1, 9, 0]
# # Получи: [2, 5, 1, 9, 0, 0, 0, 0]
# # Порядок других чисел сохранить
nums = [0, 2, 0, 5, 0, 1, 9, 0]
sort_nums = []

for num in nums:
    if num != 0:
        sort_nums.append(num)

print(sort_nums)

# 🔸 Задача 4: Разделить список на чётные и нечётные
# nums = [3, 8, 5, 12, 7, 6, 9]
# # Сформируй два списка: evens и odds
nums = [3, 8, 5, 12, 7, 6, 9]
even = []
odds = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    elif num % 2 != 0:
        odds.append(num)
print(even)
print(odds)

# 🔸 Задача 5: Найти повторяющиеся элементы
# words = ["кот", "пёс", "кот", "рыба", "пёс", "слон", "кот"]
# # Выведи все элементы, которые встречаются больше одного раза (один раз в списке)
# # Результат: ['кот', 'пёс']
words = ["кот", "пёс", "кот", "рыба", "пёс", "слон", "кот"]
unique_words = []
second_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)
    elif word in words and word in unique_words and word not in second_words:
        second_words.append(word)

print(words)
print(unique_words)
print(second_words)
