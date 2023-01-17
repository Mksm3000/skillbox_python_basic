import random

number = int(input('Количество палок: '))
shot = int(input('Количество бросков: '))
line = ['I' for i in range(number)]
#print(*line)

for i_shot in range(shot):
    min = random.randint(0, number - 2)
    max = random.randint(min + 1, number - 1)
#    print(f'\nmin: {min + 1}, max: {max + 1}')
    print(f'\nБросок {i_shot + 1}. Сбиты палки с номера {min + 1} по номер {max + 1}.')
    line = [('.' if min <= i <= max else line[i]) for i in range(number)]
    print(*line)
