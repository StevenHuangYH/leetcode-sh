#lc-46

#permutation

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]

        
        def backtrack():
            if len(path)==len(nums):
                result.append(path.copy())
                return



            for i in range(len(nums)):
                if nums[i] in path:
                    continue


                path.append(nums[i])

                backtrack()
                path.pop()


        backtrack()
        return result
    


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]

        used = [False] * len(nums) #hashtable




        def backtrack():
            if len(path)==len(nums):
                result.append(path.copy())
                return



            for i in range(len(nums)):
                if used[i]:
                    continue


                path.append(nums[i])
                used[i]=True
                backtrack()
                path.pop()
                used[i]=False#reset as False  归位


        backtrack()
        return result
    
    






        