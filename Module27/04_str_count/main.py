import random
import time
from typing import Callable, NoReturn, Any
import functools


def counter(func: Callable) -> Callable:
    counter_dict = {}

    @functools.wraps(func)
    def count_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        if func.__name__ not in counter_dict.keys():
            counter_dict[func.__name__] = 1
        else:
            counter_dict[func.__name__] += 1
        print(f'Имя функции: "{func.__name__}".\nВызывалась {counter_dict[func.__name__]} раз(а).')

    return count_wrapper


def timer(func: Callable) -> Callable:
    """ Декоратор подсчёта времени выполнения функции """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        time_func = end - start
        return print(round(time_func, 5))

    return wrapper


@counter
@timer
def lister(num: int) -> list:
    """ Функция создает список из num элементов
:return список
    """
    return [x ** 2 ** x for x in range(num)]


def how_are_you(func: Any) -> Any:
    """ Декоратор, выводящий не только функцию """

    @functools.wraps(func)
    def how_wrapper(*args, **kwargs):
        print('\nКак дела?', end=' -> ')
        answer = input()
        print('А у меня не очень! Ладно, держи свою функцию.\n')
        func(*args, **kwargs)

    return how_wrapper


@counter
@how_are_you
def test() -> None:
    """ Тестовая функция """
    print('<Тут что-то происходит...>')


while True:
    random_num = random.randint(0, 1)
    if random_num == 0:
        for element in range(20, 22):
            print(f'Для элемента №{element} время выполнения:', end=' ')
            lister(element)
            time.sleep(1)
    else:
        test()
    print('+ ' * 20)
