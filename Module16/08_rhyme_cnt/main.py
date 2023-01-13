def who_out(list, count, index_start):
    length = len(list)
    index_out = (index_start + count - 1) % length
    return index_out


people = int(input('Кол-во человек: '))
count = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {count}-й человек')

spisok = list(range(1, people + 1))

i = 0
while len(spisok) > 1:
    print(f'\nТекущий круг людей: {spisok}')
    if i >= len(spisok):
        i = i % len(spisok)
    # print('i', i)
    # print('len(spisok)', len(spisok))
    print(f'Начало счёта с номера {spisok[i]}')
    delete = int(who_out(spisok, count, i))  # индекс удаляемого числа
    print(f'Выбывает человек под номером {spisok[delete]}')
    i = delete
    spisok.pop(delete)

print(f'\nОстался человек под номером {int(spisok[0])}')
