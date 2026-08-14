#lc-144
#binary tree preorder traversal

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# pre-order: root-left-right
#in-order: left-root-right
#posterorder: left-right-root
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def f(node: Optional[TreeNode]): #pre-order traversal

           #base case
            if node is None:
                return

            #center:
            res.append(node.val)

            #left
            f(node.left)

            #right
            f(node.right)
            return
        
        f(root)
        return res


        

        