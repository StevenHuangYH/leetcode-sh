from typing import List, Optional

MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        n = len(digits)
        if n == 0:
            return []

        ans = []
        path=[""]*n

        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return

            for char in MAPPING[int(digits[i])]:
                path[i] = char
                dfs(i+1)

        dfs(0)
        return ans

# for x in "abc":
#   for y in "def";
# 构造长度为2的字符串 
# 可以写一个二重循环
# 但是如果要构造长度为3，4
# 甚至长度是不确定的要怎么写呢

# 而只是单纯的循环嵌套
# 表达能力是有限的

# 原问题：构造长度为n的字符串
# 枚举一个字母
# 子问题：构造长度为n-1的字符串

# 子问题和原问题是相似的，这种从原问题到子问题的过程适合用递归去解决
# 回溯有一个增量构造答案的过程，这个过程通常使用递归来实现

# 用一个 path 数组记录路径上的字母
# 回溯三问
# 1： 当前操作？枚举path[i]要填入的字母
# 2： 子问题？构造字符串 >= i 的部分
# 3： 下一个子问题？ 构造字符串 >= i+1 的部分
#　dfs(i) -> dfs(i + 1)