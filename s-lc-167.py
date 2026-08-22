from typing import List

# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# ==============================================================================
# Method 1: Two Pointers (双指针对撞法 - 最优解 O(1) 空间)
# Time Complexity: O(n) | Space Complexity: O(1)
# ==============================================================================
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            
            if curr_sum == target:
                # 题目要求返回 1-based index (下标从 1 开始)
                return [left + 1, right + 1]
            elif curr_sum < target:
                # 当前和偏小，由于数组升序，将左指针右移以增大和
                left += 1
            else:
                # 当前和偏大，将右指针左移以减小和
                right -= 1
                
        return []


# ==============================================================================
# Method 2: Binary Search (二分查找法)
# Time Complexity: O(n log n) | Space Complexity: O(1)
# 固定第一个数 numbers[i]，在右侧区间 [i+1, n-1] 二分查找 target - numbers[i]
# ==============================================================================
class SolutionBinarySearch:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            complement = target - numbers[i]
            low, high = i + 1, n - 1
            
            while low <= high:
                mid = low + (high - low) // 2
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return []


# ==============================================================================
# Method 3: Hash Map (哈希表法 - LC 1 通解)
# Time Complexity: O(n) | Space Complexity: O(n)
# 注意：题目限制只能使用 O(1) 额外空间，因此该方法不满足进阶要求，仅作对比参考
# ==============================================================================
class SolutionHashMap:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            seen[num] = i
        return []
