# LeetCode 53. Maximum Subarray (最大子数组和)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (动态规划 / Kadane 算法 / 前缀和极值 / 状态压缩)
- **Tags:** Array, Divide and Conquer, Dynamic Programming
- **Corresponding Python File:** [`top-100/lc-0053-maximum-subarray.py`](top-100/lc-0053-maximum-subarray.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an integer array `nums`, find the subarray with the largest sum, and return *its sum*.
* **[CN]** 给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

### Constraints / 约束条件
* $1 \le \text{nums.length} \le 10^5$
* $-10^4 \le \text{nums}[i] \le 10^4$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 状态转移不变量 (Kadane's Recurrence Relation):                           │
│    • dp[i] 表示以 nums[i] 结尾的最大连续子数组和。                           │
│    • dp[i] = max(nums[i], dp[i-1] + nums[i])                                │
│    • 若前面的累加和 dp[i-1] < 0，则拖累当前元素，不如从 nums[i] 重新开始。    │
│ 2. 空间压缩: current_sum = max(num, current_sum + num)，max_sum 维护最大值。 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0053-maximum-subarray.py`](top-100/lc-0053-maximum-subarray.py) 中的实现进行逐行深入解析：

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int], target: int = 0) -> int:
        current_sum = 0
        max_sum = float("-inf") # 初始化为负无穷，保证全负数数组正确返回最大负数

        for num in nums:
            # 状态转移：若当前累加和为负，则舍弃并从当前 num 重新开始累加
            current_sum = max(num, current_sum + num)
            # 维护全局最大子数组和
            max_sum = max(max_sum, current_sum)

        return max_sum
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 单次线性遍历数组中的每个元素，每次状态更新耗时 $\mathcal{O}(1)$，总时间严格为 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 空间状态压缩后仅使用 `current_sum` 和 `max_sum` 两个变量，额外空间为 $\mathcal{O}(1)$。 |
