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

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 🎤 追问 1: 相比 LC 15 (3Sum)，本题的去重逻辑有哪些本质区别？
* **面试官意图**: 考察对“搜索最优解”与“枚举全解集”两种问题形态的不变量区别。
* **回答核心**:
  * 在 LC 15 中，必须收集**所有不重复的三元组**，因此在固定 $i$ 后，内层双指针移动时遇到相同数字必须 `while nums[left] == nums[left+1]: left += 1` 彻底跳过重复元素以避免结果集重复。
  * 在本题 LC 16 中，目标是寻找**全局唯一的最小距离数值**。外层循环 `nums[i] == nums[i-1]` 的跳过依然是有效的去重加速，但内层无需严格跳过所有重复数值，因为相同数值只会计算出相同的 `total` 并被单调性指针自动推进，不影响最终返回的标量结果。

### 🎤 追问 2: 方案 2 中的 2-Way 剪枝是如何实现常数级加速的？
* **回答核心**:
  * 排序后数组具备严格递增性。在固定第一个数 $x = \text{nums}[i]$ 后：
    1. **最小值下界**: $x + \text{nums}[i+1] + \text{nums}[i+2]$ 是包含 $x$ 的最小可能和。如果它已经比 `target` 大，那么后续无论如何选，和都只会更大、距离只会更远，因此不仅当前 $i$ 无需双指针，后续所有更大的 $i$ 都可以直接 `break` 终止。
    2. **最大值上界**: $x + \text{nums}[n-2] + \text{nums}[n-1]$ 是包含 $x$ 的最大可能和。如果它仍比 `target` 小，说明当前 $i$ 下的最大组合都达不到 `target`，内层无需逐个尝试，更新可能的最优值后直接 `continue` 跳到下一个更大的 $i$。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ 错题排查与反模式诊断 (The Error Log: Anti-Patterns & Defensive Fixes)

| 常见陷阱 / 易错反模式 (Buggy Pattern / Traps) | 错误现象与测试用例 (Symptom & Fail Case) | 根本原因分析 (Root Cause) | 防御性修复与循环不变量 (Defensive Fix & Invariant) |
| :--- | :--- | :--- | :--- |
| **`closest_sum` 初始化为 0 或无穷大** | `nums=[-1,2,1,-4], target=1` 时若初值为 0，误把 0 当作合法和 | 0 可能不是数组中任何三个数的和 | 严格使用真实三数之和初始化 `nums[0] + nums[1] + nums[2]` |
| **距离判断忘记取绝对值 `abs()`** | 当 `total < target` 时直接比对差值大小得出错误结论 | 距离为无向几何距离 $\| \text{sum} - \text{target} \|$ | 严格使用 `abs(total - target) < abs(closest_sum - target)` |
| **剪枝 1 误写为 `continue` 而非 `break`** | 失去提前终止整个外层循环的最佳优化机会 | 排序后后续更大 $i$ 的最小和必然更偏离 `target` | 当前最小和 $> \text{target}$ 时更新后直接 `break` |

---

### 🎨 实例全程推演表 (Complete Dry-Run)

**输入**: `nums = [-1, 2, 1, -4]`, `target = 1`  
**排序后**: `nums = [-4, -1, 1, 2]`, `closest_sum = -4 + (-1) + 1 = -4` (距离 $|-4 - 1| = 5$)

| 轮次 | $i$ / $x$ | `left` / `right` | `total` | 距离 $\| \text{total} - 1 \|$ | `closest_sum` | 指针移动 |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1-1** | $i=0$ ($x=-4$) | $L=1$ ($-1$), $R=3$ ($2$) | $-3$ | $\|-3 - 1\| = 4$ | **$-3$** (更优) | $-3 < 1 \implies L \to 2$ |
| **1-2** | $i=0$ ($x=-4$) | $L=2$ ($1$), $R=3$ ($2$) | $-1$ | $\|-1 - 1\| = 2$ | **$-1$** (更优) | $-1 < 1 \implies L \to 3$ (终止内层) |
| **2-1** | $i=1$ ($x=-1$) | $L=2$ ($1$), $R=3$ ($2$) | **$2$** | $\|2 - 1\| = 1$ | **$2$** (更优) | $2 > 1 \implies R \to 2$ (终止内层) |
| **结果** | — | — | — | — | **$2$** | 最终输出 **`2`** |

---

### ❓ 常见疑难与边界排查 (Boundary FAQs)

* **Q1: 数组长度恰好为 3 时会怎样？**
  * 外层循环 `range(n - 2)` 仅执行 $i = 0$ 一次，内层 $L=1, R=2$ 计算唯一的三数之和并直接返回，完全正确。
* **Q2: 数组存在负数、目标值为负数时公式是否依然成立？**
  * 是。绝对值距离函数 $\| \text{total} - \text{target} \|$ 在全实数域上度量几何距离，正负数均保持单调性。

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n^2)$ | 数组排序耗时 $\mathcal{O}(n \log n)$；外层遍历 $n-2$ 次，内层双指针对撞最多移动 $n$ 次。加入 2-Way 剪枝后大幅减少无效迭代。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用常数个辅助变量维护最优和与双指针，额外空间复杂度严格为 $\mathcal{O}(1)$。 |
