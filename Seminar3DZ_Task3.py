# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114


list_float_numbers = [1.1, 1.2, 3.1, 5, 10.01]
max_fraction = 0
min_fraction = list_float_numbers[0]
for i in list_float_numbers:
    print(f'{i} ', end = '')
    if type(i)==float:
        string_object = str(i).split(".") 
        fractional_part = (f'0.{string_object[1]}')
        if max_fraction < float(fractional_part):
            max_fraction = float(fractional_part)
        if min_fraction > float(fractional_part):
            min_fraction = float(fractional_part)
difference = max_fraction - min_fraction
print(f'\nРазница между максимальной и минимальной дробной частями элементов: {difference}')