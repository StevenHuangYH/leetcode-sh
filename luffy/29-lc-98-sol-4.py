#lc-98
#validate binary search tree
from typing import Optional
# Definition for a binary tree 
#A vaild BST
#the left subree of a node contains only nodes with strictly less than the node's key
#the right subtree of a node contains only nodes with keys strictly greater than the ndoe's key
#both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#center-left-right
#先判断再遍历


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        pre=float("-inf")

        def inorder(node:Optional[TreeNode])-> bool:
            if node is None:
                return True

            nonlocal pre

            left_is_BST = inorder(node.left)
            if node.val <= pre:
                return False

            right_is_BST = inorder(node.right)
            if not right_is_BST:
                return False

            return left_is_BST and right_is_BST

        return inorder(root)
    