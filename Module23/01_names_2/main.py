
line_count = 0
sum_sym = 0

try:
    with open('people.txt', 'r', encoding='utf-8') as file:
        for i_line in file:
            line_count += 1
            i_line = i_line.rstrip('\n')
            sum_sym += len(i_line)
            try:
                if len(i_line) < 3:
                    raise BaseException(f'Ошибка: менее трёх символов')
            except BaseException:
                print(f'Ошибка: менее трёх символов в строке {line_count}.')

except FileNotFoundError:
    print('Файл не найден')

finally:
    print(f'Общее количество символов: {sum_sym}')
