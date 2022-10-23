# Write here the code challenge solution
class Node:

    def __init__(self , value):
        self.value = value
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
        LinkedList.length +=1

    def prepend(self,node):
        '''add node in beginning linked list'''
        pass

    def insert(self):
        pass

    def deletenode(self, node):
        # node.val  = node.next.val
        # node.next = node.next.next
        current = self.head
        
        if current.value == node:
            self.head = current.next
        else: 
            while current is not None:
                prev_node = current
                current = current.next
            prev_node.next = current.next
                
        

	    

