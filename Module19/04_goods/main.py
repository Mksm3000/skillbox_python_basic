goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

quant = 0
summ = 0
for key, value in goods.items():
    if value in store:
        for index in range(len(store[value])):
            quant += int(store[value][index]['quantity'])
            summ += int(store[value][index]['quantity']*store[value][index]['price'])
        print(f'{key} \t- {quant} шт., \tстоимость {summ} руб.')
        quant = 0
        summ = 0