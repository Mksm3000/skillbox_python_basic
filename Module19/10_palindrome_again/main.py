text = input('Введите строку: ')
res_dict = dict()

for word in text:
    if word in res_dict.keys():
        res_dict[word] += 1
    else:
        res_dict[word] = 1
# print(res_dict)

even_count = 0
odd_count = 0

for value in res_dict.values():
    if value %2 == 0:
        even_count += 1
    else:
        odd_count += 1

if odd_count >= 2:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
