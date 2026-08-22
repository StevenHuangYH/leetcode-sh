from typing import List


#sliding windows
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1 #the answer could be initialize as inf or n+1
        s = 0
        left = 0

        for right, x in enumerate(nums): #x: nums[right]
            s += x
          
            # while s - nums[left] >= target:
            #     s -= nums[left]
            #     left += 1
            # if s >= left:
            #     ans = min(ans, right- left + 1)

            while s >= target:
                ans = min(ans, right-left +1)
                s-=nums[left]
                left += 1



        return ans if ans <= n else 0