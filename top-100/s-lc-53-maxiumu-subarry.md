# LeetCode 53. Maximum Subarray (最大子数组和)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (经典动态规划 / Kadane 算法)
- **Tags:** Array, Dynamic Programming, Divide and Conquer
- **Corresponding Python File:** [`top-100/s-lc-53-maxiumu-subarry.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/top-100/s-lc-53-maxiumu-subarry.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an integer array `nums`, find the subarray with the largest sum, and return its sum.
* **[CN]** 给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

---

## 2. Code Implementation / 代码实现

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float("-inf")

        for num in nums:
            # 状态转移：若前面累加和为负数，则舍弃并从当前元素重新开始
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
            
        return max_sum
```

---

## 3. Kadane's Algorithm Intuition / 算法原理解析

1. **核心状态转移方程**：
   $$dp[i] = \max(nums[i], dp[i-1] + nums[i])$$
2. **贪心/动态规划直觉**：
   * 如果前面的子数组和 `current_sum` 变成了负数，它对后续任何元素的累加只会起到“副作用”（拖后腿）。
   * 因此，当 `current_sum + num < num`（即 `current_sum < 0`）时，我们应该直接果断舍弃前面的累加，将当前元素 `num` 作为全新子数组的起点。
3. **全局维护最大值**：
   * 每次更新 `current_sum` 后，使用 `max_sum = max(max_sum, current_sum)` 记录全局历史最高值。

---

## 4. Complexity Analysis / 复杂度分析

* **时间复杂度 (Time):** $\mathcal{O}(n)$ —— 仅需单次线性扫描。
* **空间复杂度 (Space):** $\mathcal{O}(1)$ —— 仅维护两个浮点/整型状态变量。
