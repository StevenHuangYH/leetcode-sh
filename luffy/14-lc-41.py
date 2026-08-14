#lc-41-missing-postive

from typing import List
#make array as your hash table

#auxiliary space required
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         i=1
#         while True:
#             if i in nums:
#                 i=i+1
#             else:
#                 return i
#         #o(n)
            


# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         num_sets = set(nums) #O(n) space-> wrong
#         i=1
#         while True:
#             if i in num_sets:
#                 i=i+1
#             else:
#                 return i



class Solution: #partition 归位
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            num=nums[i]
            if i==num-1: #partition
                i=i+1
            else: # not on the right postiton
                if 1<=num<=len(nums) and nums[nums[i]-1] !=nums[i]: # 1 to n, should be in num-1
                    # target=nums[num-1]
                    # nums[num-1]=num
                    # nums[i]=target
                    nums[i], nums[num-1]=nums[num-1], nums[i] #交换写法
                    #right side becomes a tuple
                else: #number that is not qualify for partition
                    i=i+1

        #traversal for the num again
        for i in range(len(nums)):
            if i ==nums[i]-1:
                pass
            else:
                return i+1
        
        return len(nums)+1
    
    
    

                










        
        