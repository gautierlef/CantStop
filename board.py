class Board:
    def __init__(self):
        self.board = []
        for i in range(6):
            self.board.append(['-'] * (3 + i * 2))
        for i in range(5):
            self.board.append(['-'] * (11 - i * 2))

    def lock_snap_hook(self):
        for column in range(len(self.board)):
            for step in range(len(self.board[column])):
                self.board[column][step] = self.board[column][step].capitalize()

    def put_climber(self, column, player):
        if player == 0:
            if 'x' in self.board[column]:
                self.board[column][self.board[column].index('x')] = '-'
                self.board[column][self.board[column].index('x') + 1] = 'x'
            elif 'X' in self.board[column]:
                self.board[column][self.board[column].index('x') + 1] = 'x'
            else:
                self.board[column][0] = 'x'
        else:
            if 'o' in self.board[column]:
                self.board[column][self.board[column].index('o')] = '-'
                self.board[column][self.board[column].index('o') + 1] = 'o'
            elif 'O' in self.board[column]:
                self.board[column][self.board[column].index('O') + 1] = 'o'
            else:
                self.board[column][0] = 'o'

    def remove_climber(self, player):
        for column in range(len(self.board)):
            for step in range(len(self.board[column])):
                if self.board[column][step] == 'x' or self.board[column][step] == 'o':
                    self.board[column][step] = '-'

    def show_board(self):
        i = 2
        for column in self.board:
            if i < 10:
                print(str(i) + '  : ' + str(column))
            else:
                print(str(i) + ' : ' + str(column))
            i += 1
