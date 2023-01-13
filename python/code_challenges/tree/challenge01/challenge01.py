# Write here the code challenge solution
class Node:
    '''
    take a value and return a node value,with left and right values.
    
    '''
    def __init__(self,value=None):
        self.value=value
        self.right=None
        self.left=None



class Tree:

    def binaryTree(self, preorder, inorder):
        '''
        preorder: List[int]
        inorder: List[int]
        return: TreeNode'''

        if not preorder or not inorder:
            return None

        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.binaryTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.binaryTree(preorder[mid+1:], inorder[mid+1:])

        return root

 

tree1 = Tree()
tree1.binaryTree([3,9,20,15,7],[9,3,15,20,7])
# tree1.binaryTree([3,9,20,15,7],[9,3,15,20,7]).value



def buildTree(root):
    final_tree=[]
    root_right=root.right
    final_tree.append(root.value)

    while root.left and root.right:
        if root.left.value:
            final_tree.append(root.left.value)
        if root.right.value:
            final_tree.append(root.right.value)
        root=root.left

    if root is None:
        final_tree.append('null')

    if root.left is None:
        final_tree.append('null')

    if root.right is None:
        final_tree.append('null')

    while root_right.right:
        if root_right.left.value:
            final_tree.append(root_right.left.value)

        if root_right.right.value:
            final_tree.append(root_right.right.value)
        
        root_right=root_right.right


    return (final_tree)


print(buildTree(tree1.binaryTree([3,9,20,15,7],[9,3,15,20,7])))

print(buildTree(tree1.binaryTree([4,3,6],[3,4,6])))



    


    

    
