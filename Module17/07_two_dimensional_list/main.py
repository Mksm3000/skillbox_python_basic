# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# Используйте только list comprehensions.

spisok = [x for x in range(1, 13)]
spisok = [spisok[0::4], spisok[1::4], spisok[2::4], spisok[3::4]]
print(spisok)
