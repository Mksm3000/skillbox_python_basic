from typing import Callable
import functools


def decorator_with_args_for_any_decorator(any_decorator: Callable) -> Callable:
    """ Декоратор (высший) для декоратора с аргс и кваргс"""
    def decorator_in(*args, **kwargs) -> Callable:
        def wrapper(func: Callable) -> Callable:
            return any_decorator(func, *args, **kwargs)
        return wrapper
    return decorator_in


@decorator_with_args_for_any_decorator
def decorated_decorator(func, *dec_args, **dec_kwargs) -> Callable:
    """ Декорируемый декоратор (низший) с аргс и кваргс """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {dec_args}, {dec_kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# Результат:
# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101
