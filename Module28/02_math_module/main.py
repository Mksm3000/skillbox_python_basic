import math
from typing import Union


class MyMath:
    @staticmethod
    def circle_len(radius: Union[int, float]) -> Union[int, float]:
        """Вычисление длины окружности"""
        return 2 * math.pi * radius

    @staticmethod
    def circle_sq(radius: Union[int, float]) -> Union[int, float]:
        """Вычисление площади окружности"""
        return math.pi * radius ** 2

    @staticmethod
    def cube_volume(side: Union[int, float]) -> Union[int, float]:
        """Вычисление объёма куба"""
        return side ** 3

    @staticmethod
    def sphere_sq(radius: Union[int, float]) -> Union[int, float]:
        """Вычисление площади поверхности сферы"""
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.sphere_sq(radius=7.7)
res_4 = MyMath.cube_volume(side=8.8)

print(res_1)
print(res_2)
print(res_3)
print(res_4)
