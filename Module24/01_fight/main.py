import random


class Warrior:
    name = ''
    health = 0


soldier_1 = Warrior()
soldier_1.name = 'Воин №1'
soldier_1.health = 100

soldier_2 = Warrior()
soldier_2.name = 'Воин №2'
soldier_2.health = 100

while True:
    index = random.randint(1, 2)
    if index == 1:
        soldier_2.health -= 20
        print(f'{soldier_1.name} атакует. {soldier_2.name} теперь имеет {soldier_2.health} здоровья.')
    else:
        soldier_1.health -= 20
        print(f'{soldier_2.name} атакует. {soldier_1.name} теперь имеет {soldier_1.health} здоровья.')

    if soldier_1.health == 0:
        print(f'\n{soldier_2.name} выиграл!')
        break
    elif soldier_2.health == 0:
        print(f'\n{soldier_1.name} выиграл!')
        break
