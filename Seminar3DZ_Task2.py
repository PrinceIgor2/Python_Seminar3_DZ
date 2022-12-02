# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

list_size = int(input('Укажите количество элементов списка: '))
random_list = []
multiple_pairs_list = []

for i in range(list_size):
    random_list.append(randint(0, 19))

for i in range(len(random_list)):
    while i < len(random_list)/2 and list_size > len(random_list)/2:
        list_size = list_size - 1
        temp = random_list[i] * random_list[list_size]
        multiple_pairs_list.append(temp)
        i += 1

print(random_list)
print(multiple_pairs_list)