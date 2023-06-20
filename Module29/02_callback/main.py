from typing import Callable

app = {}


def callback(adress: str) -> Callable:
    """ Функция обратного вызова, запускается при совпадении адреса """

    def wrapped(func: Callable) -> Callable:
        app[adress] = func
        return func
    return wrapped


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


paths = ['google.com', 'ya.ru', '//', 'bing.me']
for name in paths:
    route = app.get(name)
    if route:
        response = route()
        print(f'{name} - Ответ: {response}')
    else:
        print(f'{name} - Такого пути нет')
