# LeetCode 16. 3Sum Closest (最接近的三数之和)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (高频面试经典题 / 双指针对撞 + 极致剪枝)
- **Tags:** Array, Two Pointers, Sorting, Pruning
- **Corresponding Python File:** [`top-100/lc-0016-3-sum-closest.py`](top-100/lc-0016-3-sum-closest.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.
  * Return the **sum of the three integers**.
  * You may assume that each input would have **exactly one solution**.
* **[CN]** 给你一个长度为 `n` 的整数数组 `nums` 和一个目标值 `target`。请你从 `nums` 中选出三个整数，使它们的和与 `target` 最接近。
  * 返回这 **三个数的和**。
  * 假定每组输入只存在 **恰好一个解**。

### Constraints / 约束条件
* $3 \le \text{nums.length} \le 500$
* $-1000 \le \text{nums}[i] \le 1000$
* $-10^4 \le \text{target} \le 10^4$

---

## 2. Core Idea & Sister Problem Comparison / 核心解法与 LC 15 姊妹题对比

### 💡 核心解题思路
本题是 [LeetCode 15. 3Sum (三数之和)](top-100/lc-0015-3sum.md) 的直接姊妹题，解题脉络高度一致：
1. **排序**：先对数组进行升序排序，使整个数组具备单调性。
2. **固定基准数**：外层循环遍历固定第一个数 $nums[i]$。
3. **双指针对撞**：在剩余右侧区间 $[i + 1, n - 1]$ 内放置首尾双指针 $left$ 和 $right$：
   - 计算当前三数之和 $s = nums[i] + nums[left] + nums[right]$。
   - 若 $|s - target| < |ans - target|$，更新最优解 $ans = s$。
   - 若 $s == target$：绝对差为 0，不可能更接近了，直接返回 $target$。
   - 若 $s > target$：和偏大，将右指针左移 $right -= 1$ 以减小和。
   - 若 $s < target$：和偏小，将左指针右移 $left += 1$ 以增大和。

### 🔄 LC 15 vs LC 16 核心异同点对比：

| 维度 | LC 15. 3Sum (三数之和) | LC 16. 3Sum Closest (最接近的三数之和) |
| :--- | :--- | :--- |
| **目标** | 找出所有和为 `0` 的互不相同的三元组 | 找出三数之和与 `target` 绝对差最小的一个和 |
| **返回值** | `List[List[int]]`（三元组列表） | `int`（三数之和的值） |
| **指针移动依据** | $s > 0 \to right--$；$s < 0 \to left++$；$s == 0 \to$ 记录并双向跳过重复 | 动态维护全局最小差 $|s - target|$，按 $s$ 与 $target$ 大小关系移动指针 |
| **时间复杂度** | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ |
| **空间复杂度** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |

---

## 3. Code Implementation / 代码实现

### 方案 1：标准双指针解法 (Standard Two Pointers)

```python
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # 基准数去重（微优化）
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # 找到完全匹配，直接返回
                if total == target:
                    return target
                
                # 更新全局最接近的和
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                # 调整指针
                if total < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
```

---

### 方案 2：极致双向剪枝优化 (Extreme 2-Way Pruning - 击败 100%)

利用有序数组两端的极端值，可以在每次外层循环中执行 **$\mathcal{O}(1)$ 最小和与最大和剪枝**：

```python
class SolutionOptimized:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            
            # 剪枝 1: 当前 i 能构成的最小和 (x + 后面紧接着的两个最小数)
            min_s = x + nums[i + 1] + nums[i + 2]
            if min_s > target:
                # min_s 已经 > target，i 后续的任何组合只会更大、离 target 更远
                if min_s - target < abs(closest_sum - target):
                    closest_sum = min_s
                break  # 直接终止整个外层循环！
            
            # 剪枝 2: 当前 i 能构成的最大和 (x + 数组末尾两个最大数)
            max_s = x + nums[-2] + nums[-1]
            if max_s < target:
                # max_s 已经 < target，当前 i 的任何组合只会更小、离 target 更远
                if target - max_s < abs(closest_sum - target):
                    closest_sum = max_s
                continue  # 跳过当前 i，尝试更大的 i！
            
            # 正常双指针对撞
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

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

### 1. 数组排序与初始解记录 (Sorting & Base Value)

```python
nums.sort()
n = len(nums)
closest_sum = nums[0] + nums[1] + nums[2]
```

* **[EN] Action:** Sorts `nums` in non-decreasing order and initializes `closest_sum` with the sum of the first 3 elements (`nums[0] + nums[1] + nums[2]`).
  * **Why Sort?** Sorting introduces monotonicity, allowing us to deterministically increase the sum by moving `left` rightwards or decrease the sum by moving `right` leftwards.
* **[CN] 动作**：将数组升序排序，并用数组前 3 个数的和初始化 `closest_sum`。
  * **为什么排序？** 排序使数组具备单调性，使我们能够通过左指针右移单调增大总和、右指针左移单调减小总和。

---

### 2. 最小和与最大和双向剪枝原理 (2-Way Extreme Pruning Explained)

```python
min_s = x + nums[i + 1] + nums[i + 2]
if min_s > target:
    if min_s - target < abs(closest_sum - target):
        closest_sum = min_s
    break
```

* **[EN] Logic:** `min_s` is the minimum possible triplet sum involving `nums[i]`.
  * If `min_s > target`: All other triplets starting at `nums[i]` (and all triplets starting at subsequent larger `nums[i']`) will have a sum $\ge min\_s > target$, which will only be strictly farther away from `target`.
  * Hence, after checking `min_s`, we can immediately **`break`** out of the outer loop!
* **[CN] 逻辑**：`min_s` 是以 `nums[i]` 为首能构成的**绝对最小值**。
  * 若 `min_s > target`：说明以当前 `nums[i]` 以及后续所有更大的 `nums[i']` 为首的三元组和都会 $\ge min\_s > target$，只会与 `target` 差得越来越远！
  * 因此在比较并更新 `min_s` 后，可直接 **`break`** 彻底结束整个外层循环！

---

```python
max_s = x + nums[-2] + nums[-1]
if max_s < target:
    if target - max_s < abs(closest_sum - target):
        closest_sum = max_s
    continue
```

* **[EN] Logic:** `max_s` is the maximum possible triplet sum involving `nums[i]`.
  * If `max_s < target`: All other triplets starting at `nums[i]` will have a sum $\le max\_s < target$, which is farther from `target` than `max_s`.
  * Hence, after checking `max_s`, no other combination with this `nums[i]` can improve the closeness. We can safely **`continue`** to the next `i`!
* **[CN] 逻辑**：`max_s` 是以 `nums[i]` 为首能构成的**绝对最大值**。
  * 若 `max_s < target`：说明以当前 `nums[i]` 为首的所有其他组合和都 $\le max\_s < target$，不可能比 `max_s` 更接近 `target`。
  * 因此在比较并更新 `max_s` 后，无需进入内层双指针，直接 **`continue`** 进入下一个更大的 `i`！

---

### 3. 双指针内层扫描 (Two-Pointer Inward Search)

```python
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
```

* **[EN] Logic:**
  * If `total == target`: Exact match found with difference 0. Return immediately.
  * If `total < target`: The current sum is smaller than `target`. Increment `left` (`left += 1`) to increase `nums[left]`, thus increasing `total`.
  * If `total > target`: The current sum is greater than `target`. Decrement `right` (`right -= 1`) to decrease `nums[right]`, thus decreasing `total`.
* **[CN] 逻辑**：
  * 若 `total == target`：找到与目标完全一致的和（差值为 0），无需继续搜索，直接返回 `target`。
  * 若 `total < target`：当前和偏小，左指针右移 `left += 1` 以增大 `nums[left]`。
  * 若 `total > target`：当前和偏大，右指针左移 `right -= 1` 以减小 `nums[right]`。

---

## 5. Step-by-Step Walkthrough with Examples / 样例图解分析

### 样例 1: `nums = [-1, 2, 1, -4]`, `target = 1`

* **步骤 1：升序排序**
  * `nums = [-4, -1, 1, 2]` ($n = 4$)
  * 初始 `closest_sum = (-4) + (-1) + 1 = -4`（差值为 $|-4 - 1| = 5$）

* **步骤 2：外层 $i = 0$ ($x = -4$)**
  * `min_s = -4 + (-1) + 1 = -4 < 1`
  * `max_s = -4 + 1 + 2 = -1 < 1` $\to$ `abs(-1 - 1) = 2 < 5`，更新 `closest_sum = -1`。触发 `max_s` 剪枝，直接跳过内层循环。

* **步骤 3：外层 $i = 1$ ($x = -1$)**
  * `min_s = -1 + 1 + 2 = 2 > 1` $\to$ `abs(2 - 1) = 1 < 2`，更新 `closest_sum = 2`。
  * 因为 `min_s > 1`，触发 `min_s` 剪枝，直接 **`break`** 终止整个外层循环！

* **最终返回**：`closest_sum = 2`（对应三元组 `[-1, 1, 2]`，和为 2，距离 `target = 1` 仅相差 1），完全正确！

---

## 6. Key FAQs & Edge Cases / 核心答疑与边界分析

### Q1: 为什么不能直接用 `float("inf")` 初始化 `closest_sum`？
* 如果初始化 `closest_sum = float("inf")`，在计算 `abs(closest_sum - target)` 时可能会涉及浮点数减法，且最终返回需要转换为 `int`。
* 最标准、最安全的做法是用数组前三个数的和 `nums[0] + nums[1] + nums[2]` 初始化，保证类型始终为整型且必然来自数组的一个合法三元组。

### Q2: 为什么这道题不需要像 LC 15 那样在内层循环对 `left` 和 `right` 进行深度跳重？
* 在 LC 15 中，需要找出**所有不重复**的三元组，因此一旦找到一个解必须跳过所有相同数字以防重复加入结果列表。
* 在 LC 16 中，目标仅是维护一个全局最优的**单一数值和**，跳重虽然能带来微量性能提升，但即使不跳重也不影响正确性，单步 `left += 1` 和 `right -= 1` 依然能正确遍历到所有关键状态。

---

## 7. Complexity Analysis / 复杂度分析

| 指标 | 复杂度 | 详解 |
| :--- | :--- | :--- |
| **时间复杂度 (Time)** | $\mathcal{O}(n^2)$ | 数组排序耗时 $\mathcal{O}(n \log n)$；外层循环遍历 $n$ 个数，内层双指针对撞扫描最多 $\mathcal{O}(n)$ 次。加上极值剪枝后实际运行时间大幅优于 $\mathcal{O}(n^2)$。 |
| **空间复杂度 (Space)** | $\mathcal{O}(1)$ (或 $\mathcal{O}(\log n)$) | 仅使用常数个辅助变量（`i`, `left`, `right`, `total`, `closest_sum`）；排序消耗 $\mathcal{O}(\log n)$ 栈空间。 |
