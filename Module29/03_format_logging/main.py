from datetime import datetime
import functools
import time
from typing import Callable


def logged(cls, funk: Callable, input_str: str) -> Callable:
    """ Декоратор логирования метода класса """
    @functools.wraps(funk)
    def wrapper(*args, **kwargs):
        print(f"- Запускается '{cls.__name__}.{funk.__name__}'. Дата и время запуска: {datetime.now().strftime(input_str)}")
        start = time.time()
        result = funk(*args, **kwargs)
        end = time.time()
        print(f"- Завершение '{cls.__name__}.{funk.__name__}'. Время работы = {round(end - start, 3)}")
        return result
    return wrapper


def log_methods(input_str: str) -> Callable:
    """ Декоратор логирования класса, с настраиваемым выводом даты и времени """
    def decorator(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                current_method = getattr(cls, i_method_name)
                decorated_method = logged(cls, current_method, input_str)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorator


@log_methods("%b %d %Y - %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("%b %d %Y - %H:%M:%S")
class B(A):
    def test_sum_1(self) -> None:
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
time.sleep(2)
my_obj.test_sum_2()

"""
%a Weekday as locale’s abbreviated name.
%A Weekday as locale’s full name.
%w Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
%d Day of the month as a zero-padded decimal number.
%b Month as locale’s abbreviated name.
%B Month as locale’s full name.
%m Month as a zero-padded decimal number. 01, ..., 12
%y Year without century as a zero-padded decimal number. 00, ..., 99
%Y Year with century as a decimal number. 1970, 1988, 2001, 2013
%H Hour (24-hour clock) as a zero-padded decimal number. 00, ..., 23
%I Hour (12-hour clock) as a zero-padded decimal number. 01, ..., 12
%p Locale’s equivalent of either AM or PM.
%M Minute as a zero-padded decimal number. 00, ..., 59
%S Second as a zero-padded decimal number. 00, ..., 59
%f Microsecond as a decimal number, zero-padded on the left. 000000, ..., 999999
%z UTC offset in the form +HHMM or -HHMM (empty if naive), +0000, -0400, +1030
%Z Time zone name (empty if naive), UTC, EST, CST
%j Day of the year as a zero-padded decimal number. 001, ..., 366
%U Week number of the year (Sunday is the first) as a zero padded decimal number.
%W Week number of the year (Monday is first) as a decimal number.
%c Locale’s appropriate date and time representation.
%x Locale’s appropriate date representation.
%X Locale’s appropriate time representation.
%% A literal '%' character.
"""

