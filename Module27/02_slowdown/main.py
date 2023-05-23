import time
from typing import Callable, Any
import functools
import requests


def timer(func: Callable) -> Callable:
    """ Декоратор подсчёта времени выполнения функции """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pausa = 2
        time.sleep(pausa)
        print(f'\n<<<Пауза {pausa} сек>>>\n')
        func(*args, **kwargs)
    return wrapper


@timer
def checker(source: str) -> None:
    rez = requests.get(source)
    print(f'{source}\n{rez}')


links = ['https://api.github.com', 'https://google.com', 'https://ya.ru', 'https://bing.com']
for element in links:
    checker(element)
