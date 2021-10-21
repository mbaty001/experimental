from find_my_number import check_if_move_is_possible, find_possible_movements, main

matrix = [ ['A','B','C','D','E'], ['F','G','H','I','J'], ['K','L','M','N','O'], ['',1,2,3,'' ] ]
rows = len(matrix)
cols = len(matrix[0])
vowels = [ [x,y] for x in range(rows) for y in range(cols) if matrix[x][y] and str(matrix[x][y]).lower() in 'aeiou' ]
empties = [ [x,y] for x in range(rows) for y in range(cols) if not matrix[x][y] ]

def test_check_if_move_is_possible():
    assert check_if_move_is_possible(0, 0) == True
    assert check_if_move_is_possible(3, 0) == False
    assert check_if_move_is_possible(rows+1, 2) == False
    assert check_if_move_is_possible(1, cols+2) == False
    assert check_if_move_is_possible(-1, 2) == False
    
def test_find_possible_movements():
    assert find_possible_movements(start_point=(0,0), key_sequence=[(0,0)], total_key_sequences=0, no_of_vowels=1, length=1) == 1
    assert find_possible_movements(start_point=(0,0), key_sequence=[(0,0)], total_key_sequences=0, no_of_vowels=1, length=2) == 2
    assert find_possible_movements(start_point=(0,1), key_sequence=[(0,1)], total_key_sequences=0, no_of_vowels=0, length=2) == 3

def test_main():
    assert main(1) == 18
    assert main(2) == 59
    assert main(3) == 199
    assert main(4) == 623
    assert main(5) == 1926
    assert main(6) == 5889
    assert main(7) == 17885
    assert main(8) == 54786
    assert main(9) == 165686
    assert main(10) == 506242