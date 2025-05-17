# Вставь "X" после каждого второго элемента в списке

nums = [1,2,3,4,5,6]

i = 2

while i < len(nums):            #вот тут я застрял. сделал только с подсказкой чата гпт
    nums.insert(i, "X")
    i += 3
print(nums)

#
# Создай список a = [1, 2, 3], копируй его и очисти a — покажи, что копия осталась

a = [1, 2, 3]
b = a.copy()
a.clear()

print(f"Звенящий пустотой первый список: {a}")
print(f"Его преемник: {b}")

#
# Сделай список из квадратов чисел от 1 до 10 (через list comprehension)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadro_nums = [x ** 2 for x in nums] #понял, я думал list comprehension это метод, а это просто стиль записи списка

print(quadro_nums)

#
# Отфильтруй чётные числа из [1, 2, 3, ..., 20] в новый список

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
filter_nums = []

for num in range(1,len(nums)):
    if num % 2 == 0:
        filter_nums.append(num)
print(filter_nums)

#
# Удали все "банан" из списка ["яблоко", "банан", "груша", "банан"]

fruits = ["яблоко", "банан", "груша", "банан"]

for fruit in fruits[:]:
    if fruit == "банан":
        fruits.remove(fruit)
print(fruits)


#
# Создай копию списка, разверни её и выведи оба списка

nums = [1, 2, 3, 4, 5, 6]
copy_nums = nums.copy()
copy_nums.reverse()

print(f"Неповторимый оригинал: {nums}")
print(f"Попытка импортзамещения задом наперед: {copy_nums}")