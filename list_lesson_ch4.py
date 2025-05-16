# Блок 1: 5 лёгких задач (разминка)
# Создай список чисел от 1 до 5 и добавь в него 6 с помощью .append()
nums = [1,2,3,4,5]
nums.append(6)
print(nums)

#
# Создай список слов и вставь "привет" в начало с помощью .insert()
word = ["Огурец", "Тайланд это круто", "Хочу быть крутым спецом"]
word.insert(0,"привет")
print(word)
# Удали из списка значение 10 с помощью .remove()
nums = [1,2,3,4,5,6,7,8,9,10]
nums.remove(10)
print(nums)

#
# Используй .pop() без аргументов на списке [1, 2, 3] — выведи удалённый элемент
nums = [1,2,3]
x = nums.pop() #вроде удаляет последний элемент, верно?
print(nums) #да, верно
#
# Разверни список [1, 2, 3, 4, 5] с помощью .reverse() и выведи результат
nums = [1,2,3,4,5]
nums.reverse() #а почему nums = nums.reverse() возвращает none?
print(f"Развернутый список: {nums}")
#
# 🧠 Блок 2: 5 задач средней сложности (логика + методы)
# Вставь 0 в середину списка [1, 2, 3, 4]
nums = [1, 2, 3, 4]
x = 0

for num in nums:
    x += 1
    if x == 2:
        nums.insert(2,2)
print(nums)


#
# Создай список ["яблоко", "банан", "яблоко", "груша"], удали только первое "яблоко"
fruits = ["яблоко", "банан", "яблоко", "груша"]

for fruit in fruits:
    if fruit == "яблоко" and fruits.count(fruit) == 2:
        fruits.remove(fruit)
print(fruits)

#
# Получи копию списка [5, 6, 7], удали из копии 6, и выведи оба списка
nums = [5, 6, 7]
nums_copy = nums.copy()
nums.remove(6)

print(f"Неповторимый оригинал: {nums}")
print(f"Жалкая пародия: {nums_copy}")

#
# Отсортируй [9, 3, 6, 1] в порядке убывания без sorted()
nums = [9, 3, 6, 1]

#так я пока решал предыдущей очень замудренной и ненужной логикой, понял что тут намного легче все. просто .pop() сохраняем тройку
#потом инсертом ее вставляем.
for num in nums:
    if num == 6: #вот тут интересно. я изначально ставил условие num==3, но тогда список вел себя неадекватно при инсерте
        x = nums.pop(1)
        nums.insert(2,x)
print(nums)

#
# Подсчитай, сколько раз "да" встречается в списке ["да", "нет", "да", "да"] с .count()
answers = ["да", "нет", "да", "да"]
print(answers.count("да"))
#
# 🔁 Блок 3: 5 задач на повторение вчерашнего
# Найди второй максимум в [10, 22, 9, 22, 18] (без sort())
nums = [10, 22, 9, 22, 18]
max_num1 = max(nums)
max_num2 = -1

for num in nums:
    if num < max_num1 and num > max_num2: #интересно почему не отрабатывает если if max_num1 < num > max_num2?
        max_num2 = num
print(max_num2)

#
# Раздели [4, 7, 10, 15, 2] на чётные и нечётные списки
nums = [4, 7, 10, 15, 2]
even_nums = []
odd_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    elif num % 2 != 0:
        odd_nums.append(num)
print(even_nums)
print(odd_nums)

#
# Удали все 0 из [0, 3, 0, 4, 5, 0] и добавь их в конец
nums = [0, 3, 0, 4, 5, 0]

for num in nums[:]: #я понимаю in nums[:-1] - это последний элемент, пониманию [:2] -срез, а [:] что значит?
    if num == 0:
        nums.remove(0)
        nums.append(0)
        continue
print(nums)

#
# Получи список уникальных чисел из [4, 4, 7, 8, 4, 7] в порядке убывания
nums = [4, 4, 7, 8, 4, 7]
unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)
unique_nums.sort(reverse=True)
print(unique_nums)

#
# Найди все слова, которые повторяются более одного раза в списке ["мир", "война", "мир", "покой", "война"]

words = ["мир", "война", "мир", "покой", "война"]
unique_words = []
second_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)
    elif word in unique_words and word in words and word not in second_words:
        second_words.append(word)
print(second_words)

#
# 🧱 Блок 4: 5 задач на методы списка (сегодняшняя тема)
# Используй .index() чтобы найти позицию "груша" в списке ["яблоко", "банан", "груша", "слива"]

fruits = ["яблоко", "банан", "груша", "слива"]

print(fruits.index("груша"))

#
# Создай список ["а", "б", "в"], скопируй его, очисти оригинал — покажи, что копия осталась
words = ["а", "б", "в"]
copy_words = words.copy()

for word in copy_words:
    if word in words:
        words.remove(word)

print(copy_words)
print(words)


#
# Создай список, вставь "X" после каждого второго элемента с .insert() (без счётчиков)

nums = [1,2,3,4,5]

for num in range(len(nums)):
    if num % 2 == 0:
        nums.insert(2, 'X')
print(nums) #застрял. я понял как решить ее со счетчиком, но без него не понимаю


#
# Отсортируй список строк ["кит", "акула", "дельфин"] по алфавиту
words = ["кит", "акула", "дельфин"]
words.sort()
print(words)

#
# Удали последний элемент из списка и выведи его значение (с .pop())
words = ["кит", "акула", "дельфин"]
x = words.pop(-1)
print(x)