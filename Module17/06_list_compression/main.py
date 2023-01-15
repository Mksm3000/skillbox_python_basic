import random

number = int(input('Количество чисел в списке: '))
spisok = [random.randint(0, 2) for index in range(number)]
print(f'Список до сжатия: {spisok}')

for i in spisok:
    if i == 0:
        spisok.remove(0)
        spisok.append(0)
print(f'Список до сжатия после перестановки нулей: {spisok}')

spisok = spisok[:spisok.index(0)]
print(f'Список после сжатия: {spisok}')
