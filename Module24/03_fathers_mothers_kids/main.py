class Child:

    def __init__(self, ch_name, ch_age):
        self.ch_name = ch_name
        self.ch_age = ch_age
        self.calm_state = False
        self.hungry = True

    def kid_info(self):
        print(f'\nИмя ребенка: {self.ch_name}.\n'
              f'Возраст ребенка: {self.ch_age}.\n'
              f'Спокойствие: {self.calm_state}.\n'
              f'Голод: {self.hungry}')


class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.kids = []

    def print_info(self):
        print(f'\nИмя родителя: {self.name}.\nВозраст родителя: {self.age}.\nДети: {self.kids}')

    def add_kid(self, kid_name, kid_age):
        while kid_age > self.age - 16:
            print(f'\nОй, ошибка! Ребенок родился, когда родитель ещё сам был ребенком!')
            kid_age = int(input(f'Введите возраст ребенка {kid_name} еще раз: '))
        kid = Child(kid_name, kid_age)
        self.kids.append(kid_name)
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


mama = Parent('Elisa', 33)
mama.print_info()

son = mama.add_kid('Tommy', 45)
mama.print_info()
son.kid_info()

mama.calm(son)
son.kid_info()
mama.calm(son)

papa = Parent('Karl', 35)
papa.print_info()

papa.full(son)
son.kid_info()

mama.full(son)
son.kid_info()

baby = papa.add_kid('Anna', 2)
papa.print_info()
baby.kid_info()

papa.calm(baby)
baby.kid_info()
papa.calm(baby)
