from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(node):
            if node is None:
                return 0

            left_height = get_height(node.left) # 递归计算左子树的高度
            if left_height == -1:
                return -1

            right_height = get_height(node.right) # 递归计算右子树的高度
            if right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return get_height(root) != -1
    

