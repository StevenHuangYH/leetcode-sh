from typing import List
# 假设path 长为m
# 那么还需要选 d = k = m
# 设当前需要从[1, i] 这i个数中选数
# 如果 i < d
# 最后必然无法选出k个数
# 不需要继续递归
# 这是一种剪枝

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):

            d = k - len(path)
            
            if len(path) == k:
                ans.append(path.copy())
                return
            
            
            for j in range(i, d-1, -1):
                path.append(j)
                dfs(j-1)
                path.pop()

        dfs(n)
        return ans
