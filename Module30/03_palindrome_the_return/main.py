def can_be_poly(text: str) -> bool:
    return text[::] == text[::-1]


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

# Результат:
# ```
# True
# False
