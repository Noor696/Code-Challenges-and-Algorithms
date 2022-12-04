from challenge03 import Node,LinkedList,remove_nth_node

def test_remove_nth_node_1():

        
    linkedList1 = LinkedList()

    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    node3 = Node(3)
    linkedList1.append(node3)
    node4 = Node(4)
    linkedList1.append(node4)
    node4 = Node(5)
    linkedList1.append(node4)

    remove_nth_node(node1,3)
    
    actual = linkedList1.printAll()
    expect = [1,2,4,5]

    assert actual == expect


def test_remove_nth_node_2():

        
    linkedList2 = LinkedList()

    node1 = Node(1)
    linkedList2.append(node1)
    node2 = Node(2)
    linkedList2.append(node2)
  

    remove_nth_node(node1,1)
    
    actual = linkedList2.printAll()
    expect = [1]

    assert actual == expect


def test_remove_nth_node_3():

        
    linkedList3 = LinkedList()

    node1 = Node(1)
    linkedList3.append(node1)
    node2 = Node(2)
    linkedList3.append(node2)
    node3 = Node(3)
    linkedList3.append(node3)
  
    remove_nth_node(node1,2)
    
    actual = linkedList3.printAll()
    expect = [1,3]

    assert actual == expect


