length = int(input('Кол-во чисел: '))
spisok = []

for index in range(length):
    print(f'{index + 1}-е число:', end=' ')
    number = int(input())
    spisok.append(number)

rev_spisok = []
rev_spisok.extend(spisok)
rev_spisok.reverse()

symm = 1
for i in range(len(spisok) - 1, 0, -1):
    point = int(spisok[len(spisok) - 1])
    if spisok[i - 1] == point:
        # print(f'цифры {len(spisok)} и {i} равны')
        symm += 1
    else:
        break

print(f'Последовательность: {spisok}')
# print('symm ', symm)
# print(f'Последовательность обратная: {rev_spisok}')

print(f'Нужно приписать чисел: {len(rev_spisok) - symm}')
print(f'Сами числа: {rev_spisok[symm:]}')
