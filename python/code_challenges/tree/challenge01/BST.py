# class TreeNode():
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Tree:
#     def isValidBST(self, root) -> bool:
        
#         def dBST(node, lower, upper):
#             if not node:  # nothing here
#                 return True
#             elif (lower >= node.val > upper):
#                 return False
#             else:
#                 return dBST(node.left, lower, node.val) and dBST(node.right, node.val, upper)
        
#         return dBST(root, float('-inf'), float('inf'))


# Algorithm
#  set a range (at first we set it to (-infinity, infinity)
# - see if every node is in their own range

# define curent node lower bound as lower and upper bount as upper.

# At each call check below statements
# a. If current node is null then return true.
# b. If current node value is out of lower or upper bound then return false
# a. Call recursively for the left node, set upper bound as current node value and lower bound as it is ( set as left ).
# b. Call recursively for the right node, set lower bound as current node value and upper bound as it is ( set as right ).
# return left && right.


# def isValidBST(root) -> bool:
#     if not root:
#         return True

#     current = root
#     def valid(current):
#         if current.left and current.left.value < current.value:
#             current=current.left
#             valid(current)
#             return True
#         if current.right and current.right.value > current.value:
#             current= current.right
#             valid(current)
#             return True
#         else: 
#             return False

#     return valid(current)


class Node:
    def init(self,value):
        self.value = value
        self.left = None
        self.right = None
class Tree:
    def init(self):
        self.root = None



def valid(current):
    if current.left and current.left.value < current.value:
        valid(current.left)
        return True
    if current.right and current.right.value > current.value:
        valid(current.right)
        return True
    else: 
        return False





tree1 = Tree()

def pre_order(root):
    if root is not None:
        print(root.value)
    if root.left is not None:
        pre_order(root.left)
    if root.right is not None:
        pre_order(root.right)

def in_order(root):
    if root.left is not None:
        in_order(root.left)
    if root is not None:
        print(root.value)
    if root.right is not None:
        in_order(root.right)




node1 = Node(4)
tree1.root = node1

node2 = Node(5)
tree1.root.left = node2

node3 = Node(3)
tree1.root.right = node3

node4 = Node(1)
tree1.root.left.left = node4

node5 = Node(2)
tree1.root.left.right = node5



pre_order(tree1.root)
print(   )
in_order(tree1.root)
print(       )
print(valid(tree1.root))

