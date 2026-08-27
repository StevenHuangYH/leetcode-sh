from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        判断两棵二叉树是否在结构与节点值上完全相同 (Same Tree)。
        
        核心思维模型 (Recursive Mental Model):
        1. 递归基 (Base Case):
           - 若 p 与 q 至少有一个为空: 仅当两者同为 None (p is q) 时结构相同，返回 True；否则一空一非空，返回 False。
        2. 原问题与子问题归并 (Divide & Conquer):
           - 当前节点值必须相等: p.val == q.val
           - 左子树必须完全相同: isSameTree(p.left, q.left)
           - 右子树必须完全相同: isSameTree(p.right, q.right)
           三者必须同时满足 (and)。
        """
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
