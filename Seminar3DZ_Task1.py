# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list_size = int(input('Укажите количество элементов списка: '))
list = []
summa_even_numbers = 0
for i in range(list_size):
    list_number = int(input(f'Введите число {i+1}: '))
    list.append(list_number)
    if i % 2 != 0:
        summa_even_numbers += list[i]

print(list)
print(f'Сумма элементов списка на нечетных позициях равна {summa_even_numbers}')


