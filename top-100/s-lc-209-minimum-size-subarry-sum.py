from typing import List

# 209. Minimum Size Subarray Sum (长度最小的子数组)
# https://leetcode.com/problems/minimum-size-subarray-sum/

# ==============================================================================
# Method: Dynamic Sliding Window (变长滑动窗口 / 双指针)
# Time Complexity: O(n) | Space Complexity: O(1)
# ==============================================================================
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        fast = 0
        current_sum = 0
        min_len = float('inf')
        
        while fast < len(nums):
            current_sum += nums[fast]
            
            # 当窗口和满足条件时，尝试收缩左边界以寻找更短的子数组
            while current_sum >= target:
                min_len = min(min_len, fast - slow + 1)
                current_sum -= nums[slow]
                slow += 1
                
            fast += 1
            
        return min_len if min_len != float('inf') else 0
