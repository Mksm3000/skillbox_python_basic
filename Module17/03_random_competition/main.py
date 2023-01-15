import random

first = [round(random.uniform(5.00, 10.00), 2) for i_f in range(20)]
second = [round(random.uniform(5.00, 10.00), 2) for i_s in range(20)]
winner = [max(first[i_w], second[i_w]) for i_w in range(20)]

print(f'Первая команда: {first}')
print(f'Вторая команда: {second}')
print(f'Победители тура: {winner}')
