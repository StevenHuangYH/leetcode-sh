from typing import List
# two pointer 
class Solution:
    def trap(self, height: List[int]) -> int:
        n =  len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]

        for i in range(1,n):
            pre_max[i] = max(pre_max[i-1], height[i])

        suf_max = [0] * n
        suf_max[-1] =  height[-1]

        for i in range(n-2, -1 ,-1):
            suf_max[i] =  max(suf_max[i+1], height[i])

        result = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            result += min(pre, suf) - h


        return result

    #time complexity: O(n)
    #space complexity: O(n)

# better two pointer
class Solution2:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        left = 0
        right = n-1
        pre_max = 0
        suf_max = 0
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max= max(suf_max, height[right])
            if pre_max < suf_max:
                result += pre_max - height[left]
                left += 1
            else:
                result += suf_max - height[right]
                right -= 1
                
        return result
            





    




        