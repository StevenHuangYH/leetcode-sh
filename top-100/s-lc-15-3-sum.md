# LeetCode 15. 3Sum (三数之和)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (高频面试经典题 / 双指针 + 极致剪枝)
- **Tags:** Array, Two Pointers, Sorting, Pruning
- **Corresponding Python File:** [`top-100/s-lc-15-3-sum.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/top-100/s-lc-15-3-sum.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
  * **Note:** The solution set must **not contain duplicate triplets**.
* **[CN]** 给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。
  * **注意：** 答案中**不可以包含重复的三元组**。

---

## 2. Code Implementation / 代码实现

```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(0, n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue

            # Optimization 1: 最小和剪枝 (全停)
            if x + nums[i + 1] + nums[i + 2] > 0:
                break

            # Optimization 2: 最大和剪枝 (跳过当前)
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
```

---

## 3. Step-by-Step Walkthrough / 逐步核心逻辑

1. **先排序 (`nums.sort()`)**：赋予单调性，让双指针向内收缩调节大小。
2. **基准数去重 (`if i > 0 and x == nums[i-1]: continue`)**：防止不同轮次枚举相同的第一个数导致三元组重复。
3. **最小和剪枝 (Optimization 1)**：`x + nums[i+1] + nums[i+2] > 0` $\rightarrow$ 即使搭配最小两数和依然 $>0$，后续全部必定 $>0$，直接 **`break`**。
4. **最大和剪枝 (Optimization 2)**：`x + nums[-2] + nums[-1] < 0` $\rightarrow$ 搭配最大两数依然 $<0$，当前 $x$ 无解，跳过当前轮次 **`continue`**。
5. **双指针收缩与去重 (`j` & `k`)**：找到解后，`j += 1` 并跳过连续相同的左侧数字，`k -= 1` 并跳过连续相同的右侧数字。

---

## 4. Complexity Analysis / 复杂度分析

* **时间复杂度 (Time):** $\mathcal{O}(n^2)$（实际运行大幅优于常规解法）
* **空间复杂度 (Space):** $\mathcal{O}(1)$ 或 $\mathcal{O}(\log n)$
