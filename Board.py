class Board:
    # Constructor that builds the board and sets it to empty
    def __init__(self, board=' '*16):
        self.winning_combinations = (
            (0, 1, 2),
            (1, 2, 3),

            (4, 5, 6),
            (5, 6, 7),

            (5, 9, 10),
            (9, 10, 11),

            (12, 13, 14),
            (13, 14, 15),

            (0, 4, 8),
            (4, 8, 12),

            (1, 5, 9),
            (5, 9, 13),

            (2, 6, 10),
            (6, 10, 14),

            (3, 7, 11),
            (7, 11, 15),

            (2, 5, 8),
            (7, 10, 13),

            (3, 6, 9),
            (6, 9, 12),

            (1, 6, 11),
            (4, 9, 14),

            (0, 5, 10),
            (5, 10, 15)
        )

        self.board = board

    def rotate(self):
        return (self.board[3] + self.board[7] + self.board[11] + self.board[15] +
                self.board[2] + self.board[6] + self.board[10] + self.board[14] +
                self.board[1] + self.board[5] + self.board[9] + self.board[13] +
                self.board[0] + self.board[4] + self.board[8] + self.board[12])

    def mirror(self, num):
        if num % 2 == 0:
            return self.board[12:] + self.board[8:12] + self.board[4:8] + self.board[0:4]
        return (self.board[3] + self.board[2] + self.board[1] + self.board[0] +
                self.board[7] + self.board[6] + self.board[5] + self.board[4] +
                self.board[11] + self.board[10] + self.board[9] + self.board[8] +
                self.board[15] + self.board[14] + self.board[13] + self.board[12])

    def variations(self):
        variations = [self.board]

        newBoard = Board(self.board)

        for i in range(3):
            newBoard.board = newBoard.mirror(i)
            variations.append(newBoard.board)
            for j in range(3):
                newBoard.board = newBoard.rotate()
                variations.append(newBoard.board)
            newBoard.board = newBoard.rotate()

        return variations

    # Function that takes a number and a character and places that character in the correct spot of the given number
    def place(self, num, char):
        oldBoard = self.board

        self.board = self.board[:num - 1] + char

        if num < 16:
            self.board += oldBoard[num:]

    # Function that returns the state of the board. Who won, or if the game is still continuing, or if it's a tie
    def state(self):
        for a, b, c in self.winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                return self.board[a]  # Return 'X' or 'O'

        # If no winner, check if the board is full, meaning it's a tie, or if the game is still on
        if ' ' not in self.board:
            return 'tie'
        return 'continue'

    # Function that checks if a board is unique
    def unique(self, boards):
        if self.board in boards:
            return False
        return True
