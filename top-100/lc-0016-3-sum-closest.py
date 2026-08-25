from typing import List

# 方案 1: 标准对撞双指针 (Standard Two Pointers)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == target:
                    return target
                
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum


# 方案 2: 极致双向剪枝优化 (Extreme 2-Way Pruning - O(1) Min/Max Bound Checking)
class SolutionOptimized:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            
            # 剪枝 1: 当前 i 对应的最小三数之和
            min_s = x + nums[i + 1] + nums[i + 2]
            if min_s > target:
                if min_s - target < abs(closest_sum - target):
                    closest_sum = min_s
                break  # min_s 已大于 target，后续更大的 i 只会更远，直接终止整个循环
            
            # 剪枝 2: 当前 i 对应的最大三数之和
            max_s = x + nums[-2] + nums[-1]
            if max_s < target:
                if target - max_s < abs(closest_sum - target):
                    closest_sum = max_s
                continue  # max_s 已小于 target，当前 i 的其他组合只会更小，直接跳到下一个 i
            
            left = i + 1
            right = n - 1
            while left < right:
                total = x + nums[left] + nums[right]
                
                if total == target:
                    return target
                
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum