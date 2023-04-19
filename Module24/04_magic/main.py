import random

magic_dict = {
    'Шторм': ['Вода', 'Воздух'],
    'Пар': ['Вода', 'Огонь'],
    'Грязь': ['Вода', 'Земля'],
    'Молния': ['Огонь', 'Воздух'],
    'Пыль': ['Земля', 'Воздух'],
    'Лава': ['Огонь', 'Земля'],
}


class Basic:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        for key, value in magic_dict.items():
            if self.name in value and other.name in value and self.name != other.name:
                return key
        else:
            return None


class Magic:

    def __init__(self, answer):
        self.answer = answer


random_1 = (random.choice(list(magic_dict.values())))[0]
random_2 = (random.choice(list(magic_dict.values())))[1]

element_1 = Basic(random_1)
element_2 = Basic(random_2)

magic_element = Magic(element_1 + element_2)
print(f'\nСложили "{element_1.name}" + "{element_2.name}" и получили "{magic_element.answer}"')
