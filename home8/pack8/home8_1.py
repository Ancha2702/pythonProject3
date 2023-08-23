"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import os
import json
import csv
import pickle

def get_size(path):
    total_size = 0
    for dir_path, dir_names, file_names in os.walk(path):
        for file in file_names:
            fp = os.path.join(dir_path, file)
            total_size += os.path.getsize(fp)
    return total_size


def go_dir(dir_path):
    res = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            res.append({"parent_directory": root,
                        "object_type": 'File',
                        "name": name,
                        "size_in_bytes": os.path.getsize(full_path)})

        for name in dirs:
            full_path = os.path.join(root, name)
            res.append({"parent_directory": root,
                        "object_type": 'Directory',
                        "name": name,
                        "size_in_bytes": get_size(full_path)})
    return res

results = go_dir('C:\\Users\\user\\PycharmProjects\\pythonProject3\\home8\\pack8\\')

with open('home8.json', 'w', encoding='utf-8') as js_f:
    json.dump(results, js_f, indent=2)

with open("home8.csv", 'w', newline='', encoding='utf-8') as csv_f:
    writer = csv.DictWriter(csv_f, fieldnames=results[0].keys(), delimiter='|')
    writer.writeheader()
    writer.writerows(results)

with open("home8.pickle", 'wb') as pcl_f:
    pickle.dump(results, pcl_f)
