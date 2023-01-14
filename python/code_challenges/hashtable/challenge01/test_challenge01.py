# Write your test here
import pytest
from challenge01 import TwoSumBST
# from linked_list import Node, LinkedList
from NodeTreeClasses import*

@pytest.fixture
def tree1():
    tree=Tree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.left.right = Node(4)
    tree.root.left.left = Node(2) 
    tree.root.right.right = Node(7)

    return tree.root

@pytest.fixture
def tree2():
    tree=Tree()
    tree.root = Node(5)
    tree.root.left = None
    tree.root.right = None

    return tree.root

@pytest.fixture
def tree3():
    tree=Tree()
    tree.root = None

    return tree.root

@pytest.fixture
def tree4():
    tree=Tree()
    tree.root = Node(7)
    tree.root.left = Node(2)
    tree.root.right = Node(9)
    tree.root.left.left = Node(1) 
    tree.root.left.right = Node(5)
    tree.root.right.right = Node(14)
    
    return tree.root

def test_1(tree1):
    assert TwoSumBST(tree1,3)==False
    assert TwoSumBST(tree1,9)==True
    assert TwoSumBST(tree1,28)==False

def test_2(tree2):
    assert TwoSumBST(tree2,3)==False

def test_3(tree3):
    assert TwoSumBST(tree3,3)==False

def test_4(tree4):
    assert TwoSumBST(tree4,3)==True




    