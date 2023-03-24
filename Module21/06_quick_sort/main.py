
def qsort(liist):
    pivot = liist[-1]
    less = []
    equal = []
    greater = []

    for element in liist:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)

    if less:
        less = qsort(less)

    if greater:
        greater = qsort(greater)

    return less + equal + greater


start = [5, 8, 9, 4, 2, 9, 1, 8]
print(qsort(start))
