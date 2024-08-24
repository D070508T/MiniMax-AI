class Board:
    # Constructor that builds the board and sets it to empty if none given
    def __init__(self, board=None):
        self.winning_combinations = (
            (0, 1, 2),  # Row 1
            (3, 4, 5),  # Row 2
            (6, 7, 8),  # Row 3
            (0, 3, 6),  # Column 1
            (1, 4, 7),  # Column 2
            (2, 5, 8),  # Column 3
            (0, 4, 8),  # Diagonal 1
            (2, 4, 6)   # Diagonal 2
        )

        if board:
            self.board = board.board
        else:
            self.board = '         '

    def rotate(self):
        return (self.board[6] + self.board[3] + self.board[0] +
                self.board[7] + self.board[4] + self.board[1] +
                self.board[8] + self.board[5] + self.board[2])

    def mirror(self, num):
        if num % 2 == 0:
            return self.board[6:9] + self.board[3:6] + self.board[0:3]
        return (self.board[2] + self.board[1] + self.board[0] +
                self.board[5] + self.board[4] + self.board[3] +
                self.board[8] + self.board[7] + self.board[6])

    def variations(self):
        variations = []

        newBoard = Board(self)

        for i in range(3):
            newBoard.mirror(i)
            variations.append(Board(newBoard))
            for j in range(3):
                newBoard.rotate()
                variations.append(Board(newBoard))

        return variations

    # Function that takes a number and a character and places that character in the correct spot of the given number
    def place(self, num, char):
        oldBoard = self.board

        self.board = self.board[:num - 1] + char

        if num < 9:
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
