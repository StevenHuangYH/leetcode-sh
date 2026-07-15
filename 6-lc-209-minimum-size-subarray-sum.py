from typing import List

#sliding window 
#sum >= target?
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        fast = 0
        sum = 0
        min_len = float('inf')
        
        while fast < len(nums):
            sum += nums[fast]
            
            while sum >= target:
                min_len = min(min_len, fast - slow + 1)
                sum -= nums[slow]
                slow += 1
                
            fast += 1
            
        return min_len if min_len != float('inf') else 0
    
#note: 
# target has not yet met, move fast pointer to the right
# when target has met, move slow pointer to the right to find the minimum length of subarry


            