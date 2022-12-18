from linked_list import LinkedList,Node

class HashTabel():
    def __init__(self,size=3):
        # in the hash table I have two properity :(size & Array(map))
       self.size = size # initial value =3 , and I can expand this length
       self.map = [None]*size # the array in hash table called map
        # self.map = [LinkedList()]*size  # to create linkedlist inside each bocket
        # self.map = [[]]*size  # to create array inside each bocket


    def custom_hash(self, key):
        # the key should bassed to hash algorithm 

        sum_of_asccii = 0  # ASCII table 
        for ch in key: # loop through the element inside the key to get sum for asccii codes # the key is srting
            asccii_of_ch = ord(ch) # ord() :pre defind method that I can use use it in order to get the ascii code ro the letter in python
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*193  #hash code # multiply with prime number
        indx = temp%self.size #compressing procces #compress the value to fit of array size by using (mod)
        return indx

        # I will use the (indx) to store the data I want 

    def set(self, key, value):
       
        hashed_key = self.custom_hash(key) # new indx & I use this index to store the (key : value)
        # if the bucket is none add directly
        # if not none -> a. add [key,value] / -> b.if have key value -> create linked list
        
        if not self.map[hashed_key]: # if the buchet is empty
            self.map[hashed_key] = [key, value]

        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key, value])
            else: # if the bucket contains one pair only # means  if I add another pair 
                chain = LinkedList() #make chaining process to create a linked list
                existing_pair = self.map[hashed_key]  # temporary variable
                new_pair = [key, value]
                self.map[hashed_key] = chain
                chain.add(existing_pair)
                chain.add(new_pair)


def First_Repeated_Word(string):
    '''
    function that will take a string as a parameter 
    and return the first repeated word in that string.
    input :string
    output :string
    '''
    sent = set()
    word = string.split()
    for s in word:
        if s in sent: 
            return s

        else: 
            sent.add(s)

    return "No Repetition"


if __name__ == '__main__':

    a = "ASAC is a department at LTUC. ASAC teaches programming in LTUC ."
    print (a)
    print ("repeated word --> ", First_Repeated_Word(a))

    print ("****************")

    b = "The soup was stirred and stirred until thickened ."
    print (b)
    print ("repeated word --> ", First_Repeated_Word(b))