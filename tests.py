import calculator

def test_power():
    assert calculator.power(2, 3) == 8

def test_multiply():
    assert calculator.multiply(5, 6) == 30

def test_add():
    assert calculator.add(2, 3) == 5

def test_square_root_():
    assert calculator.square_root(9) == 3.0

def test_divide():
    assert calculator.divide(10, 2) == 5.0
