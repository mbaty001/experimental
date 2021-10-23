from find_my_number import check_if_move_is_possible, find_possible_movements, main, ROWS, COLS

def test_check_if_move_is_possible():
    assert check_if_move_is_possible(0, 0) == True
    assert check_if_move_is_possible(3, 0) == False
    assert check_if_move_is_possible(ROWS+1, 2) == False
    assert check_if_move_is_possible(1, COLS+2) == False
    assert check_if_move_is_possible(-1, 2) == False
    
def test_find_possible_movements():
    assert find_possible_movements(start_point=(0,0), key_sequence_length=1, total_key_sequences=0, no_of_vowels=1, length=1) == 1
    assert find_possible_movements(start_point=(0,0), key_sequence_length=1, total_key_sequences=0, no_of_vowels=1, length=2) == 2
    assert find_possible_movements(start_point=(0,1), key_sequence_length=1, total_key_sequences=0, no_of_vowels=0, length=2) == 3

def test_main():
    assert main(1) == 18
    assert main(2) == 60
    assert main(3) == 214
    assert main(4) == 732
    assert main(5) == 2486
    assert main(6) == 8392
    assert main(7) == 27912
    assert main(8) == 93204
    assert main(9) == 306288
    assert main(10) == 1013398
