#Minimax
class MiniMax:
    def __init__(self, board):
        self.board = board
        self.calls = 0
        self.tables = {}

    def availableMoves(self):
        moves = []
        for i in range(1, 10):
            if self.board.get(i) == ' ':
                moves.append(i)
        return moves

    def getBestMove(self, AI):
        self.calls = 0
        bestMove = None

        if AI:
            bestScore = -2
            for move in self.availableMoves():
                self.board.place(move, 'X')
                score = self.miniMax(False, 5)
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
                score = self.miniMax(True, 5)
                self.board.place(move, ' ')

                if score == -1:
                    return move

                if score < bestScore:
                    bestScore = score
                    bestMove = move
        return bestMove

    def miniMax(self, maximizing, limit):
        self.calls += 1

        if str(self.board) in self.tables:
            return self.tables[str(self.board)]

        state = self.board.state()

        if state == 'X':
            return 1
        elif state == 'O':
            return -1
        elif state == 'tie':
            return 0

        if maximizing:
            bestScore = -2
            for move in self.availableMoves():
                self.board.place(move, 'X')
                score = self.miniMax(False, limit-1)
                self.board.place(move, ' ')

                if score == 1:
                    self.tables[str(self.board)] = 1
                    return 1

                bestScore = max(bestScore, score)
        else:
            bestScore = 2
            for move in self.availableMoves():
                self.board.place(move, 'O')
                score = self.miniMax(True, limit-1)
                self.board.place(move, ' ')

                if score == -1:
                    self.tables[str(self.board)] = -1
                    return -1

                bestScore = min(bestScore, score)

        self.tables[str(self.board)] = bestScore

        return bestScore
