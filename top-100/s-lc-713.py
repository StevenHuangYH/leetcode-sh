from typing import List

# ==============================================================================
# 713. Subarray Product Less Than K (乘积小于 K 的子数组)
# LeetCode: https://leetcode.com/problems/subarray-product-less-than-k/
#
# Pattern: Dynamic Sliding Window (变长滑动窗口 / 双指针)
# Time Complexity: O(n) | Space Complexity: O(1)
# ==============================================================================
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Calculates the number of contiguous subarrays where the product of all 
        elements is strictly less than k.

        Why this Sliding Window design works:
        ------------------------------------
        1. Base Case `k <= 1`:
           Since nums contains strictly positive integers (nums[i] >= 1), the 
           minimum product of any non-empty subarray is 1. If k <= 1, no subarray
           product can be strictly less than k. Thus, return 0 immediately.
           This base case also guarantees k >= 2 in the loop, ensuring `left` 
           never exceeds `right + 1`.

        2. Expanding Right Boundary `prod *= x`:
           Each element x = nums[right] is multiplied into `prod` to extend 
           the candidate window nums[left..right].

        3. Shrinking Left Boundary `while prod >= k`:
           - Why `//=`? Division is the inverse of multiplication. Integer division
             `//=` avoids floating-point precision loss and exact division is 
             guaranteed since nums[left] was previously a factor of `prod`.
           - Why `while`? Adding a large element may require removing multiple 
             left elements sequentially before `prod < k` is restored.
           - Why no out-of-bounds? If nums[right] >= k, `left` advances until 
             left == right, `prod` becomes 1. Since k >= 2, `1 >= k` is False,
             terminating the while loop with left = right + 1 (contributing 0).

        4. Subarray Counting Formula `ans += right - left + 1`:
           If nums[left..right] has product < k, every contiguous sub-segment 
           ending at `right` (from nums[right] up to nums[left..right]) also has 
           product < k. The count of such subarrays ending at `right` is exactly
           `right - left + 1`.
        """
        if k <= 1:
            return 0

        ans = 0
        prod = 1
        left = 0

        for right, x in enumerate(nums):
            # 1. 扩张窗口：将新元素乘入当前窗口总乘积
            prod *= x
            
            # 2. 收缩窗口：当乘积 >= k（不合法）时，持续从左端移出元素
            #    - 使用整除 `//=` 是乘法的逆运算，避免浮点数精度误差
            #    - 使用 `while` 是因为单次移出可能不足以使乘积降至 k 以下
            while prod >= k:
                prod //= nums[left]
                left += 1
                
            # 3. 核心计数：以当前 right 为固定右端点的所有连续子数组均合法
            #    子数组数量刚好等于当前窗口的长度: right - left + 1
            ans += right - left + 1

        return ans
