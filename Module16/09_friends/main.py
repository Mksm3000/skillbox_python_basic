friends = int(input('Кол-во друзей: '))
debt_count = int(input('Долговых расписок: '))

friends_list = []
for _ in range(friends):
    friends_list.append(0)
#print(friends_list)

for i in range(debt_count):
    print(f'{i + 1}-я расписка')
    print(f'Кому:', end=' ')
    index_to = int(input())
    print(f'От кого:', end=' ')
    index_from = int(input())
    print('Сколько:', end=' ')
    debt = int(input())

    data_plus = int(friends_list[index_to - 1]) + debt
    friends_list.pop(index_to - 1)
    friends_list.insert(index_to - 1, data_plus)

    data_minus = int(friends_list[index_from - 1]) - debt
    friends_list.pop(index_from - 1)
    friends_list.insert(index_from - 1, data_minus)

#    print(f'Баланс друзей: {friends_list}')

print(f'\nБаланс друзей:')
for i, char in enumerate(friends_list):
    print(f'{i + 1} : {char}')