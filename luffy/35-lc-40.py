#lc-40
#combination sum 2
from typing import List


#Deduplication

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]

        candidates.sort() #sorting first


        def dfs(starting_index, cur_sum):
            if cur_sum == target:
                result.append(path.copy())   
                return


            for i in range(starting_index, len(candidates)):
                #pruning here:
                if cur_sum+candidates[i]>target:
                    break


                #deduplication 去重
                if i > starting_index and candidates[i]==candidates[i-1]:
                    continue

                #track back here
                path.append(candidates[i])

                #since every number could only used once so i+1
                dfs(i+1,cur_sum+candidates[i]) 
                path.pop()


        dfs(0,0)
        return result












