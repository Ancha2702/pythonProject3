"""Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
+ При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
import os


def group_rename(res_name: str, len_number: int, start_exp: str, final_exp: str,
                 old_name: list[int, int], work_dir=os.getcwd()):
    count = 1
    start_letter, end_letter = old_name
    for dirs, folders, files in os.walk(work_dir):
        for i, file in enumerate(files):
            if file.endswith(start_exp):
                old_name = os.path.join(dirs, file)
                new_name = (f'{dirs}\\{file[start_letter:end_letter]}{res_name}'
                            f'{str(count).zfill(len_number)}.{final_exp}')
                os.rename(old_name, new_name)
                count += 1


group_rename('file', 3, 'xls', 'pdf', [0, 2], 'Test7')
