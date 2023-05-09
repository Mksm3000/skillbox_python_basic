class Property:

    def __init__(self, worth):
        self.worth = worth

    def tax(self, amount=1):
        self.amount = amount
        return self.worth/amount


class Apartment(Property):

    def tax(self, amount=1000):
        self.amount = amount
        return self.worth/amount


class Car(Property):

    def tax(self, amount=200):
        self.amount = amount
        return self.worth / amount


class CountryHouse(Property):

    def tax(self, amount=500):
        self.amount = amount
        return self.worth / amount

answer = True

while answer:
    budget = int(input('\nВведите сумму вашего бюджета: '))

    apartments = Apartment(int(input('\nВведите стоимость вашей квартиры: ')))
    print(f'Размер налога на квартиру: {apartments.tax()}')

    car = Car(int(input('\nВведите стоимость вашей машины: ')))
    print(f'Размер налога на машину: {car.tax()}')

    country = CountryHouse(int(input('\nВведите стоимость вашего загородного дома: ')))
    print(f'Размер налога на загородный дом: {country.tax()}')

    tax_summ = apartments.tax() + car.tax() + country.tax()
    if tax_summ <= budget:
        print(f'\nПоздравляем!\nВашего бюджета ({budget}) хватает для уплаты всех налогов ({tax_summ}).\n')
    else:
        print(f'\nВнимание!\nВашего бюджета ({budget}) недостаточно для оплаты всех налогов ({tax_summ})!!!\n')

    answer = input('Продолжаем? Y/N  ')
    if answer.lower() == 'n':
        answer = False
