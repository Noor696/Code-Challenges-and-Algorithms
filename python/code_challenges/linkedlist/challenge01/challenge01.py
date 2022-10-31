# Write here the code challenge solution
class Node:

    def __init__(self , node):
        self.value = node
        self.next = None



class LinkedList:
    
    def __init__(self):
        self.head=None

    def append(self,node):
        '''add node in last linked list'''

        if self.head is None:
            self.head = node

        else: 
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next

            current_node.next=node

    def display(self):
        '''return a list of linked list elements'''
        new_arr=[]    
        
        current = self.head
        while current is not None:
            
              new_arr.append(current.value)  
              current = current.next
              
        return new_arr


def deletenode(node):
    '''function to delete a node in a singly-linked list.'''

    next_node=node.next
    node.value  = next_node.value
    node.next = next_node.next
    next_node.next=None
    del(next_node)


if __name__ == "__main__":

 linkedList1 = LinkedList()

 node1 = Node("A")
 linkedList1.append(node1)

 node2 = Node("B")
 linkedList1.append(node2)

 node3 = Node("C")
 linkedList1.append(node3)

 node4 = Node("D")
 linkedList1.append(node4)

 deletenode(node2)   

 print(linkedList1.display())           
        

	    

