def list_create(num, line):
    list_create = []
    for i in range(num):
        print(f'Введите {i + 1} число {line}-го списка:', end=' ')
        num = int(input())
        list_create.append(num)
    return list_create


num_list_1 = 3
list_1 = list_create(num_list_1, 1)
print()
num_list_2 = 7
list_2 = list_create(num_list_2, 2)

print(f'\nПервый список: {list_1}')
print(f'Второй список: {list_2}')

list_1_new = list_1 + list_2

times = len(list_1_new)

for time in range(times):
  for i in list_1_new:
    count = 0
    for j in list_1_new:
      if i == j:
        count += 1
    if count > 1:
      list_1_new.remove(i)

print(f'\nНовый первый список с уникальными элементами: {list_1_new}')