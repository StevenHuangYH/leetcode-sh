#lc 145 
#binary tree postorder traversal

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def f(node:Optional[TreeNode]):
            if node is None:
                return

            f(node.left)

            f(node.right)

            res.append(node.val)


            return

        f(root)
        return res