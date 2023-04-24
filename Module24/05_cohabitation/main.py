
import random


class House:
    """ Описание дома (холодильник, деньги) """

    def __init__(self, food=50, wallet=0):
        self.food = food
        self.wallet = wallet

    def home_info(self):
        print(f'Состояние дома: еда - {self.food}, деньги - {self.wallet}.')


class Human:
    """ Описание человека (имя, дом, сытость) """

    def __init__(self, name, house, full=50):
        self.name = name
        self.house = house
        self.full = full

    def eat(self):  # функция "есть"
        self.full += 5
        self.house.food -= 5

    def work(self):  # функция "работать"
        self.full -= 10
        self.house.food -= 10
        self.house.wallet += 50

    def play(self):  # функция "играть"
        self.full -= 5

    def shopping(self):  # функция "поход в магазин"
        self.house.food = 50
        self.house.wallet -= 25

    def human_info(self):
        print(f'Состояние {self.name}: сытость - {self.full}.')


home_common = House(50, 0)
home_m = House(35, 20)
home_w = House(45, 10)
home_common.home_info()

man = Human('Karl', home_common, 45)
woman = Human('Sarah', home_common, 55)
man.human_info()
woman.human_info()

day_count = 0

while True:
    day_count += 1
    cube = random.randint(1, 6)

    print(f'\nСегодня {day_count}-ый день.')

    if cube != 1 or cube != 2:
        print(f'Кубик "{cube}" - надо поиграть.')
        if man.full < 20:
            print(f'У {man.name} голод. Надо поесть')
            man.eat()
        if woman.full < 20:
            print(f'У {woman.name} голод. Надо поесть')
            woman.eat()

        if home_common.food < 10:
            print(f'Дома еды меньше 10')
            if man.full >= woman.full:
                print(f'{man.name} идёт в магазин')
                man.shopping()
            else:
                print(f'{woman.name} идёт в магазин')
                woman.shopping()

        if home_common.wallet < 50:
            print(f'Дома денег меньше 50')
            if man.full >= woman.full:
                print(f'{man.name} идёт на работу')
                man.work()
            else:
                print(f'{woman.name} идёт на работу')
                woman.work()

        else:
            man.play()
            woman.play()

    elif cube == 1:
        print('Кубик "1" - надо работать.')
        man.work()
        woman.work()
    elif cube == 2:
        print('Кубик "2" - надо поесть.')
        man.eat()
        woman.eat()

    man.human_info()
    woman.human_info()
    home_common.home_info()

    if day_count > 365 or man.full < 0 or woman.full < 0:
        break
