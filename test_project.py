import pytest
from project import add,subtract,multiply,divide



def test_add():
    assert add(20,5) == 25.0
    assert add(10,5) == 15.0


def test_subtract():

    assert subtract(10,5) == 5.0
    assert subtract(10,2) == 8.0

def test_multiply():

    assert multiply(10,5) == 50.0
    assert multiply(10,2) == 20.0

def test_divide():

    assert divide(10,5) == 2.0
    assert divide(10,2) == 5.0
    assert divide(10, 0) is None

    






