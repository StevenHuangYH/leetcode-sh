
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        n=len(numbers)
        right = n-1

        while left < right:
            result = numbers[left]+numbers[right]

            if result == target:
                break
            if result > target:
                right -= 1
            else:
                left+=1
            

        return [left+1,right+1]
            
        
    

        