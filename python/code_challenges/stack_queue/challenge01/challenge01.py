# Write here the code challenge solution

# Implement the MyQueue class: /done

# push(int x) Pushes element x to the back of the queue. /done
# pop() Removes the element from the front of the queue and returns it.
# peek() Returns the element at the front of the queue.
# empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

class MyQueue:
    
  
    def __init__(self) -> None:
       self.queue = []
       self.size=0

    
    def push(self,element):
        '''
        Pushes element x to the back of the queue.
        '''

        self.queue.append(element)
        self.size +=1
        return self.queue



    def pop(self):

        '''
        Removes the element from the front of the queue and returns it.
        '''

        stack_1=self.queue
        stack_2=[]

        for i in range(len(stack_1)):
            
            stack_2.append(stack_1.pop())
        remove_member=stack_2.pop()

        for i in range(len(stack_2)-1,-1,-1):
            self.queue.append(stack_2[i])

        return remove_member, self.queue


    def peek(self):
        '''
        Returns the element at the front of the queue. 
        '''

        
        return self.queue[0]
        

    def empty(self):

        '''
        Returns true if the queue is empty, false otherwise.
        '''

        if len(self.queue)>0:
            return False
        else:
            return True

# to check
if __name__ =="__main__":
 
    queue1=MyQueue()

    # add element [1,2]
    print("queue1.push('A'), queue = ", queue1.push("A"))
    print("queue1.push('B'), queue = ",queue1.push("B"))

    print("queue1.peek() -> ",queue1.peek())

    print("queue1.pop() -> ",queue1.pop())
    print("queue1.empty() -> ",queue1.empty())
