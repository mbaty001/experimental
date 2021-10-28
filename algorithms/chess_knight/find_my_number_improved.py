"""
Find My Number solution by michal.batyra@gmail.com
"""

MATRIX = [ ['A','B','C','D','E'], ['F','G','H','I','J'], ['K','L','M','N','O'], ['',1,2,3,'' ] ]
ROWS = len(MATRIX)
COLS = len(MATRIX[0])
VOWELS = { (x,y) for x in range(ROWS) for y in range(COLS) if MATRIX[x][y] and str(MATRIX[x][y]).lower() in 'aeiou' }
KNIGHT_JUMPS = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))

possible_moves = {}
for x in range(ROWS):
    for y in range(COLS):
        if MATRIX[x][y] == '':
            continue
        for jump in KNIGHT_JUMPS:
            tx = x + jump[0]
            ty = y + jump[1]
            if 0<=tx<ROWS and 0<=ty<COLS and MATRIX[tx][ty] != '':
                possible_moves.setdefault((x, y), []).append((tx, ty))

def find_possible_movements(start_point, key_sequence_length, total_key_sequences, no_of_vowels, length):
    ''' count the key_sequences with the given length '''

    if key_sequence_length == length:
        return total_key_sequences + 1

    for point in possible_moves[start_point]:
        if no_of_vowels < 2 or point not in VOWELS:
            total_key_sequences = find_possible_movements(point, 
                                                          key_sequence_length+1,
                                                          total_key_sequences,
                                                          no_of_vowels+int(point in VOWELS),
                                                          length)
    return total_key_sequences

def main(length):
    ''' entrypoint '''
    total_key_sequences = 0
    for start_point in possible_moves.keys():
        no_of_vowels = 1 if start_point in VOWELS else 0
        key_sequence_length = 1
        total_key_sequences += find_possible_movements(start_point, key_sequence_length, 0, no_of_vowels, length)
    return total_key_sequences

if __name__ == "__main__":
    key_sequence_length = 10
    print(main(key_sequence_length))
