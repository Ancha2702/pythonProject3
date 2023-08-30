"""
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json
import csv
import pickle
import os
def convert_txt_to_json(txt_file, json_file):
    with open(txt_file, 'r', encoding='utf-8') as f, \
            open(json_file, "w", encoding='utf-8') as js_f:
        contents = f.readlines()
        my_dict = {}
        for el in contents:
            key, val = el.split("-")
            my_dict[key.title()] = float(val)
        json.dump(my_dict, js_f, separators=(',\n', ':'), ensure_ascii=False)

"""
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.

"""
def fun_dump_json():
    # name = input("введите имя:> ")
    # user_id = input("введите id:> ")
    # level = int(input('введите уровень доступа (1-7):> '))
    name = "Петя"
    user_id = "002"
    level = 4

    with open('task8_2.json', "r", encoding='utf-8') as f:
        res = json.load(f)

    my_dct = {
        "level": level,
        "id": user_id,
        "name": name,
    }

    with open('task8_2.json', "w", encoding='utf-8') as js_f:
        res.append(my_dct)
        json.dump(res, js_f, indent=2, separators=(',', ':'), ensure_ascii=False)
"""
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
def json_to_csv():
    with open('task8_2.json', "r", encoding='utf-8') as js_f:
        res = json.load(js_f)
        lst = []
        keys = res[0].keys()
        lst.append(keys)
        for el in res:
            vals = el.values()
            lst.append(vals)

    with open('task8_2.csv', "w", newline='', encoding='utf-8') as cs_f:
        writer = csv.writer(cs_f)
        for el in lst:
            writer.writerow(el)

"""
Задание №5
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
def find_json():
    for el in os.listdir():
        if el.endswith(".json"):
            with open(el, "r", encoding="utf-8") as j:
                res = json.load(j)
            path = ''.join(el.split(".")[:-1]) + ".pickle"
            with open(path, "wb") as p:
                pickle.dump(res,p)

"""
Задание №6
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
def pickle_to_csv():
    with open('new_json.pickle', 'rb') as f:
        data = pickle.load(f)

    with open("new_c.csv", "w", encoding="utf-8") as c:
        writer = csv.writer(c)
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    json_to_csv()
    #convert_txt_to_json('task7_3.txt', 'task8_1.json')