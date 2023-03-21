import copy


def func(dikt, change, z_args):
    for key, value in dikt.items():
        if isinstance(value, str):
            for z_arg in z_args:
                if z_arg in value:
                    dikt[key] = value.replace(z_arg, change)
        elif isinstance(value, dict):
            sub_dikt = value
            for subb_key, subb_value in sub_dikt.items():
                func(subb_value, change, z_args)
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
result_total = dict()
zamena = ('телефон',)

while time:
    result = copy.deepcopy(site)
    brand = input('\nВведите название продукта для нового сайта: ')
    result_total[str(brand)] = func(result, brand, zamena)

    for name in result_total:
        print(name, result_total[name])
    print()
    zamena = list(zamena)
    zamena.append(brand)
    zamena = tuple(zamena)
#    print('zamena:', zamena)

    time -= 1
