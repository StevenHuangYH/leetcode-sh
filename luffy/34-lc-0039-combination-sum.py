#lc39

#combination Sum
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]

        def backtrack(cur_sum, starting_index):
            if cur_sum == target:
                result.append(path.copy())
                return


            if cur_sum>target:
                return


            for i in range(starting_index, len(candidates)):
                path.append(candidates[i])
                backtrack(cur_sum+candidates[i], i) 
                #cur_sum + candidates[i]: add the current candidate to cur_sum for updating the current sum
                #i: pass i as the starting index 
                #this is becuase problem allows us to reuse the same number an unlimited number of times


                path.pop()

        backtrack(0,0)
        return result            


#pruning after sorting
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        candidates.sort()

        def backtrack(cur_sum, starting_index):
            if cur_sum == target:
                result.append(path.copy())
                return


            if cur_sum>target:
                return


            for i in range(starting_index, len(candidates)):


                #pruning
                if cur_sum + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(cur_sum+candidates[i], i) 
                #cur_sum + candidates[i]: add the current candidate to cur_sum for updating the current sum
                #i: pass i as the starting index 
                #this is becuase problem allows us to reuse the same number an unlimited number of times


                path.pop()

        backtrack(0,0)
        return result      



#pick or not pick
class Solution3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]

        def dfs(i, cur_sum):
            if cur_sum == target:
                result.append(path.copy())
                return

            if  i >= len(candidates):
                return

            if cur_sum >=target:
                return

            path.append(candidates[i])
            dfs(i, cur_sum+candidates[i])
            path.pop()

            dfs(i+1, cur_sum)

        dfs(0,0)
        return result      