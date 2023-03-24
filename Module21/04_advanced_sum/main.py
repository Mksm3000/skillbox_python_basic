def sum(*args):
    summ = 0
    for i_elem in args:
        if isinstance(i_elem, int):
            summ += i_elem
        elif isinstance(i_elem, list):
            for sub_elem in i_elem:
                summ += sum(sub_elem)
    return summ


# sum([[1, 2, [3]], [1], 3])
# Ответ в консоли: 10

# data = sum([[1, 2, [3]], [1], 3])
# print(f'Ответ в консоли: {data}')

# sum(1, 2, 3, 4, 5)
# Ответ в консоли: 15

# data = sum(1, 2, 3, 4, 5)
# print(f'Ответ в консоли: {data}')
