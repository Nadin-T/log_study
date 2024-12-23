import os
import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='directory_info.log', filemode='w', encoding='utf-8')

# Определение namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def collect_directory_info(directory_path):
    if not os.path.isdir(directory_path):
        logging.error(f"Указанный путь не является директорией: {directory_path}")
        return

    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        parent_directory = os.path.basename(directory_path)

        if os.path.isdir(full_path):
            info = FileInfo(name=entry, extension='', is_directory=True, parent_directory=parent_directory)
            logging.info(f"Каталог: {info}")
        else:
            name, extension = os.path.splitext(entry)
            info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=parent_directory)
            logging.info(f"Файл: {info}")

if __name__ == "__main__":
    path = input("Введите путь до директории: ")
    collect_directory_info(path)
