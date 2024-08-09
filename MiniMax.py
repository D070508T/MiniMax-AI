from Board import Board


class MiniMax:
    def __init__(self, board):
        self.board = board
        self.calls = 0
        self.tables = {}

    def availableMoves(self):
        moves = []
        for i in (4, 0, 2, 6, 8, 1, 3, 5, 7):
            if self.board.get(i) == ' ':
                moves.append(i)
        return moves

    def oppositeValue(self, num):
        if num == 1:
            return -1
        if num == -1:
            return 1
        return 0

    def addBoard(self, board, value):
        for var in board.variations():
            self.tables[str(var)] = value

            inverted = ''
            for char in str(var):
                if char == 'X':
                    inverted += 'O'
                elif char == 'O':
                    inverted += 'X'
                else:
                    inverted += ' '

            self.tables[inverted] = self.oppositeValue(value)

    def getBestMove(self, AI):
        self.calls = 0
        bestMove = None

        if AI:
            bestScore = -2
            for move in self.availableMoves():
                self.board.place(move, 'X')
                score = self.miniMax(False)
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
                score = self.miniMax(True)
                self.board.place(move, ' ')

                if score == -1:
                    return move

                if score < bestScore:
                    bestScore = score
                    bestMove = move
        return bestMove

    def miniMax(self, maximizing):
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
                score = self.miniMax(False)
                self.board.place(move, ' ')

                if score == 1:
                    self.addBoard(Board(self.board), 1)
                    return 1

                bestScore = max(bestScore, score)
        else:
            bestScore = 2
            for move in self.availableMoves():
                self.board.place(move, 'O')
                score = self.miniMax(True)
                self.board.place(move, ' ')

                if score == -1:
                    self.addBoard(Board(self.board), -1)
                    return -1

                bestScore = min(bestScore, score)

        self.addBoard(Board(self.board), bestScore)

        return bestScore
