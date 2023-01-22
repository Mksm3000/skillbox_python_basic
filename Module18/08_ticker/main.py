def shift_compare(list_1, list_2):
    index = list_2.index(list_1[0],)
#    print('index', index)
    for _ in range(len(list_2)-index):
        tail = list_2[len(list_2)-1]
#        print('tail', tail)
        list_2.pop(len(list_2)-1)
        list_2.insert(0, tail)
#        print('list_2', list_2)
    if list_1 == list_2:
        return index


first = list(input('Первая строка: '))  # qwerty
second = list(input('Вторая строка: '))  # rtyqwe
result = shift_compare(first, second)

if result is None:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    print(f'\nПервая строка получается из второй со сдвигом {result}.')