from typing import Any
from datetime import date


class Date:

    def __init__(self, day: int, month: int, year: int) -> None:
        self.__date = date(year, month, day)

    @classmethod
    def fragmentation(cls, data_string: str) -> tuple:
        return tuple(map(int, data_string.split('-')))

    @classmethod
    def is_date_valid(cls, data_string: str) -> bool:
        try:
            day, month, year = cls.fragmentation(data_string)
            if date(year, month, day):
                return True
        except:
            return False

    @classmethod
    def from_string(cls, data_string: str) -> Any:
        if cls.is_date_valid(data_string):
            day, month, year = cls.fragmentation(data_string)
            result = cls(day, month, year)
            return result
        else:
            return f'Ошибка в данных'

    def __str__(self) -> str:
        return self.__date.strftime('День: %d (%A)\tМесяц: %m (%B)\tГод: %Y')


test_date = Date.from_string('10-12-2077')
print(test_date)

test_date = Date.from_string('12-04-1961')
print(test_date)

print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

# Результат:
# День: 10	Месяц: 12	Год: 2077
# True
# False
