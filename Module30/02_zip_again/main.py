from typing import List

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(map(lambda x, y: (x, y), letters, numbers))
print(result)


# Результат работы программы:
# ```
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]