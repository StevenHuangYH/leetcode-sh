from typing import List

# 713. Subarray Product Less Than K (乘积小于 K 的子数组)
# https://leetcode.com/problems/subarray-product-less-than-k/

# ==============================================================================
# Method: Sliding Window (滑动窗口 / 双指针)
# Time Complexity: O(n) | Space Complexity: O(1)
# ==============================================================================
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 边界条件：因为 nums[i] >= 1，所以子数组乘积至少为 1。
        # 当 k <= 1 时，不存在严格小于 k 的乘积，直接返回 0。
        if k <= 1:
            return 0

        ans = 0
        prod = 1
        left = 0

        for right, x in enumerate(nums):
            prod *= x
            
            # 当窗口内乘积 >= k 时，收缩左边界
            while prod >= k:
                prod //= nums[left]
                left += 1
                
            # 核心计数：以 right 结尾且合法的连续子数组个数恰好为 right - left + 1
            ans += right - left + 1

        return ans
