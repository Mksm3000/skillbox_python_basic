# Напишите функцию, возвращающую список элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс — это простое число.
# Для проверки на простое число напишите отдельную функцию is_prime.
# Необязательное усложнение: сделайте так, чтобы основная функция состояла только из оператора return и так же возвращала список.

# Пример вызова функции:
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# Ответ в консоли: [2, 3, 5, 7]
# Пример вызова функции:
# print(crypto('О Дивный Новый мир!'))
# Ответ в консоли: ['Д', 'и', 'н', 'й', 'в', 'й', 'р']

def is_prime(num):
    count = 1
    if num <= 1:
        return False
    else:
        for index in range(2, int(num ** 0.5) + 1):
            if num % index == 0:
                count += 1
        if count < 2:
            return True


def crypto(data):
    answer = list()
    for index, value in enumerate(data):
        if is_prime(index):
            answer.append(value)
    return answer


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))