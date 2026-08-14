#lc-78
#subsets


from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[] 

        def dfs(i):
            if i>=len(nums):
                result.append(path.copy())
                return
            #pick
            path.append(nums[i])
            dfs(i+1)

            #backtrack
            path.pop()

            #not pick
            dfs(i+1)


        dfs(0)
        return result

        
