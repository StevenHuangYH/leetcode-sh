from typing import List

# 方案 1: 开区间模版 (-1, n - 1) —— 推荐 (红蓝二分法)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        开区间 (-1, len(nums) - 1)
        红蓝染色法：
        - 蓝色 (Blue): nums[mid] > nums[mid + 1] (处于下坡段，峰值在 mid 或 mid 左侧)
        - 红色 (Red):  nums[mid] < nums[mid + 1] (处于上坡段，峰值在 mid 严格右侧)
        """
        left = -1
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:  # colored as blue
                right = mid
            else:                          # colored as red
                left = mid

        return right


# 方案 2: 闭区间模版 [0, n - 2]
class SolutionClosed:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 2

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1

        return left


# 方案 3: 左闭右开区间模版 [0, n - 1)
class SolutionHalfOpen:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left