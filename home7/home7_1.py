"""Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
from pathlib import Path
import os

def sort_f(directory: str) -> None:
    extensions = {
        'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg',
                  'mpeg', 'm4v',
                  'h264', 'flv', 'rm', 'swf', 'vob'],

        'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb',
                 'sav',
                 'tar', 'xml'],

        'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa',
                  'wma', 'wpl',
                  'cda'],

        'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg',
                  'tif',
                  'tiff'],
        'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

        'exe': ['exe'],
    }

    res = [file.split('.') for dirs, folders, files in os.walk(directory) for
             file in files]

    for (name, expan) in res:
        for k, v in extensions.items():
            if expan in v:
                new_dir = Path().cwd() / directory / k
                if new_dir.is_dir():
                    old_dir = Path(directory) / f'{name}.{expan}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{expan}')
                else:
                    Path(new_dir).mkdir(parents=True)
                    old_dir = Path(directory) / f'{name}.{expan}'
                    old_dir = old_dir.replace(new_dir / f'{name}.{expan}')

    sort_f('directory_for_sort', extensions)