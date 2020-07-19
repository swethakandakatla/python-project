import pytest

@pytest.mark.one
def method1():
    a=5
    b=7
    assert a==b

@pytest.mark.two
def method2():
    a=14
    b=17
    assert a+3==b