# LeetCode 16. 3Sum Closest (最接近的三数之和)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (排序 + 双指针 + 距离绝对值最小化 + 2-Way 极限剪枝)
- **Tags:** Array, Two Pointers, Sorting
- **Corresponding Python File:** [`top-100/lc-0016-3-sum-closest.py`](top-100/lc-0016-3-sum-closest.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return *the sum of the three integers*. You may assume that each input would have exactly one solution.
* **[CN]** 给你一个长度为 `n` 的整数数组 `nums` 和 一个目标值 `target`。请你从 `nums` 中选出三个整数，使它们的和与 `target` 最接近。返回这三个数的和。假定每组输入只存在恰好一个解。

### Constraints / 约束条件
* $3 \le \text{nums.length} \le 500$
* $-1000 \le \text{nums}[i] \le 1000$
* $-10^4 \le \text{target} \le 10^4$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 距离单调性不变量 (Distance Monotonicity Invariant):                      │
│    • 目标是最小化 abs(sum - target)。                                       │
│    • 当 total < target 时，只能让 left += 1 增大和；                         │
│    • 当 total > target 时，只能让 right -= 1 减小和；                        │
│    • 当 total == target 时，距离为 0，已达理论最优，直接提前 return target。  │
│ 2. 2-Way 极致极值剪枝 (Extreme 2-Way Bound Pruning):                         │
│    • 剪枝 1: min_s = x + nums[i+1] + nums[i+2] > target，若该最小和比历史最优│
│      还更接近 target，更新后直接 break（后续更大 i 的和只会更偏离）。         │
│    • 剪枝 2: max_s = x + nums[-2] + nums[-1] < target，若该最大和更接近，   │
│      更新后直接 continue（当前 i 的其他和只会更小，直接跳过双指针）。        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 3Sum 系列演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 3Sum & Closest Extremum Lineage (三数之和变体思维谱系图)                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Exact Zero Sum): LC 15 3Sum                                       │
│  └─ 精确匹配目标值: total == 0 收集，严格去重跳过重复项                      │
│        │                                                                    │
│        ▼ [演进 Twist: 宽松匹配 + 距离绝对值动态更新 (Distance Minimize)]     │
│  Level 2 (Closest Target Sum): LC 16 3Sum Closest (本题★)                   │
│  └─ 核心: 实时维护 abs(total - target) 极小值，total == target 时立即短路   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0016-3-sum-closest.py`](top-100/lc-0016-3-sum-closest.py) 中的双方案实现进行逐行深入解析：

```python
from typing import List

# 方案 1: 标准对撞双指针 (Standard Two Pointers)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2] # 初始化最接近和
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # 理论最优短路
                if total == target:
                    return target
                
                # 维护更接近 target 的和
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                if total < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum

# 方案 2: 极致双向剪枝优化 (Extreme 2-Way Pruning)
class SolutionOptimized:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            
            # 剪枝 1: 当前 i 对应的最小三数之和
            min_s = x + nums[i + 1] + nums[i + 2]
            if min_s > target:
                if min_s - target < abs(closest_sum - target):
                    closest_sum = min_s
                break  # 后续更大的 i 只会更大，直接终止外层循环
            
            # 剪枝 2: 当前 i 对应的最大三数之和
            max_s = x + nums[-2] + nums[-1]
            if max_s < target:
                if target - max_s < abs(closest_sum - target):
                    closest_sum = max_s
                continue  # 当前 i 无法更接近 target，直接跳过内层循环
            
            left = i + 1
            right = n - 1
            while left < right:
                total = x + nums[left] + nums[right]
                if total == target:
                    return target
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                if total < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
```

---

## 5. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n^2)$ | 数组排序 $\mathcal{O}(n \log n)$，外层遍历 $n$ 次，内层双指针对撞最多移动 $n$ 次。加入 2-Way 剪枝后大幅减少无效循环。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用常数个辅助变量，额外空间复杂度严格为 $\mathcal{O}(1)$。 |
