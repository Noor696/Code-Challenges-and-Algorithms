from challenge01 import *

def test_2():
    
    graph2=Graph()

    a=graph2.add_node('a')
    b=graph2.add_node('b')
    c=graph2.add_node('c')
    d=graph2.add_node('d')

    graph2.add_edge(a,b)
    graph2.add_edge(a,c)
    graph2.add_edge(c,d)


    actual=graph2.breadthFirst(a)
    expect=['a', 'b', 'c', 'd']
    assert actual == expect

def test_Edge():

    graphE=Graph()

    n=graphE.add_node('n')
    m=graphE.add_node('m')

    actual = graphE.breadthFirst(n)
    expect = "Not Found Edges"

    assert actual == expect