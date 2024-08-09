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

    # Rotates board
    def rotate(self):
        copy = [row[:] for row in self.board]

        self.board = [
            [copy[2][0], copy[1][0], copy[0][0]],
            [copy[2][1], copy[1][1], copy[0][1]],
            [copy[2][2], copy[1][2], copy[0][2]],
        ]

    # Mirrors board
    def mirror(self, num):
        if num % 2 == 0:
            temp = [self.board[0][0], self.board[1][0], self.board[2][0]]
            self.board[0][0], self.board[1][0], self.board[2][0] = self.board[0][2], self.board[1][2], self.board[2][2]
            self.board[0][2], self.board[1][2], self.board[2][2] = temp
        else:
            temp = self.board[0]
            self.board[0] = self.board[2]
            self.board[2] = temp

    # Returns all variations of the board
    def variations(self):
        variations = [Board(self)]

        newBoard = Board(self)

        for i in range(3):
            newBoard.mirror(i)
            variations.append(str(Board(newBoard)))
            for j in range(3):
                newBoard.rotate()
                variations.append(str(Board(newBoard)))

        return variations

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

    # Function that returns a string representation of the board
    def __str__(self):
        raw = ''
        for row in self.board:
            for char in row:
                raw += char
        return raw