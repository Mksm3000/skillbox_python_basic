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
    bad_news = False
    chance = random.randint(1, 10)
    marks = random.randint(1, 7)
    if chance == 10:
        bad_news = True
    return marks, bad_news


error_list = [DrunkError, CarCrashError, GluttonyError, DepressionError]

with open('karma.log', 'w', encoding='utf-8') as file:
    file.write('')

karma = 0
day = 0

while karma < 500:
    day += 1
    try:
        point, problem = one_day()
        if problem:
            random_error = random.choice(error_list)
            raise random_error

        else:
            karma += point
            print(f'День: {day}. Карма: {karma}.')

    except random_error:
        minus_point = point * 5 # отрицательная карма с коэф. 5
        karma -= minus_point
        with open('karma.log', 'a', encoding='utf-8') as file:
            file.write('День: ' + str(day) + '. Минус ' + str(minus_point) + ' кармы за ' + str(random_error.__name__) + '\n')

print(f'\nНа {day} день к вам снизошло просветление! Аум!')


