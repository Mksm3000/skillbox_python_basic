
from typing import Callable, NoReturn, Any
import functools
import time


# Реализуйте декоратор `logging`, который будет отвечать за логирование функций.
# На экран выводится название функции и её документация.
# Если во время выполнения декорируемой функции возникла ошибка, то в файл `function_errors.log`
# записываются названия функции и ошибки.
#
# Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки,
# а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.
#
# Дополнительно: запишите дату и время возникновения ошибки, используя модуль `datetime`.

with open('function_errors.log', 'w', encoding='utf-8') as file:
    file.write("")


def logging(func: Any) -> Any:
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
            return print(f'Имя функции: "{func.__name__}".\nОписание функции: {func.__doc__}.')
        except (ZeroDivisionError, TypeError, NameError) as exc:
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write('\nВремя: ' + str(time.ctime())
                           + '.\nФункция: ' + str(func.__name__)
                           + '.\nОписание функции: ' + (str(func.__doc__))
                           + '.\nТип ошибки: ' + str(type(exc).__name__)
                           + '.\nОписание ошибки: ' + str(exc) + '\n')
    return wrapper


@logging
def divider(dividend: int, divisor: Any) -> Any:
    """Делим нечто на другое нечто"""
    result = dividend/divisor
    return print(f"\n{result}")


fix = 101
exam_list = [5, 'a', 1.1, 0, '0', 4e-2, ('50', 'hey')]

for element in exam_list:
    divider(fix,element)
    time.sleep(1.1)

