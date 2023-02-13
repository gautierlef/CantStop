class Board:
    def __init__(self, character):
        self.board = []
        self.character = character
        for i in range(6):
            self.board.append(['-'] * (3 + i * 2))
        for i in range(5):
            self.board.append(['-'] * (11 - i * 2))

    def put_climber(self, column):
        column = column - 2
        if self.character.capitalize() in self.board[column]:
            self.board[column][self.board[column].index(self.character.capitalize()) + 1] = self.character
            self.board[column][self.board[column].index(self.character.capitalize())] = '-'
        elif self.character in self.board[column]:
            self.board[column][self.board[column].index(self.character) + 1] = self.character
            self.board[column][self.board[column].index(self.character)] = '-'
        else:
            self.board[column][0] = self.character

    def remove_climbers(self):
        for column in range(len(self.board)):
            for step in range(len(self.board[column])):
                if self.board[column][step] == self.character or self.board[column][step] == self.character:
                    self.board[column][step] = '-'

    def lock_snap_hook(self):
        for column in range(len(self.board)):
            for step in range(len(self.board[column])):
                self.board[column][step] = self.board[column][step].capitalize()

    def is_snap_hook_on_top(self, column):
        if self.character.capitalize() in column:
            if column.index(self.character.capitalize()) + 1 == len(column):
                return True
        return False

    def is_win(self):
        count = 0
        for column in self.board:
            if self.is_snap_hook_on_top(column):
                count += 1
        if count >= 3:
            return True
        return False

    def is_valid_move(self, column):
        column = column - 2
        if self.character.capitalize() in self.board[column]:
            if self.board[column].index(self.character.capitalize()) + 1 == len(self.board[column]):
                return False
            return True
        elif self.character in self.board[column]:
            if self.board[column].index(self.character) + 1 == len(self.board[column]):
                return False
        return True

    def show_board(self):
        i = 2
        for column in self.board:
            if i < 10:
                print(str(i) + '  : ' + str(column))
            else:
                print(str(i) + ' : ' + str(column))
            i += 1
