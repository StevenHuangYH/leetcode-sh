from typing import List
from collections import Counter

# 3471. Find the Largest Almost Missing Integer
# https://leetcode.com/problems/find-the-largest-almost-missing-integer/

# ==============================================================================
# Method 1: Fixed-Size Sliding Window (定长滑动窗口 + Set 去重 + Dict 频数统计)
# Intuitive approach using sliding window pattern
# ==============================================================================
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        window_counts = {}
        
        # Slide a fixed window of size k across nums
        for i in range(len(nums) - k + 1):
            current_window = nums[i : i + k]
            
            # Use set() so that duplicate numbers inside the SAME window are only counted once
            for num in set(current_window):
                window_counts[num] = window_counts.get(num, 0) + 1
        
        # Find the largest number that appeared in EXACTLY 1 window
        max_val = -1
        for num, count in window_counts.items():
            if count == 1:
                max_val = max(max_val, num)
                
        return max_val


# ==============================================================================
# Method 2: Mathematical Case Analysis (O(n) 最优数学分类讨论)
# ==============================================================================
class SolutionOptimal:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)
        
        # Case 1: k == 1 (Every element is its own window -> max unique element)
        if k == 1:
            unique_nums = [x for x, c in freq.items() if c == 1]
            return max(unique_nums) if unique_nums else -1
        
        # Case 2: k == n (Only 1 window containing all elements -> max element)
        if k == n:
            return max(nums)
        
        # Case 3: 1 < k < n (Only boundary elements nums[0] and nums[-1] can appear once)
        candidates = []
        if freq[nums[0]] == 1:
            candidates.append(nums[0])
        if freq[nums[-1]] == 1:
            candidates.append(nums[-1])
            
        return max(candidates) if candidates else -1