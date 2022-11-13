# Write here the code challenge solution

class Node :

    def __init__(self,value,left=None,right=None) -> None:
        self.value=value 
        self.right=right
        self.left=left

class Tree:

    def __init__(self) -> None:
        self.tree_array=[]

    def convert_to_BST(self,nums):

        '''
        function to convert sorted array to a balanced BST
        '''

        idex =len(nums)//2 # to find the middle index

        if  not nums:
            return None
        
        left= nums[:idex]
        right=nums[idex+1:]
        root=Node(nums[idex],self.convert_to_BST(left),self.convert_to_BST(right))   

        return root


 
    def output_tree(self,root):
        
        if not root:
            return ['null']               
                                  
        if root :

            if root.left:
       
                self.tree_array.append(root.left.value)
                try:
                    self.tree_array.append(root.right.value)
                except AttributeError:
                    self.tree_array.append('null')
                
            else:

                if not root.left:
                    self.tree_array.append('null')
                    
                    if not root.right:
                        self.tree_array.append('null')

            self.output_tree(root.left)  
            self.output_tree(root.right)      

        return self.tree_array 

if __name__ == '__main__':
    tree1 = Tree()
    root = tree1.convert_to_BST([1,2,3])
    actual = tree1.output_tree(root)
    print(actual)
