import sys

BOARD_SIZE = int(sys.argv[1])
JUMPS = ((2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2))

def move(x, y, sequence):
    board[x][y] = sequence
    if sequence == BOARD_SIZE * BOARD_SIZE:
        for i in range(BOARD_SIZE):
            print(board[i])
        return
    for jump in JUMPS:
        temp_x = x + jump[0]
        temp_y = y + jump[1]

        if 0<=temp_x<BOARD_SIZE and 0<=temp_y<BOARD_SIZE and board[temp_x][temp_y] == 0:
            move(temp_x, temp_y, sequence+1)
    board[x][y] = 0

if __name__ == "__main__":

    board = []
    for i in range(BOARD_SIZE):
        board.append(BOARD_SIZE * [0])

    move(0, 0, 1)
