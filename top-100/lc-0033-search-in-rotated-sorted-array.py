from typing import List, Optional




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue (i: int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return target > end and nums[i] >= target
            else:
                return target > end or nums[i] >= target


        left = -1
        right = len(nums)-1
        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid

        if right == len(nums) or nums[right] != target:
            return -1

        return right


        