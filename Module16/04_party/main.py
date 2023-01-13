guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
status = ''

while status != 'Пора спать':
    print(f'Сейчас на вечеринке {len(guests)} человек(а): {guests}')
    status = input('Гость пришёл или ушёл? ')
    if status == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            print(f'Привет, {name}!')
            guests.append(name)
        else:
            print(f'Прости, {name}, но мест нет.')
    elif status == 'ушёл':
        name = input('Имя гостя: ')
        if name in guests:
            guests.remove(name)
        else:
            print(f'Прости, но гостя {name} у нас нет.')
print('Вечеринка закончилась, все легли спать.')