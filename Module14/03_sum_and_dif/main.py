print('Задача 3. Сумма и разность\n')

#Пример работы программы:
#Введите число: 500
#Сумма чисел: 5
#Количество цифр в числе: 3
#Разность суммы и количества цифр: 2

def summ(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    return summ

def count(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

number = int(input('Введите число: '))
print('Сумма чисел:', summ(number))
print('Количество цифр в числе:', count(number))
print('Разность суммы и количества цифр:', summ(number) - count(number))

# задача 3 выполнена