class Node:

    def __init__(self,value=None):
        self.value=value

    def __str__(self):
        return self.value

class Edge:

    def __init__(self,vertex,weight=0):

        self.vertex=vertex
        self.weight=weight

class Graph:

    def __init__(self):

        self.adj_list={}
        
        self.visited=[]

    def add_node(self,node):

        nodei=Node(node)
        self.adj_list[nodei]=[]

        return nodei

    def add_edge(self,node1,node2,weight=0):

        if not node1 in self.adj_list.keys():
            print( 'node not exist')

        if not node2 in self.adj_list.keys():
            print( 'node not exist')

        edge1=Edge(node2)
        self.adj_list[node1].append(edge1)

        edge2=Edge(node1)
        self.adj_list[node2].append(edge2)

    def __str__(self) :

        output=''

        for key in self.adj_list.keys():
            output += f'{key} -> '

            for edge in self.adj_list[key]:
                output += f'{edge.vertex} -> '

            output+= '\n'

        return output


    def breadthFirst(self,root):

        if root.value in self.visited:
            return root.value

        self.visited.append(root.value)

        if self.adj_list[root]:
            for node in self.adj_list[root]:
                self.breadthFirst(node.vertex)
                
        else:
            return 'Not Found Edges'

        return self.visited


if __name__=='__main__':

    print('Graph1\n')

    graph1=Graph()

    a=graph1.add_node('a')
    b=graph1.add_node('b')
    c=graph1.add_node('c')
    d=graph1.add_node('d')
    e=graph1.add_node('e')
    f=graph1.add_node('f')
    g=graph1.add_node('g')
    h=graph1.add_node('h')
    i=graph1.add_node('i')
    k=graph1.add_node('k')

    # graph1.add_edge(a,c)
    # graph1.add_edge(a,e)
    # graph1.add_edge(a,b)

    # graph1.add_edge(c,f)

    # graph1.add_edge(b,d)

    # graph1.add_edge(e,g)
    # graph1.add_edge(e,d)

    # graph1.add_edge(f,i)
    # graph1.add_edge(f,h)
    
    # graph1.add_edge(i,k)
    graph1.add_edge(a,c)
    graph1.add_edge(a,e)
    graph1.add_edge(a,b)

    graph1.add_edge(b,d)
    graph1.add_edge(e,g)
    graph1.add_edge(c,f)
    graph1.add_edge(e,f)
    graph1.add_edge(d,e)
    graph1.add_edge(g,h)
    graph1.add_edge(f,i)
    graph1.add_edge(f,h)

    graph1.add_edge(h,k)
    graph1.add_edge(i,k)


    print(graph1.breadthFirst(a))

    print('Graph2********\n')

    graph2=Graph()

    a=graph2.add_node('a')
    b=graph2.add_node('b')
    c=graph2.add_node('c')
    d=graph2.add_node('d')

    graph2.add_edge(a,b)
    graph2.add_edge(a,c)
    graph2.add_edge(b,c)
    graph2.add_edge(c,d)

    print(graph2.breadthFirst(a)) # expect=['a', 'b', 'c', 'd']

    print('GraphEdge********\n')

    graphE=Graph()

    n=graphE.add_node('n')
    m=graphE.add_node('m')

    print(graphE.breadthFirst(n))