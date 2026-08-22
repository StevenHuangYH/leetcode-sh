from typing import List

class Solution3: #even better hash table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        for i,item in enumerate(nums):
            other = target - item
            if other in cache:
                return [i, cache[other]]
            cache[item] = i
        return []


#when you need to find two numbers in a list that add up to a specific target, 
# you can use a hash table (dictionary) to store the numbers you've seen so far and their indices. This allows you to check in constant time if the complement (the number needed to reach the target) exists in the hash table. The provided code implements this approach efficiently.