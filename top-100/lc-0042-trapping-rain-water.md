# LeetCode 42. Trapping Rain Water (接雨水)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Hard (双指针 / 前缀后缀最值 / 柱体容积短板效应 / 空间降维)
- **Tags:** Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
- **Corresponding Python File:** [`top-100/lc-0042-trapping-rain-water.py`](top-100/lc-0042-trapping-rain-water.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.
* **[CN]** 给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

### Constraints / 约束条件
* $n == \text{height.length}$
* $1 \le n \le 2 \times 10^4$
* $0 \le \text{height}[i] \le 10^5$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 单柱储水基本公理 (Column Water Invariant):                               │
│    • 下标 i 处的储水量等于左右两侧最大柱高短板减去自身高度：                │
│      Water(i) = min(pre_max[i], suf_max[i]) - height[i]                      │
│ 2. 空间 O(1) 双指针优化原理 (Two Pointers Space Reduction):                  │
│    • 维护 pre_max 与 suf_max。                                              │
│    • 若 pre_max < suf_max: 当前 left 处的瓶颈必然是 pre_max，右侧肯定有 >=  │
│      suf_max 的更高挡板。因此 water = pre_max - height[left]，left += 1。   │
│    • 若 suf_max <= pre_max: 同理处理 right 侧，right -= 1。                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0042-trapping-rain-water.py`](top-100/lc-0042-trapping-rain-water.py) 中的双解法进行深入解析：

### 解法一：前缀/后缀最值数组法 (`Solution` - $\mathcal{O}(n)$ 空间)

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        # 1. 预处理前缀最大值
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        # 2. 预处理后缀最大值
        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        # 3. 计算每个位置储水并累加
        result = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            result += min(pre, suf) - h

        return result
```

---

### 解法二：对撞双指针空间优化法 (`Solution2` - $\mathcal{O}(1)$ 空间)

```python
class Solution2:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        left = 0
        right = n - 1
        pre_max = 0
        suf_max = 0

        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])

            # 决定哪一侧是真正的短板
            if pre_max < suf_max:
                result += pre_max - height[left]
                left += 1
            else:
                result += suf_max - height[right]
                right -= 1
                
        return result
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 无论是前后缀预处理还是双指针单次遍历，所有柱子均被访问常数次，运行时间严格为 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 解法二仅维护 `left`, `right`, `pre_max`, `suf_max` 4 个变量，额外空间为 $\mathcal{O}(1)$（解法一为 $\mathcal{O}(n)$）。 |
