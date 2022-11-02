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
        # LinkedList.length +=1

    def prepend(self,node):
        '''add node in beginning linked list'''
        pass

    def display(self):
        
        output=[]
        
        current = self.head
        while current is not None:
            output.append(current.value)
                
            current = current.next

        return output



def middle_node(head):
    '''find Middle Node of Linked List'''

    new_arr=[]
    linked_list=[head]
    while linked_list[-1].next:
        linked_list.append(linked_list[-1].next)
    mid_node=linked_list[len(linked_list) // 2]
    while mid_node:
            new_arr.append(mid_node.value)
            mid_node=mid_node.next

    new_arr_mid = new_arr[0]

    return new_arr_mid



if __name__ == "__main__":

 print ("test middle node (1,2,3,4,5)")


 linkedList1 = LinkedList()
 node1 = Node(1)
 linkedList1.append(node1)
 node2 = Node(2)
 linkedList1.append(node2)
 node3 = Node(3)
 linkedList1.append(node3)
 node4 = Node(4)
 linkedList1.append(node4)
 node5 = Node(5)
 linkedList1.append(node5)

 print (linkedList1.display())
 print (middle_node(linkedList1.head))
#     expect=3


 print ("test middle node (1,2,3,4,5,6)")

 linkedList2 = LinkedList()
 node1 = Node(1)
 linkedList2.append(node1)
 node2 = Node(2)
 linkedList2.append(node2)
 node3 = Node(3)
 linkedList2.append(node3)
 node4 = Node(4)
 linkedList2.append(node4)
 node5 = Node(5)
 linkedList2.append(node5)
 node6 = Node(6)
 linkedList2.append(node6)
 
 # expect= 4

 print (linkedList2.display())
 print (middle_node(linkedList2.head))
