# Напишите программу, которая инициализирует список из 10 случайных целых чисел,
# а затем делит эти числа на пары кортежей внутри списка.
# Выведите результат на экран.
#
# Дополнительно: решите задачу несколькими способами.
# Пример:
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

import random

original_list = [random.randint(0, 50) for _ in range(10)]
print(f'Оригинальный список: {original_list}')

new_list = list()
for index in range(int(len(original_list)/2)):
    piece = original_list[index*2:index*2+2]
    piece = tuple(piece)
    new_list.append(piece)

print(f'Новый список: {new_list}')