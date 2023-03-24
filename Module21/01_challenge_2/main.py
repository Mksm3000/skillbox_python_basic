def funk(number):
    if number <= 0:
        return
    funk(number-1)
    print(number)


num = int(input('Введите num: '))
funk(num)
