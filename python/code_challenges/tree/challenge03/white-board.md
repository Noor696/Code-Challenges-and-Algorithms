## Convert Sorted Array to BST:

### Problem Domain:

Given an integer array nums, convert it to a height-balanced binary search tree.
**A height-balanced binary** tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


Input : array_nums = [0,-3,-10,5,9]
Output : [0,-3,9,-10,null,5]

create a method which accepts a list.
the method put The middle element of the array as root.
Get the middle of the left sub tree and make it the left root .
Get the middle of the right sub tree and make it the right root.
Recursively do the same for the left sub and right sub.
Print the output of the tree.