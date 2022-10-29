# Write here the code challenge solution

# Implement the MyQueue class: /done

# push(int x) Pushes element x to the back of the queue. /done
# pop() Removes the element from the front of the queue and returns it.
# peek() Returns the element at the front of the queue.
# empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

# Example 1:

# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

class MyQueue:
    def __init__(self) -> None:
       self.queue = []

    
    def push(self,element):
        '''
        Pushes element x to the back of the queue.
        '''

        self.queue.append(element)


    def pop(self):

        '''
        Removes the element from the front of the queue and returns it.
        '''

        stack_1=self.queue
        stack_2=[]
        for i in range(len(stack_1)):
            
            stack_2.append(stack_1.pop())
        removed_item=stack_2.pop()
        self.queue=[]

        for i in range(len(stack_2)-1,-1,-1):
            self.queue.append(stack_2[i])
        return removed_item


    def peek(self):
        '''
        Returns the element at the front of the queue. 
        '''

        if self.top:
            return self.queue[0]
        else:
            return("This stack is empty")

    def empty(self):

        '''
        Returns true if the queue is empty, false otherwise.
        '''

        if len(self.queue)>0:
            return False
        else:
            return True
