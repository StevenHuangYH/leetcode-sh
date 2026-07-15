from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache={}
        for i,item in enumerate(numbers):
            other = target - item
            if other in cache:
                return(cache[other]+1,i+1)
            cache[item] = i


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer approach
        left = 0
        right = len(numbers) - 1
        while left != right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return[left+1, right+1]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1


#two pointer approach is more efficient than hash table approach in this case 
# because the input list is sorted. The two pointer approach has a time complexity of O(n) 
# and a space complexity of O(1), while the hash table approach has a time complexity of O(n) 
# but a space complexity of O(n) due to the additional storage used for the hash table.
            
            
#note:
#if the list is already sorteed
#two pointer approach is the general methond



                
        