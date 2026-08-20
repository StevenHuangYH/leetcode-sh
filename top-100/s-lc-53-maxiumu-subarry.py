#maximum subarry

#kadene
#current_max=max(today, current_sum + today)
#max_sum = max(max_sum. current_sum)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        max_sum = float("-inf")

        
        for num in nums:
            current_sum=max(num, current_sum + num)
            max_sum=max(max_sum, current_sum)
        return max_sum

    

        