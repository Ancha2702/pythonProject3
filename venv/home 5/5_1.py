"""Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

def tupl_sourse (str_soor: str):
    a, b, c = '\\'.join(str_source.split('\\')[:-1]), \
        str_source.split('\\')[-1].split('.')[0], \
        str_source.split('\\')[-1].split('.')[1]
    return a, b, c
str_source = 'C:\\Users\\user\\Documents\\python.py'
print(tupl_sourse(str_source))
