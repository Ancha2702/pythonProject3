"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.
"""

number = int(input("Введите число: "))
hexi = " "
DIVIDER = 16

print('Проверка с помощью hex():', hex(number))

while number >= 1:
    result = number % DIVIDER
    if result == 10:
        result = 'a'
    elif result == 11:
        result = 'b'
    elif result == 12:
        result = 'c'
    elif result == 13:
        result = 'd'
    elif result == 14:
        result = 'e'
    elif result == 15:
        result = 'f'
    hexi = str(result) + hexi
    number = number // DIVIDER

print('Число в шестнадцатеричной системе:', hexi)
