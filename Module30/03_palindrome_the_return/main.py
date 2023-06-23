from collections import Counter


def can_be_poly(text: str) -> bool:
    return len(list(filter(lambda value: value % 2, Counter(text).values()))) < 2


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

# Результат:
# ```
# True
# False
