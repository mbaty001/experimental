"""
Find My Number solution by michal.batyra@gmail.com
"""

MATRIX = [ ['A','B','C','D','E'], ['F','G','H','I','J'], ['K','L','M','N','O'], ['',1,2,3,'' ] ]
ROWS = len(MATRIX)
COLS = len(MATRIX[0])
VOWELS = [ [x,y] for x in range(ROWS) for y in range(COLS) if MATRIX[x][y] and str(MATRIX[x][y]).lower() in 'aeiou' ]
EMPTIES = [ [x,y] for x in range(ROWS) for y in range(COLS) if not MATRIX[x][y] ]

def find_possible_movements(start_point, key_sequence, total_key_sequences, no_of_vowels, length):
    ''' count the key_sequences with the given length '''

    if len(key_sequence) == length:
        return total_key_sequences + 1

    (x, y) = start_point

    jumps = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
    for jump in jumps:
        tx = x + jump[0]
        ty = y + jump[1]
        if check_if_move_is_possible(tx, ty):
            if no_of_vowels < 2 or [tx, ty] not in VOWELS:
                key_sequence_copy = key_sequence + [(tx, ty)]
                if [tx, ty] in VOWELS:
                    total_key_sequences = find_possible_movements((tx, ty), key_sequence_copy, total_key_sequences, no_of_vowels+1, length)
                else:
                    total_key_sequences = find_possible_movements((tx, ty), key_sequence_copy, total_key_sequences, no_of_vowels, length)
    return total_key_sequences

def check_if_move_is_possible(tx, ty):
    ''' Verify if the move is not outside of chessboard '''
    return 0<=tx<ROWS and 0<=ty<COLS and [tx, ty] not in EMPTIES

def main(length):
    ''' entrypoint '''
    total_key_sequences = 0
    for startx in range(ROWS):
        for starty in range(COLS):
            start_point = [startx, starty]
            if start_point in EMPTIES:
                continue
            no_of_vowels = 1 if start_point in VOWELS else 0
            key_sequence = [start_point]
            total_key_sequences += find_possible_movements(start_point, key_sequence, 0, no_of_vowels, length)
    return total_key_sequences

if __name__ == "__main__":
    key_sequence_length = 10
    print(main(key_sequence_length))
