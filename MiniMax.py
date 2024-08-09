class MiniMax:
    def __init__(self, board):
        self.priority_order = (5, 1, 3, 7, 9, 2, 4, 6, 8)  # Center, corners, edges
        self.board = board
        self.calls = 0
        self.boards = {}

    def addBoard(self, board, value):
        self.boards[board] = value

        for var in board.variations():
            self.boards[var] = value

            for i in range(9):
                newVar = var.board
                if var.board[i] == 'X':
                    newVar = var.board[:i] + 'O' + var.board[i+1:]
                elif var.board[i] == 'O':
                    newVar = var.board[:i] + 'X' + var.board[i+1:]

                if i != len(var.board) - 1:
                    newVar += var.board[i+1:]

            if value == 1:
                value = -1
            elif value == -1:
                value = 1

            self.boards[var.board] = value

    def availableMoves(self):
        moves = []
        for i in self.priority_order:
            if self.board.board[i - 1] == ' ':
                moves.append(i)
        return moves

    def getBestMove(self, AI):
        self.calls = 0
        bestMove = None

        if AI:
            bestScore = -2
            for move in self.availableMoves():
                self.board.place(move, 'X')
                score = self.miniMax(False, 4)
                self.board.place(move, ' ')

                if score == 1:
                    return move

                if score > bestScore:
                    bestScore = score
                    bestMove = move
        else:
            bestScore = 2
            for move in self.availableMoves():
                self.board.place(move, 'O')
                score = self.miniMax(True, 4)
                self.board.place(move, ' ')

                if score == -1:
                    return move

                if score < bestScore:
                    bestScore = score
                    bestMove = move
        return bestMove

    def miniMax(self, maximizing, limit):
        self.calls += 1
        limit -= 1

        if self.board in self.boards:
            return self.boards[self.board]

        state = self.board.state()

        if state == 'X':
            self.addBoard(self.board, 1)
            return 1
        elif state == 'O':
            self.addBoard(self.board, -1)
            return -1
        elif state == 'tie' or limit <= 0:
            self.addBoard(self.board, 0)
            return 0

        if maximizing:
            bestScore = -2
            for move in self.availableMoves():
                self.board.place(move, 'X')
                score = self.miniMax(False, 4)
                self.board.place(move, ' ')

                if score == 1:
                    self.addBoard(self.board, 1)
                    return 1

                bestScore = max(bestScore, score)
        else:
            bestScore = 2
            for move in self.availableMoves():
                self.board.place(move, 'O')
                score = self.miniMax(True, 4)
                self.board.place(move, ' ')

                if score == -1:
                    self.addBoard(self.board, -1)
                    return -1

                bestScore = min(bestScore, score)

        self.boards[self.board] = bestScore
        return bestScore