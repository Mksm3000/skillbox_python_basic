import copy


def func(dikt, word, change):
    for key, value in dikt.items():
        if isinstance(value, str):
            if word in value:
                dikt[key] = value.replace(word, change)
        elif isinstance(value, dict):
            sub_dikt = value
            for sub_key, sub_value in sub_dikt.items():
                func(sub_value, word, change)
    return dikt


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

time = int(input('\nСколько сайтов: '))

while time:
    search = input('\nКакое слово ищем для замены? ')
    brand = input('Введите название продукта для нового сайта: ')
    result = func(copy.copy(site), search, brand)

    for key, value in result.items():
        if isinstance(value, dict):
            print(key)
            for sub_key, sub_value in value.items():
                print(sub_key, sub_value)
        else:
            print(key, value)

    time -= 1