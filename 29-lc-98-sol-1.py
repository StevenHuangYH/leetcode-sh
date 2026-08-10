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


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node:Optional[TreeNode], min_limit, max_limit):
            #return bool value

            if node is None:
                return True #cannot return False

            left_is_BST=dfs(node.left, min_limit, node.val)
            right_is_BST=dfs(node.right,node.val,max_limit)

            if left_is_BST and right_is_BST and min_limit < node.val< max_limit:
                return True
            return False

        return dfs(root, float("-inf"),float("inf"))

            
