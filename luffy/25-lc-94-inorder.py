#inordertraversal
#lc-94

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def f(node: Optional[TreeNode]): #pre-order traversal

           #base case
            if node is None:
                return


            f(node.left)


            
            res.append(node.val)


            
            f(node.right)
            return
        
        f(root)
        return res