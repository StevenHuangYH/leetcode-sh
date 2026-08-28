from typing import List, Optional

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return 


            dfs(i+1)

            path.append(nums[i])
            dfs(i+1)
            path.pop()

        dfs(0)
        return ans


# 站在答案的角度思考
# 枚举第一个数选谁
# 枚举第二个数选谁
# 每个节点都是答案

# 注意[1,2] 和 [2,1]是重复的子集
# 为了避免重复
# 下一个数应大于当前选择的数

# 回溯三问
# 当前操作？枚举一个下标　J >= i 的数字、加入path
# 子问题？从下标 >= i 的数字中构造子集
# 下一个子问题？ 从下标 >= j + 1的数字中构造子集

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return 


            for j in range(i,n):
                path.append(nums[j])
                dfs(i+1)
                path.pop()

        dfs(0)
        return ans
