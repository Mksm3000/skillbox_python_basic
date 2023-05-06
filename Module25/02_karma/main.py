import random


class DrunkError(Exception):

    def info(self):
        return 'Минус кармы из-за пьянки'


class CarCrashError(Exception):

    def info(self):
        return 'Минус кармы из-за аварии'


class GluttonyError(Exception):

    def info(self):
        return 'Минус кармы из-за обжорства'


class DepressionError(Exception):

    def info(self):
        return 'Минус кармы из-за уныния'


def one_day():
    chance = random.randint(1, 10)
    marks = random.randint(1, 7)
    error_list = [DrunkError, CarCrashError, GluttonyError, DepressionError]
    if chance == 10:
        raise random.choice(error_list)
    return marks


with open('karma.log', 'w', encoding='utf-8') as file:
    file.write('')

karma = 0
day = 0

while karma < 500:
    day += 1
    try:
        point = one_day()
        karma += point
        print(f'День: {day}. Карма: {karma}.')

    except (DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
        minus_point = random.randint(1, 50)
        karma -= minus_point
        with open('karma.log', 'a', encoding='utf-8') as file:
            file.write('День: ' + str(day) + '. Минус ' + str(minus_point) + ' кармы за ' + str(exc.__class__.__name__) + '\n')

print(f'\nНа {day} день к вам снизошло просветление! Аум!')
