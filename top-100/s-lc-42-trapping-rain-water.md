# LeetCode 42. Trapping Rain Water (接雨水)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Hard (高频面试经典题 / 前后缀最大值 & 双指针)
- **Tags:** Array, Two Pointers, Dynamic Programming, Stack
- **Corresponding Python File:** [`top-100/s-lc-42-trapping-rain-water.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/top-100/s-lc-42-trapping-rain-water.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
* **[CN]** 给定 `n` 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

---

## 2. Core Principle / 核心原理

每个位置 $i$ 能接的雨水量取决于其**左侧最高柱子**和**右侧最高柱子**的较小值：
$$\text{water}[i] = \max(0, \min(\text{pre\_max}[i], \text{suf\_max}[i]) - \text{height}[i])$$

---

## 3. Code Implementations / 代码实现

### 方案 1：前后缀最大值数组 (Prefix & Suffix Max - DP)

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        result = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            result += min(pre, suf) - h

        return result
```

* **时间复杂度:** $\mathcal{O}(n)$ | **空间复杂度:** $\mathcal{O}(n)$

---

### 方案 2：对撞双指针空间优化 (Two Pointers - Optimal $\mathcal{O}(1)$ Space)

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
            
            # 若左侧历史最高 < 右侧历史最高，则当前 left 处的接水量由 pre_max 决定
            if pre_max < suf_max:
                result += pre_max - height[left]
                left += 1
            else:
                result += suf_max - height[right]
                right -= 1
                
        return result
```

* **时间复杂度:** $\mathcal{O}(n)$ | **空间复杂度:** $\mathcal{O}(1)$
