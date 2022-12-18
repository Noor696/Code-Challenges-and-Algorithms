# Write here the code challenge solution
import pytest
from linked_list import LinkedList , Node
from challenge02 import HashTabel, First_Repeated_Word

def test_first_repeted_word_1():

    actual = First_Repeated_Word("ASAC is a department at LTUC. ASAC teaches programming in LTUC .")
    expect = "ASAC"

    assert actual==expect

def test_first_repeted_word_2():

    actual = First_Repeated_Word("I am learning programming at ASAC .")
    expect = "No Repetition"

    assert actual==expect

def test_first_repeted_word_3():

    actual = First_Repeated_Word("The soup was stirred and stirred until thickened")
    expect = "stirred"

    assert actual==expect


