import random


class Hero:
    """ Класс героя"""
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        """ Имя героя """
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        """ Получение очков здоровья """
        return self.__hp

    def set_hp(self, new_value):
        """ Настройка очков здоровья """
        self.__hp = max(new_value, 0)

    def get_power(self):
        """ Получение уровня урона """
        return self.__power

    def set_power(self, new_power):
        """ Настройка уровня урона """
        self.__power = new_power

    def is_alive(self):
        """ Статус жизни """
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, round(self.get_hp(),2))


class Healer(Hero):
    # Целитель:

    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    def __init__(self, name):
        super().__init__(name)
        self.__magic = self.start_power * 3

    def get_magic(self):
        """ Получение уровня урона """
        return self.__magic

    def set_magic(self, new_magic):
        """ Настройка уровня урона """
        self.__magic = new_magic

    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе
    # своей стратегии выполняет ОДНО из действий (атака, исцеление) на выбранную им цель

    def attack(self, target):
        target.take_damage(self.get_power() * 0.5)

    def take_damage(self, power):
        self.set_hp(self.get_hp() - power * 1.2)
        super().take_damage(power)

    def healing(self, target):
        target.set_hp(target.get_hp() + self.get_magic())

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        target_of_healing = friends[0]
        min_health = target_of_healing.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_healing = friend
                min_health = target_of_healing.get_hp()

        if min_health < 100:
            print("|| исцеляет ||", target_of_healing.name)
            self.healing(target_of_healing)
        else:
            if not enemies:
                return
            print(">> атакует ближнего >>", enemies[0].name)
            self.attack(enemies[0])
        self.set_power(self.get_power() + 0.1)
        print('\n')



class Tank(Hero):
    # Танк:

    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    def __init__(self, name):
        super().__init__(name)
        self.shield_up = False  # Щит не поднят (False), иначе - True
        self.defence = 1  # Показатель брони. 1 (щит не поднят), иначе - 2
        self.might = 2  # Показатель силы. 2 (щит не поднят), иначе - 1

    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель

    def shield_status(self):
        return self.shield_up

    def attack(self, target):
        target.take_damage((self.get_power() * 0.5) / self.might)

    def raise_shield(self):
        if not self.shield_up:
            self.shield_up = True
            self.defence = 2
            self.might = 1

    def lower_shield(self):
        if self.shield_up:
            self.shield_up = False
            self.defence = 1
            self.might = 2

    def take_damage(self, power):
        self.set_hp(self.get_hp() - (power / self.defence))
        super().take_damage(power)

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        if not enemies:
            return

        if self.get_hp() < 80 and not self.shield_up:
            self.raise_shield()
            print("|| поднял щит")
        elif self.get_hp() > 130 and self.shield_up:
            self.lower_shield()
            print("__ опустил щит")
        else:
            print(">> атакует ближнего >>", enemies[0].name)
            self.attack(enemies[0])

        self.set_power(self.get_power() + 0.1)
        print('\n')

class Attacker(Hero):
    # Убийца:

    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 2.5  # коэффициент усиления урона

    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power)
    # умноженному на коэффициент усиления урона (self.power_multiply)

    # после нанесения урона - вызывается метод ослабления power_down.

    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)

    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе
    # своей стратегии выполняет ОДНО из действий (атака, усиление, ослабление)
    # на выбранную им цель

    def attack(self, target):
        target.take_damage((self.get_power() * self.power_multiply))
        self.power_down()


    def take_damage(self, power):
        self.set_hp(self.get_hp() - (power * self.power_multiply / 2))
        super().take_damage(power)

    def power_up(self):
        self.power_multiply *= 2

    def power_down(self):
        self.power_multiply /= 2

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        if not enemies:
            return

        if (self.get_power() * self.power_multiply) < 40:
            self.power_up()
            print("накапливает силы для удара")
        else:
            print(">> атакует ближнего >>", enemies[0].name)
            self.attack(enemies[0])
        self.set_power(self.get_power() + 0.1)
        print('\n')
