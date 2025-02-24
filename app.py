#Main
import random
import time

from Board import Board
from MiniMax import MiniMax

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
        for j in range(1, 10):
            if board.get(j) == ' ':
                empty += 1

        minimax.getBestMove(False)

        while True:
            num = random.randint(1, 9)
            if board.get(num) == ' ':
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
time elapsed: {round(elapsed, 2)} seconds
time per run: {round(elapsed / count, 2)} seconds
time per call: {elapsed / total} seconds''')