length = int(input('Введите длину списка: '))
spisok = [(1 if index % 2 == 0 else index % 5) for index in range(length)]

# Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]
print(f'Результат: {spisok}')