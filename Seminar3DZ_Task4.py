# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

user_number = int(input('Введите число: '))
binary = ''
while user_number > 0:
    binary = str(user_number%2) + binary
    user_number = user_number // 2
print(binary)