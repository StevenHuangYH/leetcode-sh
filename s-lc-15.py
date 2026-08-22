from typing import List

# 15. 3Sum (三数之和)
# https://leetcode.com/problems/3sum/

# ==============================================================================
# Method 1: Sort + Two Pointers with 2-Way Extreme Pruning (双指针 + 极致双向剪枝)
# Time Complexity: O(n^2) | Space Complexity: O(1) 或 O(log n)
# ==============================================================================
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # The order of triplet does not matter
        # Indices: i < j < k
        # The result cannot include repeated triplets

        result = []
        n = len(nums)

        for i in range(0, n - 2):
            x = nums[i]
            
            # 基准数去重: 跳过与前一个重复的数
            if i > 0 and x == nums[i - 1]:
                continue

            # Optimization 1 (最小和剪枝):
            # 若 x 与其后最小的两个数相加都 > 0，则后续任意组合必 > 0，直接 break
            if x + nums[i + 1] + nums[i + 2] > 0:
                break

            # Optimization 2 (最大和剪枝):
            # 若 x 与全数组最大的两个数相加仍然 < 0，则当前 x 无法与任何后序数配对为 0，跳过本次循环
            if x + nums[-2] + nums[-1] < 0:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    result.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                        
        return result
