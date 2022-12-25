print('Задача 4. Число наоборот 3\n')

# Пользователь вводит два вещественных числа — N и K.
# Напишите программу, которая сначала заменяет целую часть на число.
# Оно должно отличаться от исходного тем, что цифры записаны в обратном порядке.
# Затем то же самое программа делает с дробной частью.
# После этого числа складываются и сумма выводится на экран.

# Пример работы программы:
# Введите первое число: 102.12
# Введите второе число: 123.34
# Первое число наоборот: 201.21
# Второе число наоборот: 321.43
# Сумма: 522.64

def rever(n):
    text = str(n)
    numberInt = ''
    numberFract = ''
    flag = True
    for i in text:
        if i != '.' and flag == True:
            numberInt = i + numberInt
        elif i == '.':
            flag = False
        elif i != '.' and flag == False:
            numberFract = i + numberFract
#    print(numberInt + '.' + numberFract)
    return float(numberInt + '.' + numberFract)


first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))
print('\nПервое число наоборот:', rever(first))
print('Второе число наоборот:', rever(second))
print('\nСумма:', rever(first) + rever(second))

# задача 4 выполнена