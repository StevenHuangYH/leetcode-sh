from typing import List, Optional

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

        ans = []
        cur = [root]
        while cur:
            nxt = []
            vals = []
            for node in cur:
                vals.append(node.val)

                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)

            cur = nxt
            ans.append(vals)

        return ans

# 初始数组 cur 只有 root
# 遍历 cur，把 left and right children 记录到下一层节点数组nxt中
# 遍历 cur 的同时，把节点值记录到数组vals中
# 遍历结束后，把vals加入答案中
# 遍历结束后，把cur替换为nxt
# 开启下一次循环

# cur 为空，意味着所有节点遍历完毕，
# 即，退出循环

from collections import deque

#use queue
class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        q = deque([root])

        while q:
            vals = []

            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)

            ans.append(vals)
        return ans

        
