# Write your test here
import pytest
from challenge01 import MyQueue

def test_queue_push():

    queue_1=MyQueue()

    queue_1.push("A")
    queue_1.push("B")
    queue_1.push("C")
    queue_1.push("D")

    actual=queue_1.queue
    expect=["A","B","C","D"]
    
    assert actual == expect


def test_queue_pop():

    queue_2=MyQueue()
    queue_2.push("A")
    queue_2.push("B")
    queue_2.push("C")
    queue_2.push("D")
    
    actual=queue_2.pop(),queue_2.queue
    expect="A",["B","C","D"]

    assert actual == expect

def test_queue_peek():

    queue_3=MyQueue()
    queue_3.push("A")
    queue_3.push("B")

    actual=queue_3.peek()
    expect= "A"

    assert actual == expect


def test_queue_empty():

    queue_4=MyQueue()
    queue_4.push("A")
    queue_4.push("B")

    actual=queue_4.empty()
    expect= False

    assert actual == expect
