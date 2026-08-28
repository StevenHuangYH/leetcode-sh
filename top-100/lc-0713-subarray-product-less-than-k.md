# LeetCode 713. Subarray Product Less Than K (乘积小于 K 的子数组)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (滑动窗口 / 连续子数组计数 / 乘积单调性 / 边界特判)
- **Tags:** Array, Sliding Window
- **Corresponding Python File:** [`top-100/lc-0713-subarray-product-less-than-k.py`](top-100/lc-0713-subarray-product-less-than-k.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an array of integers `nums` and an integer `k`, return *the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`*.
* **[CN]** 给你一个整数数组 `nums` 和一个整数 `k` ，请你返回子数组内所有元素的乘积严格小于 `k` 的连续子数组的数目。

### Constraints / 约束条件
* $1 \le \text{nums.length} \le 3 \times 10^4$
* $1 \le \text{nums}[i] \le 1000$ (所有元素均为正整数)
* $0 \le k \le 10^6$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 边界短路守卫 (k <= 1 Guard):                                             │
│    • 因为 nums[i] >= 1，任何非空连续子数组的乘积 >= 1。                      │
│    • 当 k <= 1 时，不存在严格小于 k 的乘积，必须直接返回 0。                │
│ 2. 连续子数组右端点计数公理 (Right-Endpoint Counting Invariant):            │
│    • 当窗口 nums[left...right] 满足 prod < k 时，以 right 为右端点的合法    │
│      连续子数组恰好有 (right - left + 1) 个：                               │
│      [right, right], [right-1, right], ..., [left, right]。                 │
│    • 每一轮迭代将 right - left + 1 累加进 ans，天然不重不漏！                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0713-subarray-product-less-than-k.py`](top-100/lc-0713-subarray-product-less-than-k.py) 中的实现进行逐行深入解析：

```python
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 1. 边界条件防御：当 k <= 1 时不可能有子数组乘积 < k，直接返回 0
        if k <= 1:
            return 0

        ans = 0
        prod = 1  # 记录当前窗口内所有元素的累乘积
        left = 0  # 滑动窗口左指针

        # 2. 移动右边界扩展窗口
        for right, x in enumerate(nums):
            prod *= x
            
            # 3. 核心收缩：当窗口内乘积 >= k 时，收缩左边界
            while prod >= k:
                prod /= nums[left]
                left += 1
                
            # 4. 核心计数：以 right 结尾且合法的连续子数组个数恰好为 right - left + 1
            ans += right - left + 1

        return ans
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 每个元素乘入窗口一次，除出窗口最多一次，左右指针均单调向右移动，总时间严格为 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅维护 `ans`, `prod`, `left` 局部变量，额外空间为 $\mathcal{O}(1)$。 |
