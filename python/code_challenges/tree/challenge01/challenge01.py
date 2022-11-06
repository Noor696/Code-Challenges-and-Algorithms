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

    def buildTree(self, preorder, inorder):
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