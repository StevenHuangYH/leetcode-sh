#lc-102

#Binary Tree level order traversal

from collections import deque #底层是double linked list
from typing import Optional, List

#bfs
#breadth-first search bfs

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=deque()
        queue.append(root)
        res=[]

        while queue:
            n=len(queue)
            cur_level=[]
            for i in range(n):
                node=queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(cur_level)

        return res


            




