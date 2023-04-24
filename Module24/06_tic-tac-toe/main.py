class Board:

    def __init__(self):
        self.base = [Cell(num, num) for num in range(1, 10)]

    def base_print(self):
        print(self.base[0].symbol, '|', self.base[1].symbol, '|', self.base[2].symbol)
        print('-' * 10)
        print(self.base[3].symbol, '|', self.base[4].symbol, '|', self.base[5].symbol)
        print('-' * 10)
        print(self.base[6].symbol, '|', self.base[7].symbol, '|', self.base[8].symbol)

    def reset_base(self):
        self.base = [Cell(num, num) for num in range(1, 10)]

    def change_cell(self, num, symb):
        correct_num = num - 1
        if self.base[correct_num].symbol in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.base[correct_num].symbol = symb
            return True
        else:
            return False

    def check_end(self, sign):
        self.base_print()
        for i in Board.victory:
            if self.base[i[0]].symbol == sign and self.base[i[1]].symbol == sign and self.base[i[2]].symbol == sign:
                return True
        return False

    victory = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
               [0, 3, 6], [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]


class Cell:

    def __init__(self, num: int, symbol):
        self.num = num
        self.symbol = symbol


class Player:

    def __init__(self, name, symbol, wins=0):
        self.name = name
        self.wins = wins
        self.symbol = symbol

    def choose(self):
        while True:
            num_cell = int(input('введите номер клетки: '))
            if 1 <= num_cell <= 9:
                break
            else:
                print('Номер клетки должен быть от 1 до 9.')
        return num_cell


class Game:
    draw = 0

    def __init__(self, player1, player2, field):
        self.player1 = player1
        self.player2 = player2
        self.field = field

    def one_step(self, player, symbol):
        number = player.choose()
        if self.field.change_cell(number, symbol):
            return True if self.field.check_end(symbol) else False

    def one_game(self):
        count = 0
        while True:
            if count % 2 == 0:
                print(f'\n{self.player1.name}', end=' ')
                if self.one_step(self.player1, self.player1.symbol):
                    print(f'\nВыиграл {self.player1.name}')
                    self.player1.wins += 1
                    break
            elif count % 2 != 0:
                print(f'\n{self.player2.name}', end=' ')
                if self.one_step(self.player2, self.player2.symbol):
                    print(f'\nВыиграл {self.player2.name}')
                    self.player2.wins += 1
                    break
            count += 1
            if count >= 9:
                print('Ничья!')
                self.draw += 1
                break

    def general_start(self):
        while True:
            ask = input('\n<Будем играть? Y/N : ')
            if ask.lower() == 'y':
                self.field.reset_base()
                self.field.base_print()
                print()
                self.one_game()
            elif ask.lower() == 'n':
                break
            else:
                print('Ой! Введите Y или N.\n')
            print(f'Текущий счет: {self.player1.name} - {self.player1.wins}; {self.player2.name} - {self.player2.wins}')
            if self.draw > 0:
                print(f'Игр в ничью: {self.draw}')


while True:
    name_1 = input('\nИмя игрока №1: ')
    sym_1 = input('Символ игрока №1: ')

    name_2 = input('\nИмя игрока №2: ')
    sym_2 = input(f'Символ игрока №2 (запрещено использовать символ "{sym_1}" игрока {name_1}): ')

    igrok_1 = Player(name_1, sym_1)
    igrok_2 = Player(name_2, sym_2)
    new_board = Board()
    ttt_game = Game(igrok_1, igrok_2, new_board)
    ttt_game.general_start()
