# Container with Most water.

# use two pointer method

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1

        result = 0

        while left < right:
            area = (right-left) * min(height[left], height[right])
            result =  max(result, area)

            if height[left]<height[right]:
                left += 1
            else:
                right -= 1

        return result

# time complexity: O(n)
# space complexity: O(1) 
# each time you move a pointer costs O(1)







