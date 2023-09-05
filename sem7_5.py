"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""
import os
from string import ascii_lowercase
from random import choices
from random import randint
from random import randbytes


def func(ext, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096, files=42):
    for i in range(files):
        name = ''.join(choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        size = randint(min_rand_bytes, max_rand_bytes)
        with open(name, 'wb') as f:
            f.write(randbytes(size))


func('.txt')

def func_2(files=10, **kwargs):
    dct = kwargs
    val = []
    for k, v in dct.items():
        val.append(v)
    for i in range(files):
        ext = str(*choices(val))
        func(ext, files=1, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096)


print(func_2(5, a='.txt', b='.doc', c='.exe'))
"""Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
def func_3(dir):
    my_path = os.getcwd() + dir
    try:
        os.makedirs(my_path)
        os.chdir(my_path)
    except FileExistsError:
        os.chdir(my_path)
    func_2(5, a='.txt', b='.doc', c='.exe')
    os.chdir('..')


func_3('\\task6')