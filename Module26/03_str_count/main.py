import os
from collections.abc import Iterable


def counter() -> Iterable[str]:
    os.chdir('..')
    my_path = os.getcwd()
    print(f'\nПерешли (на 1 уровень выше) в родительскую директорию: {my_path}\n')

    for root, dirs, files in os.walk(my_path):
        for name in files:
            if name.endswith('.py'):
                print(f'\n{root}{os.sep}{name}')
                with open(root + os.sep + name, encoding='utf8') as data:
                    count = 0
                    for line in data:
                        line = line.rstrip('\n')
                        if len(line) != 0  and not line.startswith('#'):
                            count += 1
                    yield f'В файле {count} строк(и).'


result = counter()
for i in result:
    print(i)
