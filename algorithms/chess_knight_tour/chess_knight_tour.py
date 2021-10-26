'''
solves knight tour problem using backtracking
'''

import sys

BOARD_SIZE = int(sys.argv[1])
JUMPS = ((2,1), (1,2), (2,-1), (-2,1), (-2,-1), (1,-2), (-1,2), (-1,-2))

def move(x, y, sequence):
    board[x][y] = sequence
    if sequence == BOARD_SIZE**2:
        return True
    for jump in JUMPS:
        temp_x = x + jump[0]
        temp_y = y + jump[1]

        if 0<=temp_x<BOARD_SIZE and 0<=temp_y<BOARD_SIZE and board[temp_x][temp_y] == 0:
            if move(temp_x, temp_y, sequence+1):
                return True
    # Backtracking
    board[x][y] = 0
    return False

if __name__ == "__main__":

    board = [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

    if move(0, 0, 1):
        for i in range(BOARD_SIZE):
            print(board[i])
    else:
        print('There is no solution')

