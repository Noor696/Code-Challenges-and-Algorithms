# Write your test here
import pytest
from challenge03 import Node,Tree

tree1 = Tree()

def test_height_balanced_binary_tree1():
    root = tree1.convert_to_BST([1,2,3])
    tree1.tree_array = [root.value]

    actual = tree1.output_tree(root)
    expect = [2,1,3,'null','null','null','null',]

    assert actual == expect




