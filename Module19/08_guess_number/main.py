number = int(input('Введите максимальное число: '))

variant = set()
set_yes = set()
set_no = set()
answer = ''

while answer != 'Помогите!':
    print('Нужное число есть среди вот этих чисел:', end=' ')
    variant = input()
    if variant == 'Помогите!':
        diff = set_yes.difference(set_no)
        print(f'Артём мог загадать следующие числа: {" ".join(diff)}')
        break
    variant = set(variant.split())
#    print(type(variant), variant)
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        set_yes = set_yes.union(variant)
#        print('set_yes', set_yes)
    elif answer == 'Нет':
        set_no = set_no.union(variant)
#        print('set_no', set_no)
