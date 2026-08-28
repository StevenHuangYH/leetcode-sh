# LeetCode 3471. Find the Largest Almost Missing Integer (找出最大的几乎缺失整数)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (定长滑动窗口 / 集合去重 / 数学分类讨论 / 边界极值分析)
- **Tags:** Array, Hash Table
- **Corresponding Python File:** [`daily-practice/lc-3471-find-the-largest-almost-missing-integer.py`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** You are given an integer array `nums` and an integer `k`. An integer `x` is **almost missing** from `nums` if `x` appears in **exactly one** subarray of size `k` within `nums`. Return the **largest** almost missing integer, or `-1` if no such integer exists.
* **[CN]** 给你一个整数数组 `nums` 和一个整数 `k` 。如果整数 `x` 恰好在 `nums` 中 **仅一个** 大小为 `k` 的子数组中出现，则称 `x` 是一个 **几乎缺失的整数** 。返回 **最大的** 几乎缺失整数，如果不存在这样的整数，则返回 `-1` 。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 定长窗口滑窗统计法 (General Sliding Window):                             │
│    • 滑动长度为 k 的窗口，对每个窗口 set(window) 去重，频数加 1。            │
│    • 统计所有 count == 1 的最大元素。                                        │
│ 2. O(n) 数学分类讨论公理 (Mathematical Bound Invariant):                    │
│    • 情况 1: k == 1 -> 每个元素自成窗口，寻找在全数组中仅出现 1 次的最大元素。  │
│    • 情况 2: k == n -> 整个数组是唯一窗口，直接返回 max(nums)。               │
│    • 情况 3: 1 < k < n -> 只有首端点 nums[0] 和尾端点 nums[-1] 可能恰好被 1   │
│      个窗口包含（中间元素必然被 >= 2 个窗口包含）。比较全局频数为 1 的端点。 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`daily-practice/lc-3471-find-the-largest-almost-missing-integer.py`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.py) 中的双实现进行逐行深入解析：

```python
from typing import List
from collections import Counter

# 方案 1: 定长滑动窗口模拟
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        window_counts = {}
        
        # 滑动大小为 k 的窗口
        for i in range(len(nums) - k + 1):
            current_window = nums[i : i + k]
            # 同一窗口内重复出现的数字仅计数一次
            for num in set(current_window):
                window_counts[num] = window_counts.get(num, 0) + 1
        
        # 寻找恰好出现在 1 个窗口中的最大值
        max_val = -1
        for num, count in window_counts.items():
            if count == 1:
                max_val = max(max_val, num)
                
        return max_val

# 方案 2: O(n) 最优数学分类讨论
class SolutionOptimal:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)
        
        # 情况 1: k == 1
        if k == 1:
            unique_nums = [x for x, c in freq.items() if c == 1]
            return max(unique_nums) if unique_nums else -1
        
        # 情况 2: k == n
        if k == n:
            return max(nums)
        
        # 情况 3: 1 < k < n，仅需检查两端元素
        candidates = []
        if freq[nums[0]] == 1:
            candidates.append(nums[0])
        if freq[nums[-1]] == 1:
            candidates.append(nums[-1])
            
        return max(candidates) if candidates else -1
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 数学分类法通过 `Counter(nums)` 线性统计元素频数，后续 $O(1)$ 判定；定长滑窗耗时 $\mathcal{O}(n \cdot k)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(n)$ | 哈希表存储不同元素的出现频数。 |
