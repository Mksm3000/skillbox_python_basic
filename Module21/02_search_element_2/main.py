def find(struct, key, depth):
    if key in struct:
        return struct[key]

    while depth >= 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find(sub_struct, key, depth)
                if result:
                    break
        else:
            result = None
        depth -= 1
        return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

user_key = input('\nИскомый ключ: ')
user_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()
max_depth = 100
if user_depth == 'n':
    max_depth = max_depth
elif user_depth == 'y':
    max_depth = int(input('Введите максимальную глубину: '))

value = find(site, user_key, max_depth)

if value:
    print(f'Значение ключа: {value}')
else:
    print('Упс! Такого ключа в структуре сайта нет.')

# Пример 1:
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: n
# Значение ключа: {'title': 'Мой сайт'}
#
# Пример 2:
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: y
# Введите максимальную глубину: 1
# Значение ключа: None
