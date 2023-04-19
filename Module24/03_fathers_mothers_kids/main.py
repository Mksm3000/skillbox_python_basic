
class Parent:
    kids = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'\nИмя родителя: {self.name}.\nВозраст родителя: {self.age}.\nДети: {self.kids}')

    def add_kid(self, kid_name, kid_age):
        if kid_age > (Parent(self.name, self.age).age - 16):
            print(f'Ой, ошибка! Ребенок родился, когда родитель ещё сами были ребенком!')
            new_kid_age = int(input('\nВведите возраст ребенка еще раз: '))
            self.add_kid(kid_name, new_kid_age)
        kid = Child(kid_name, new_kid_age)
        if isinstance(kid, Child):
            Parent.kids.append(kid.ch_name)
        else:
            Parent.kids.append(kid)
        return kid

    def calm(self, kid):
        print('\nРодитель хочет успокоить ребенка {}'.format(kid.ch_name))
        if kid.calm_state == False:
            kid.calm_state = True
            return print('Ребенок успокоился!')
        else:
            return print('Ребенок и так спокоен. Успокойтесь сами!')

    def full(self, kid):
        print('\nРодитель хочет покормить ребенка {}'.format(kid.ch_name))
        if kid.hungry == True:
            kid.hungry = False
            return print('Ребенок покормлен!')
        else:
            return print('Ребенок сыт. Не надо его перекармливать!')


class Child:

    def __init__(self, ch_name, ch_age):
        self.ch_name = ch_name
        self.ch_age = ch_age
        self.calm_state = False
        self.hungry = True

    def print_info(self):
        print(f'\nИмя ребенка: {self.ch_name}.\nВозраст ребенка: {self.ch_age}.\nСпокойствие: {self.calm_state}.\nГолод: {self.hungry}')


mama = Parent('Elisa', 33)
mama.print_info()
son = mama.add_kid('Tom', 28)
mama.print_info()
son.print_info()
mama.calm(son)
son.print_info()
mama.calm(son)

papa = Parent('Karl', 35)
papa.print_info()
papa.full(son)
son.print_info()
mama.full(son)
son.print_info()

baby = papa.add_kid('Anna', 2)
papa.print_info()
baby.print_info()
papa.calm(baby)
baby.print_info()
papa.calm(baby)
