# Write your test here

from challenge01 import Node, Tree , buildTree


tree1 = Tree()

def test_tree1():
    
    
    actual = buildTree(tree1.binaryTree([3,9,20,15,7],[9,3,15,20,7]))
    expect = [3, 9, 20, 'null', 'null', 15, 7]

    assert actual == expect
    # assert buildTree(tree1.binaryTree([3,9,20,15,7],[9,3,15,20,7])) == [3, 9, 20, 'null', 'null', 15, 7]

def test_tree2():
    
    
    actual = buildTree(tree1.binaryTree([4,3,6],[3,4,6]))
    expect = [4, 3, 6, 'null', 'null']

    assert actual == expect




