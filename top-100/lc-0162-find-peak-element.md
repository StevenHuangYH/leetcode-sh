# LeetCode 162. Find Peak Element (寻找峰值)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (二分查找 / 导数与单调性斜率 / 红蓝二分法 / 局部极值定理)
- **Tags:** Array, Binary Search
- **Corresponding Python File:** [`top-100/lc-0162-find-peak-element.py`](top-100/lc-0162-find-peak-element.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**. You must write an algorithm that runs in $O(\log n)$ time.
* **[CN]** 峰值元素是指其值严格大于左右相邻值的元素。给你一个整数数组 `nums`，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 **任何一个峰值** 所在位置即可。你必须实现时间复杂度为 $O(\log n)$ 的算法来解决此问题。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 爬坡上山不变量 (Slope Monotonicity Invariant):                            │
│    • 比较 nums[mid] 与 nums[mid + 1] 的斜率：                                │
│      - 若 nums[mid] > nums[mid + 1]: 处于【下坡段】(蓝色)，峰值必定在 mid 或  │
│        mid 的左侧，收缩右边界 right = mid。                                  │
│      - 若 nums[mid] < nums[mid + 1]: 处于【上坡段】(红色)，峰值必定在 mid+1  │
│        或其右侧，收缩左边界 left = mid。                                     │
│ 2. 开区间二分 (-1, n - 1): 终止时 right 即为峰值下标。                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0162-find-peak-element.py`](top-100/lc-0162-find-peak-element.py) 中的多方案实现进行逐行深入解析：

```python
from typing import List

# 方案 1: 开区间模版 (-1, n - 1) —— 红蓝二分法
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            # 若处于下坡段，峰值在左半区（含 mid）
            if nums[mid] > nums[mid + 1]:
                right = mid
            # 若处于上坡段，峰值在右半区
            else:
                left = mid

        return right
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(\log n)$ | 每次二分判定均将搜索区间减半，总迭代次数为 $\lceil \log_2 n \rceil$，严格满足 $\mathcal{O}(\log n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用 `left`, `right`, `mid` 常数级指针变量。 |
