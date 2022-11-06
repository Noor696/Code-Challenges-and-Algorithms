# Write here the code challenge solution
class Node:
    '''
    take a value and return a node value,with left and right values.
    
    '''
    def __init__(self,value) -> None:
        self.value=value
        self.right=None
        self.left=None

class Tree:

    def binaryTree(self, preorder, inorder):
        '''
        preorder: List[int]
        inorder: List[int]
        return: TreeNode'''

        if inorder:

            INDEX_root = inorder.index(preorder.pop(0))
            root = Node(inorder[INDEX_root])
            root.left = self.buildTree(preorder, inorder[:INDEX_root])
            root.right = self.buildTree(preorder, inorder[INDEX_root+1:])
			
            return root

tree1 = Tree()
tree1.binaryTree([3,9,20,15,7],[9,3,15,20,7]).value
# print (tree1)

def buildTree(root):
    final_tree=[]
    root_right=root
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


    print(final_tree)



buildTree(tree1.binaryTree([3,9,20,15,7],[9,3,15,20,7]))


    


    

    





# def pre_order(root):
#     if root is not None:
#         print(root.value)
#     if root.left is not None:
#         pre_order(root.left)
#     if root.right is not None:
#         pre_order(root.right)

# def in_order(root):
#     if root.left is not None:
#         in_order(root.left)
#     if root is not None:
#         print(root.value)
#     if root.right is not None:
#         in_order(root.right)

