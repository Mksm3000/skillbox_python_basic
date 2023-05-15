from collections.abc import Iterable, Iterator


# класс-итератор
class Iterator:

    def __init__(self, num: int) -> None:
        self.start = 0
        self.num = num

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.start < self.num:
            self.start += 1
            return self.start ** 2
        else:
            raise StopIteration


# функция-генератор
def generator(num: int) -> Iterable[int]:
    for i in range(1, num + 1):
        yield i ** 2


number = int(input('Введите число: '))

sequence = Iterator(number)
seq_list = generator(number)
# генераторное выражение
seq_gen = (i**2 for i in range(1,number+1))


print('\nВариант №1')
for index in sequence:
    print(index, end=' ')

print('\n\nВариант №2')
for index in seq_list:
    print(index, end=' ')

print('\n\nВариант №3')
for index in seq_gen:
    print(index, end=' ')