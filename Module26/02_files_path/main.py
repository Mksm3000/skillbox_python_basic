# Реализуйте функцию `gen_files_path`, которая рекурсивно проходит по всем каталогам
# указанной директории (по умолчанию — корневой диск), находит указанный пользователем каталог и
# генерирует пути всех встреченных файлов.

import os

my_path = os.path.abspath(os.path.join(os.path.sep))

target = 'PycharmProjects'
print(f'Ищем директорию с именем "{target}"\n')


def gen_files_path():
    for root, dirs, files in os.walk(my_path):
        print(root)
        for name in dirs:
            if name == target:
                return print(f'\nДиректория "{target}" найдена по адресу "{root}"')


gen_files_path()
