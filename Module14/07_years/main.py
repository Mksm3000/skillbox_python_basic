print('Задача 7. Годы\n')

# Что нужно сделать
# Недавно Костя прочитал научно-фантастическую книгу.
# В ней самые страшные события случались только тогда, когда в году были три одинаковые цифры.
# Косте стало интересно, какие годы были или будут «особенными» в определённом промежутке.
# Напишите программу, в которой у пользователя запрашивается два четырёхзначных числа A и B.
# Затем выведите в порядке возрастания все четырёхзначные числа в интервале от A до B,
# запись которых содержит ровно три одинаковые цифры.
#
# Пример работы программы:
# Введите первый год: 1900
# Введите второй год: 2100
# Годы от 1900 до 2100 с тремя одинаковыми цифрами:
# 1911
# 1999
# 2000
# 2022

def three(n):
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0

    for num in str(n):
        if num == '0':
            count0 += 1
        elif num == '1':
            count1 += 1
        elif num == '2':
            count2 += 1
        elif num == '3':
            count3 += 1
        elif num == '4':
            count4 += 1
        elif num == '5':
            count5 += 1
        elif num == '6':
            count6 += 1
        elif num == '7':
            count7 += 1
        elif num == '8':
            count8 += 1
        elif num == '9':
            count9 += 1
        if count0 >= 3 or count1 >= 3 or count2 >= 3 or count3 >= 3 or count4 >= 3 or count5 >= 3 or count6 >= 3 or count7 >= 3 or count8 >= 3 or count9 >= 3:
            return n


start = int(input('Введите первый год: '))
finish = int(input('Введите второй год: '))

print('Годы от', start, 'до', finish, 'с тремя одинаковыми цифрами:')
for year in range(start, finish + 1):
    if (three(year)) == None:
        ''
    else:
        print(three(year))

# задача 7 выполнена
# прошу сообщить более элегантное решение задачи - спасибо!