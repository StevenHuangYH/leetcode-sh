from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: #if root is None
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


#二叉树与递归
#如何思考二叉树相关问题
#为什么需要使用递归
#为什么这样写就一定能正确
#计算机是如何执行递归的
#另一种递归思路

# 思考整棵树与其左右子树的关系
# 整棵树的最大深度为 = max(左子树的最大深度，右子树的最大深度) + 1


# 原问题：计算出整棵树的最大深度
# 子问题：计算出 左/右子树的最大深度
# 因此 子问题与原问题是相似的

# 类比循环，执行的代码也应该是相同的，
# 但是，子问题需要把计算结果返给上一级的问题
# 这更适合使用递归实现。

# 但由于子问题的规模比原问题小
# 不断递下去，始终会有尽头
# 这就是递归的 边界条件（base case）
# 直接返回它的答案 （归）

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        ans = 0
        def f(node, cnt):
            if root is None:
                return 0
            cnt += 1
            nonlocal ans
            ans = max(ans,cnt)
            f(node.left, cnt)
            f(node.right, cnt)
        f(root, 0)
        return ans

