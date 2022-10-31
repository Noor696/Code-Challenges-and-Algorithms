# Write your test here
import pytest
from challenge01 import Node,LinkedList,deletenode

def test_delete():
    '''
    test delete method 
    '''
    
    linkedList1 = LinkedList()
    node1 = Node("A")
    linkedList1.append(node1)

    node2 = Node("B")
    linkedList1.append(node2)

    node3 = Node("C")
    linkedList1.append(node3)

    node4 = Node("D")
    linkedList1.append(node4)

    deletenode(node3)

    actual=linkedList1.display()
    expect= ['A', 'B', 'D']
    
    assert actual == expect


def test_delete_head():
    '''
    test delete method 
    '''
    
    linkedList1 = LinkedList()

    node1 = Node("A")
    linkedList1.append(node1)

    node2 = Node("B")
    linkedList1.append(node2)

    node3 = Node("C")
    linkedList1.append(node3)

    node4 = Node("D")
    linkedList1.append(node4)

    deletenode(node1)

    actual=linkedList1.display()
    expect= ["B" ,"C", "D"]
    
    assert actual == expect