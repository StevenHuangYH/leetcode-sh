# LeetCode 153. Find Minimum in Rotated Sorted Array (寻找旋转排序数组中的最小值)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (二分查找 / 红蓝开区间二分 / 旋转数组阶梯断点判定)
- **Tags:** Array, Binary Search
- **Corresponding Python File:** [`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the sorted rotated array `nums` of unique elements, return *the minimum element of this array*. You must write an algorithm that runs in $O(\log n)$ time.
* **[CN]** 给你一个元素值 **互不相同** 的数组 `nums` ，它原来是一个升序排列的数组，并进行了旋转。请你找出并返回数组中的 **最小元素** 。你必须设计一个时间复杂度为 $O(\log n)$ 的算法解决此问题。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 数组分段参考锚点 (Pivot Invariant with nums[-1]):                        │
│    • 以末尾元素 x = nums[-1] 为划分标准：                                    │
│      - 蓝色 (Blue): nums[mid] < x -> mid 必定位于右半段（含最小值及右侧），  │
│        收缩右边界 right = mid。                                              │
│      - 红色 (Red): nums[mid] >= x -> mid 必定位于左半段（严格在最小值左侧），│
│        收缩左边界 left = mid。                                               │
│ 2. 开区间收敛: left = -1, right = n - 1，终止时 right 严格指向最小值下标。   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py) 中的实现进行逐行深入解析：

```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 开区间 (-1, len(nums) - 1)
        left = -1
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            # 红蓝二分染色：以数组末尾元素为基准
            if nums[mid] < nums[-1]:
                right = mid # 处于右半段，蓝色区间向左收缩
            else:
                left = mid  # 处于左半段，红色区间向右收缩

        return nums[right]
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(\log n)$ | 每次通过 `nums[mid] < nums[-1]` 将搜索范围折半，严格满足二分对数复杂度。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用常数个指针变量。 |
