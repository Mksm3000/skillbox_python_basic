
def tpl_sort(tpl):
    tpl = list(tpl)
    for num in tpl:
        if not float(num).is_integer():
            tpl = tuple(tpl)
            return tpl
    tpl.sort()
    tpl = tuple(tpl)
    return tpl


import random

original_list = [random.randint(-10, 10) for _ in range(7)]
# original_list = [5, -7.5, -5, -9, -10, 4, 1]
original_tuple = tuple(original_list)

# print(f'Оригинальный список: {original_list}')
print(f'Оригинальный кортеж: {original_tuple}')
print(f'Отсортированный кортеж: {tpl_sort(original_tuple)}')
