# LeetCode 34. Find First and Last Position of Element in Sorted Array (在排序数组中查找元素的第一个和最后一个位置)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (二分查找 / lower_bound 万能模版 / 区间范围映射)
- **Tags:** Array, Binary Search
- **Corresponding Python File:** [`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value. If `target` is not found in the array, return `[-1, -1]`. You must write an algorithm with $O(\log n)$ runtime complexity.
* **[CN]** 给你一个按照非递减顺序排列的整数数组 `nums`，和一个目标值 `target`。请你找出给定目标值在数组中的开始位置和结束位置。如果数组中不存在目标值 `target`，返回 `[-1, -1]`。你必须设计并实现时间复杂度为 $O(\log n)$ 的算法解决此问题。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 万能 lower_bound 核心原语:                                               │
│    • lower_bound(target) 寻找第一个满足 nums[i] >= target 的下标。            │
│ 2. 4 种二分边界关系的等价映射 (The 4-Way Equivalence Map):                  │
│    • ① >= target : lower_bound(target)                                      │
│    • ② > target  : lower_bound(target + 1)                                  │
│    • ③ < target  : lower_bound(target) - 1                                  │
│    • ④ <= target : lower_bound(target + 1) - 1                              │
│ 3. 起始与结束位置求解:                                                       │
│    • start = lower_bound(target)                                            │
│    • end   = lower_bound(target + 1) - 1                                    │
│    • 合法性检验: start == len(nums) or nums[start] != target 判定无解返回 [-1,-1]│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py) 中的实现进行逐行深入解析：

```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # 万能 lower_bound: 返回首个 >= target 的元素下标
        def lower_bound(target: int) -> int:
            left = -1
            right = len(nums) # 开区间 (-1, n)
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid # 蓝色 (>= target)
                else:
                    left = mid  # 红色 (< target)
            return right

        # 1. 查找第一个 >= target 的位置
        start = lower_bound(target)

        # 2. 越界或不存在 target 的防护
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        # 3. 查找最后一个 <= target 的位置等价于 (第一个 >= target + 1) - 1
        end = lower_bound(target + 1) - 1

        return [start, end]
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(\log n)$ | 调用了 2 次 `lower_bound`，每次耗时 $\mathcal{O}(\log n)$，总耗时严格为 $\mathcal{O}(\log n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用了指针变量，额外空间为 $\mathcal{O}(1)$。 |
