from typing import List
# 要求nums是非递减的，即nums[i] <= nums[i+1]
# 返回最小的满足 nums[i] >= target的i
# 如果不存在，则return len(nums)
def lower_bound (nums: List[int], target: int) -> int:
    left = 0
    n=len(nums)
    right = n - 1 #闭区间：[left , right]
    while left <= right: #range is not empty
        #left + (right - left) // 2
        mid = (left+right) // 2
        if nums[mid] < target:
            left = mid + 1 # [mid+1, right]
        else:
            right = mid - 1 # [left, mid - 1]
    return left

def lower_bound2 ( nums: List[int], target: int) -> int:
    left = 0
    n=len(nums) 
    right = n - 1 #左闭右开区间 [left, right)
    while left < right: #range is not empty
        mid = (left+right)//2 
        if nums[mid] < target:
            left = mid + 1 # [left , right)
        else:
            right = mid # [left ,mid)
    return left #right

def lower_bound3 (nums: List[int], target: int) -> int:
    left = 0
    n=len(nums) 
    right = n - 1 #开区间 (left, right)
    while left < right: #range is not empty
        mid = (left+right)//2 
        if nums[mid] < target:
            left = mid  # (mid , right)
        else:
            right = mid # (left ,mid)
    return left #right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]

        end = lower_bound(nums, target + 1)-1
        return [start, end]

        
