from typing import List, Optional

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        m = n * 2
        ans = []
        path = [""] * m 

        def dfs(i, open_count):
            if i == m:
                ans.append("".join(path))
                return

            if open_count < n:
                path[i] = "("
                dfs(i + 1, open_count + 1)
            if i - open_count < open_count:
                path[i] = ")"
                dfs(i + 1, open_count)

        dfs(0, 0)
        return ans
