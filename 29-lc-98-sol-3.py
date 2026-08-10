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
        def dfs(node: Optional[TreeNode],low_limit:float, high_limit:float) -> bool:
            if not node:
                return True

            #Pruning (剪枝)
            if node.val <=low_limit or node.val >= high_limit:
                return False

            #judge in advance
            left_is_BST=dfs(node.left,low_limit,node.val)
            if not left_is_BST:
                return False
            right_is_BST=dfs(node.right, node.val, high_limit)
            if not right_is_BST:
                return False

            return True

        return dfs(root,float('-inf'), float('inf'))

            
            