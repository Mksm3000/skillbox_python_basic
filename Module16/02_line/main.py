class_a = list(range(160,176+1,2))
class_b = list(range(162,180+1,3))
united_class = class_a + class_b
united_class.sort()
print(f'Отсортированный список учеников: {united_class}')