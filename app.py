import random
import time

from Board import Board
from MiniMax import MiniMax

allCalls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x = int(input('How many times would you like to run: '))

start = time.time()
for i in range(x):
    board = Board()
    minimax = MiniMax(board)

    while board.state() == 'continue':
        empty = 0
        for j in range(16):
            if board.board[j] == ' ':
                empty += 1

        minimax.getBestMove(False)

        while True:
            num = random.randint(0, 15)
            if board.board[num] == ' ':
                break

        allCalls[empty] += minimax.calls

        board.place(num, 'O')

        if board.state() == 'continue':
            board.place(minimax.getBestMove(True), 'X')

        allCalls[empty - 1] += minimax.calls

elapsed = time.time() - start

for i in range(1, 17):
    allCalls[i] = round(allCalls[i] / x, 1)
    print(f'{i} available moves: {allCalls[i]}')

total = 0
for call in allCalls:
    total += call

print(f'''\ntotal calls: {total}\n
time elapsed: {round(elapsed * 1_000, 5)} milliseconds
time per run: {round((elapsed / x) * 1_000, 5)} milliseconds
time per call: {round((elapsed / total) * 1_000, 5)} milliseconds''')
