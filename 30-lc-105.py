#lc-105

#construct binary tree from preorder and inorder traversal
from typing import List,Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



#pre-order root-left-righ
#inorder: left-root-right

#posterorder: left-right-root


#divide and conquer
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
