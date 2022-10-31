# Write your test here

from challenge02 import validate_Parentheses

def test_validate_Parentheses_case0():
    
    actual=validate_Parentheses("()")
    expect=True
    assert actual==expect

def test_validate_Parentheses_case1():

    actual=validate_Parentheses("()[]{}")
    expect=True
    assert actual==expect

def test_validate_Parentheses_case2():
    actual=validate_Parentheses("[({}]")
    expect=False
    assert actual==expect

def test_validate_Parentheses_case3():
    actual=validate_Parentheses("[(hello)()]")
    expect=True
    assert actual==expect

def test_validate_Parentheses_case4():
    actual=validate_Parentheses("[{(())}]")
    expect=True
    assert actual==expect
