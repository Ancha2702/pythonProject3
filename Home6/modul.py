"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def dat(st):
    day, month, year = map(int, (st.split(".")))
    if year in range(1, 10000) and month in range(1, 13) and day in range(1, 32):
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 and month == 2:
            if day <= 29:
                return True
            else:
                return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day <= 31:
                return True
            else:
                return False
        elif month == 2:
            if 1 <= day <= 28 + is_leap_year(year):
                return True
            else:
                return False
        else:
            if day <= 30:
                return True
            else:
                return False
    else:
        return False


print(dat("28.02.1999"))
