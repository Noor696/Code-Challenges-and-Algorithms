class Node:

    ''' 
    node class have two property:
    value : the user input the value.
    next : (pointer) at the first time the next should refer to the null.
     '''

    def __init__(self , value):
        self.value = value
        self.next = None

class LinkedList:

   
    #firstly when initilize the linkedlist is contains only "head" and the head refer to the null.
    def __init__(self):
        self.head=None


    def append(self,node):
        '''
        method allow me to append the node in the end of linkedlist 
        (take the value from the user, create a node, put value, append value into linkedlist, head= new node )
        '''

        if self.head == None: # edge case: if linkedlist is empty
            self.head = node  # head ~= pointer

        else: 
            current_node = self.head 

            while current_node.next is not None:  # the while loop is stop when the the current node pointer to null.

                current_node = current_node.next

            current_node.next = node

    def printAll(self):
        if self.head is None:
            return []
        else:
            current = self.head
            link_output=[]
            while current is not None:
                link_output.append(current.value)  # put the value inside linkedlist output
                current = current.next
            return link_output


    

if __name__== "__main__":

    
    linkedList1 = LinkedList()

    node1 = Node("A")
    linkedList1.append(node1)
    node2 = Node("B")
    linkedList1.append(node2)
    node3 = Node("C")
    linkedList1.append(node3)
    node4 = Node("D")
    linkedList1.append(node4)



