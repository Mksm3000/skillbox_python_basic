from typing import Callable
import functools

# На вас возложили задачу по созданию и поддержке специализированного сайта-форума.
# Вы только начали выполнять задачу и сейчас остановились на реализации действий, которые могут
# совершать посетители форума.
# И конечно же, для разных пользователей прописаны разные возможности.

# Напишите декоратор `check_permission`, который проверяет, есть ли у пользователя доступ к
# вызываемой функции, и если нет, то выдаёт исключение `PermissionError`.


def check_permission(name: str) -> Callable:
    """ Декоратор проверяет есть ли у пользователя доступ к вызываемой функции """
    def check(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if name in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: У пользователя "{name}" недостаточно прав, чтобы выполнить функцию "{func.__name__}"')
        return wrapper
    return check


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()


# Результат:
# Удаляем сайт
# PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment