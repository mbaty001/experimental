from find_my_number_improved import main

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
