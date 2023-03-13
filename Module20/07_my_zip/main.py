# Пример:
# Строка: abcd
# Кортеж чисел: (10, 20, 30, 40)
# Результат:
# <generator object <genexpr> at 0x00000204A4234048>
# ('a', 10)
# ('b', 20)
# ('c', 30)
# ('d', 40)
#
# def my_zip(str, kort):
#     answer = []
#     for i in range(min(len(str), len(kort))):
#         block = (str[i], kort[i])
#         answer.append(block)
#     return answer


import random

# print(ord("a"), ord("z"))

stroka = str()
stroka_length = random.randint(5, 10)
for _ in range(stroka_length):
    stroka += chr(random.randint(97, 122))
print(f'Строка: {stroka}')

kortezh = list()
kortezh_length = random.randint(6, 8)
for _ in range(kortezh_length):
    kortezh.append(random.randint(10, 100))
kortezh = tuple(kortezh)
print(f'Кортеж: {kortezh}')

my_gen = ((stroka[i], kortezh[i]) for i in range(min(len(stroka), len(kortezh))))

print('\n', my_gen)
print('Результат:')
for pair in my_gen:
    print(pair)
