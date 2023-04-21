import random


class Water:
    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vape()
        elif isinstance(other, Earth):
            return Mud()


class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lite()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()


class Fire:
    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lite()
        elif isinstance(other, Water):
            return Vape()


class Earth:
    def __str__(self):
        return 'Earth'

    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Lite()
        elif isinstance(other, Fire):
            return Lava()


class Storm:
    def __str__(self):
        return 'Storm'


class Vape:
    def __str__(self):
        return 'Vape'


class Mud:
    def __str__(self):
        return 'Mud'


class Lite:
    def __str__(self):
        return 'Lite'


class Dust:
    def __str__(self):
        return 'Dust'


class Lava:
    def __str__(self):
        return 'Lava'


water = Water()
air = Air()
storm = Storm()
fire = Fire()
vape = Vape()
earth = Earth()
mud = Mud()
lite = Lite()
dust = Dust()
lava = Lava()

while True:
    r1 = random.choice([water, air, fire, earth])
    r2 = random.choice([water, air, fire, earth])
    print(f'\n{r1} + {r2}', end=' = ')
    print(r1 + r2)
    void = input('push any key!\n')