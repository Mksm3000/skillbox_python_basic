import random


class Warrior:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def fight(self, enemy):
        enemy.health -= 20
        print(f'{self.name} атакует. {enemy.name} теперь имеет {enemy.health} здоровья.')


soldier_1 = Warrior('Воин №1', 100)
soldier_2 = Warrior('Воин №2', 100)

while True:
    index = random.randint(1, 2)
    if index == 1:
        soldier_1.fight(soldier_2)
    else:
        soldier_2.fight(soldier_1)

    if soldier_1.health == 0:
        print(f'\n{soldier_2.name} выиграл!')
        break
    elif soldier_2.health == 0:
        print(f'\n{soldier_1.name} выиграл!')
        break
