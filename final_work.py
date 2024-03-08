# Задание №6
# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import os
import logging
import argparse
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='file_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Определение объекта namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_file_info(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            name, extension = os.path.splitext(item)
            file_info = FileInfo(name=name, extension=extension, is_directory=False,
                                 parent_directory=os.path.basename(directory))
            logging.info(f"File: {file_info}")
        elif os.path.isdir(item_path):
            file_info = FileInfo(name=item, extension='', is_directory=True,
                                 parent_directory=os.path.basename(directory))
            logging.info(f"Directory: {file_info}")
            get_file_info(item_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect information about files and directories.")
    parser.add_argument("directory_path",
                        help="Path to the directory to analyze. If the path contains spaces, enclose it in double quotes.")

    args = parser.parse_args()

    directory_path = args.directory_path
    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
        exit(1)

    get_file_info(directory_path)
