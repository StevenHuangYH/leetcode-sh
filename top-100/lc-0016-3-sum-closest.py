from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closetSum = float("inf")
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == target:
                    return total
                
                if abs(total - target) < abs(closetSum - target):
                    closetSum = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1
                    
        return closetSum