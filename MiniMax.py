class MiniMax:
    def __init__(self, board):
        self.priority_order = (5, 6, 9, 10, 0, 3, 12, 15, 1, 2, 4, 8, 7, 11, 13, 14)  # Center, corners, edges
        self.board = board
        self.calls = 0
        self.boards = {}

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
                score = self.miniMax(False, 2)
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
                score = self.miniMax(True, 2)
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

        for b in self.board.variations():
            if b in self.boards:
                return self.boards[self.board]
            newStr = ''
            for char in b:
                if char == 'O':
                    newStr += 'X'
                elif char == 'X':
                    newStr += 'O'
                else:
                    newStr += ' '
            if newStr in self.boards:
                val = self.boards[newStr]
                if val == 1:
                    return -1
                elif val == -1:
                    return 1
                else:
                    return 0

        state = self.board.state()

        if state == 'X':
            self.boards[self.board.board] = 1
            return 1
        elif state == 'O':
            self.boards[self.board.board] = -1
            return -1
        elif state == 'tie' or limit <= 0:
            self.boards[self.board.board] = 0
            return 0

        if maximizing:
            bestScore = -2
            for move in self.availableMoves():
                self.board.place(move, 'X')
                score = self.miniMax(False, 2)
                self.board.place(move, ' ')

                if score == 1:
                    self.boards[self.board.board] = 1
                    return 1

                bestScore = max(bestScore, score)
        else:
            bestScore = 2
            for move in self.availableMoves():
                self.board.place(move, 'O')
                score = self.miniMax(True, 2)
                self.board.place(move, ' ')

                if score == -1:
                    self.boards[self.board.board] = -1
                    return -1

                bestScore = min(bestScore, score)

        self.boards[self.board] = bestScore
        return bestScore
