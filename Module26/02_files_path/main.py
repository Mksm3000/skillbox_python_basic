# Реализуйте функцию `gen_files_path`, которая рекурсивно проходит по всем каталогам
# указанной директории (по умолчанию — корневой диск), находит указанный пользователем каталог и
# генерирует пути всех встреченных файлов.

import os
from collections.abc import Iterable


def gen_files_path(my_path: str, target: str) -> Iterable[str]:
    print(f'\nСписок файлов в директории "{target}":\n')
    for root, dirs, files in os.walk(my_path):
        for direct in dirs:
            for file in files:
                if target in root:
                    yield f'{root}\\{direct}\\{file}'


root_path = os.path.abspath(os.path.join(os.path.sep))
dir_name = 'Python_Basic\Module'

for element in gen_files_path(root_path, dir_name):
    print(element)
