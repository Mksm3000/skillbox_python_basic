from typing import Callable
import functools


# Реализуйте декоратор для декораторов:
# он должен декорировать другую функцию, которая должна быть декоратором, и даёт возможность любому декоратору
# принимать произвольные аргументы.
#
# Пример использования:


def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    """ Декоратор (высший) для декоратора с аргс и кваргс"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(*args, **kwargs) -> Callable:
    """ Декорируемый декоратор (низший) с аргс и кваргс """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# Результат:
# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101
