
import time
from typing import Callable
import functools


def timer(func: Callable) -> Callable:
    """ Декоратор подсчёта времени выполнения функции """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        time_func = end - start
        return print(round(time_func,5))
    return wrapper


@timer
def counter(num: int) -> list:
    """ Функция создает список из num элементов
:return список
    """
    return [x ** 2 ** x for x in range(num)]


for element in range(18,24):
    print(f'Для элемента №{element} время выполнения:', end=' ')
    counter(element)
    time.sleep(1)

print(f'\nОписание функции {counter.__name__}:\n{counter.__doc__}')
