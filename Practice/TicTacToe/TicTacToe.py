import random


class MyError(Exception):
    def __init__(self, message):
        self.message = message


class TicTacToe:
    def __init__(self, first, second):
        self.field = [' ' for _ in range(9)]
        self.free_cells = list(range(9))
        self.char = 'X'
        self.first = first
        self.second = second

    def draw_field(self):
        print('---------')
        for i in range(3):
            print('| ' + ' '.join(self.field[3 * i: 3 * (i + 1)]) + ' |')
        print('---------')

    def change(self):
        return ('X', 'O')[self.char == 'X']

    def check(self, some_char=None, some_field=None):
        if not some_field:
            some_field = self.field
        if not some_char:
            some_char = self.char
        if (any(some_field[3 * i:3* i + 3].count(some_char) == 3 for i in range(3))
                or any(some_field[i::3].count(some_char) == 3 for i in range(3))
                or some_field[::4].count(some_char) == 3
                or some_field[2:8:2].count(some_char) == 3):
            return True
        return False

    def check_char(self, some_char=None):
        if not some_char:
            some_char = self.char
        for x in self.free_cells:
            test_field = self.field[:]
            test_field[x] = some_char
            if self.check(some_char, test_field):
                return x

    def easy_check(self):
        return random.choice(self.free_cells)

    def medium_check(self):
        if self.check_char():
            return self.check_char()
        elif self.check_char(self.change()):
            return self.check_char(self.change())
        return None

    def hard_check(self):
        if 4 in self.free_cells:
           return 4
        elif any(i % 2 == 0 for i in self.free_cells):
            return random.choice([i for i in self.free_cells if i % 2 == 0])
        return None

    def easy_move(self):
        print('Making move level "easy"')
        return self.easy_check()

    def medium_move(self):
        print('Making move level "medium"')
        if self.medium_check():
            return self.medium_check()
        return self.easy_check()

    def hard_move(self):
        print('Making move level "hard"')
        if self.medium_check():
            return self.medium_check()
        elif self.hard_check():
            return self.hard_check()
        return self.easy_check()

    def user_move(self):
        while True:
            try:
                x, y = (int(i) for i in input('Enter the coordinates:').split())
                if any(not 1 <= c <= 3 for c in (x, y)):
                    raise MyError('Coordinates should be from 1 to 3!')
                elif self.field[(3 - y) * 3 + x - 1] != ' ':
                    raise MyError('This cell is occupied! Choose another one!')
            except ValueError:
                print('You should enter numbers!')
            except MyError as me:
                print(me)
            else:
                return (3 - y) * 3 + x - 1

    def play(self):
        players = {'user': self.user_move, 'easy': self.easy_move, 'medium': self.medium_move, 'hard': self.hard_move}
        for i in range(9):
            if i % 2 == 0:
                x = players[self.first]()
            else:
                x = players[self.second]()
            self.free_cells.remove(x)
            self.field[x] = self.char
            self.draw_field()
            if self.check():
                print(self.char, 'win\n')
                break
            self.char = self.change()
        else:
            print('Draw\n')


while True:
    command = input('Input command:').split()
    if command[0] == 'exit':
        break
    elif (len(command) == 3 and command[0] == 'start'
          and all(c in ('user', 'easy', 'medium', 'hard') for c in (command[1], command[2]))):
        game = TicTacToe(command[1], command[2])
        game.draw_field()
        game.play()
    else:
        print('Bad parameters')
