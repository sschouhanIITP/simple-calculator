from calculator import add, subtract, multiply, divide, power

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2  

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(10, 2) == 5
    
def test_power():
    assert power(2, 3) == 8

def test_divide_by_zero():
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."
    else:
        assert False, "Expected ValueError for division by zero"   

