import random

summ = 0

file = open('out_file.txt', 'w')
file.close()

while summ < 777:
    num = int(input('Введите число: '))
    try:
        if 13 == random.randint(1, 13):
            raise random.choice([SyntaxError, KeyError, ValueError])
    except SyntaxError:
        print('SyntaxError. Вас постигла неудача!')
        break
    except KeyError:
        print('KeyError. Вас постигла неудача!')
        break
    except ValueError:
        print('ValueError. Вас постигла неудача!')
        break
    else:
        file = open('out_file.txt', 'a', encoding='utf-8')
        file.write(str(num) + '\n')
        file.close()
        summ += num
        if summ >= 777:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')

