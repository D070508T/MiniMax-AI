#Main
import random
import time

from Board import Board
from MiniMax import MiniMax

while True:

    allCalls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0

    x = int(input('How many times would you like to run: '))

    start = time.time()
    for i in range(x):
        count += 1
        board = Board()
        minimax = MiniMax(board)

        while board.state() == 'continue':
            empty = 0
            for j in range(9):
                if board.board[j] == ' ':
                    empty += 1

            minimax.getBestMove(False)

            while True:
                num = random.randint(0, 8)
                if board.board[num] == ' ':
                    break

            allCalls[empty] += minimax.calls

            board.place(num, 'O')

            if board.state() == 'continue':
                board.place(minimax.getBestMove(True), 'X')

            allCalls[empty - 1] += minimax.calls

    elapsed = time.time() - start

    for i in range(1, 10):
        allCalls[i] = round(allCalls[i] / count, 1)
        print(f'{i} available moves: {allCalls[i]}')

    total = 0
    for call in allCalls:
        total += call

    print(f'''\ntotal calls: {total}\n
time elapsed: {round(elapsed*1000, 2)} milliseconds
time per run: {round((elapsed*1000) / count, 2)} milliseconds
time per call: {(elapsed*100000) / total} microseconds''')