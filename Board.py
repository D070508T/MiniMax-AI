#Board
class Board:
    # Constructor that builds the board and sets it to empty
    def __init__(self, board=None):
        if board:
            self.board = [row[:] for row in board.board]
        else:
            self.board = [
                [' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']
            ]

    # Function that takes a number and a character and places that character in the correct spot of the given number
    def place(self, num, char):
        self.board[(num - 1) // 3][(num - 1) % 3] = char

    # Function that returns the value inside the spot of the given number
    def get(self, n):
        return self.board[(n - 1) // 3][(n - 1) % 3]

    # Function that returns the state of the board. Who won, or if the game is still continuing, or if it's a tie
    def state(self):
        for i in range(3):
            # Check row
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]

            # Check column
            if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return 'continue'
        return 'tie'

    # Function that checks if a board is unique
    def unique(self, boards):
        for other in boards:
            if self.board == other.board:
                return False
        return True