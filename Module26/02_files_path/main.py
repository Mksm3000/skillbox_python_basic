# Реализуйте функцию `gen_files_path`, которая рекурсивно проходит по всем каталогам
# указанной директории (по умолчанию — корневой диск), находит указанный пользователем каталог и
# генерирует пути всех встреченных файлов.

import os
import time
from collections.abc import Iterable


def gen_files_path(my_path: str, target: str) -> Iterable[str]:
    for directory, folders, files in os.walk(my_path):
        if target == directory:
            break
        for file in files:
            yield os.path.join(directory, file)


root_path = os.path.abspath(os.path.join(os.path.sep))

dir_name = 'PycharmProjects'
print(f'\nИщем директорию "{dir_name}".')

for directory, folders, files in os.walk(root_path):
    if dir_name in folders:
        print('Да, такая директория существует', end='')

        dir_path = os.path.join(directory,dir_name)
        print(f'"{dir_path}"\n')

        # чтобы успеть увидеть комментарий с адресом
        time.sleep(2)

        data = gen_files_path(root_path, dir_path)

        for element in data:
            print(element)
