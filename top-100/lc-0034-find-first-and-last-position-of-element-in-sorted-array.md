# LeetCode 34. Find First and Last Position of Element in Sorted Array (在排序数组中查找元素的第一个和最后一个位置)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (高频面试经典题 / 二分查找模版题)
- **Tags:** Array, Binary Search
- **Corresponding Python File:** [`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py`](file:///Users/stevenhuang/Desktop/leetcode-sh/top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.
  * If `target` is not found in the array, return `[-1, -1]`.
  * **Requirement:** You must write an algorithm with $\mathcal{O}(\log n)$ runtime complexity.
* **[CN]** 给你一个按照非递减顺序排列的整数数组 `nums` ，和一个目标值 `target` 。请你找出给定目标值在数组中的开始位置和结束位置。
  * 如果数组中不存在目标值 `target` ，返回 `[-1, -1]` 。
  * **要求**：你必须设计并实现时间复杂度为 $\mathcal{O}(\log n)$ 的算法解决此问题。

---

## 2. Core Idea: The Universal `lower_bound` Framework / 核心解法：万能 `lower_bound` 体系

在有序数组中，所有四种常见的二分查找需求，均可转化为求 **大于等于某个值的第一个下标**（即 `lower_bound`）：

| 查询需求 | 含义描述 | 转化为 `lower_bound` 的等价写法 | 备注说明 |
| :--- | :--- | :--- | :--- |
| **$\ge x$** | 第一个 $\ge x$ 的位置 | `lower_bound(nums, x)` | 基础原型 |
| **$> x$** | 第一个 $> x$ 的位置 | `lower_bound(nums, x + 1)` | 等价于 $\ge (x + 1)$（整数范围内） |
| **$< x$** | 最后一个 $< x$ 的位置 | `lower_bound(nums, x) - 1` | 第一个 $\ge x$ 的前一个位置 |
| **$\le x$** | 最后一个 $\le x$ 的位置 | `lower_bound(nums, x + 1) - 1` | 第一个 $> x$ 的前一个位置 |

### 本题应用：
1. **寻找起始位置 (Start Index)**：即寻找数组中第一个 $\ge target$ 的位置：
   $$\text{start} = \text{lower\_bound}(nums, target)$$
   * **特判**：若 $\text{start} == len(nums)$（所有数都比 $target$ 小）或 $nums[\text{start}] \neq target$（数组中无 $target$），说明 $target$ 不存在，直接返回 `[-1, -1]`。
2. **寻找结束位置 (End Index)**：即寻找数组中最后一个 $\le target$ 的位置，等价于 **第一个 $> target$（即 $\ge target + 1$）的前一个位置**：
   $$\text{end} = \text{lower\_bound}(nums, target + 1) - 1$$
3. 返回 `[start, end]`。

---

## 3. Code Implementation / 代码实现

```python
from typing import List

# 闭区间写法 [left, right]
def lower_bound(nums: List[int], target: int) -> int:
    """
    返回最小的满足 nums[i] >= target 的下标 i。
    若不存在（即所有元素均 < target），返回 len(nums)。
    """
    left = 0
    right = len(nums) - 1  # 闭区间 [left, right]
    
    while left <= right:   # 当区间不为空时循环
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1  # 目标在右半部分，范围缩小为 [mid + 1, right]
        else:
            right = mid - 1 # 目标在左半部分或当前 mid，范围缩小为 [left, mid - 1]
            
    return left  # 循环结束时 right + 1 == left，left 即为第一个 >= target 的位置


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1. 查找第一个 >= target 的位置
        start = lower_bound(nums, target)
        
        # 2. 判断 target 是否在数组中存在
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
            
        # 3. 查找最后一个 <= target 的位置（即第一个 >= target + 1 的位置减 1）
        end = lower_bound(nums, target + 1) - 1
        
        return [start, end]
```

---

## 4. The Three Interval Paradigms / 二分查找的三种区间模版深度对比

二分查找的核心在于**区间定义（循环不变量）**，不同区间的定义决定了边界更新和终止条件：

```
闭区间 [left, right]       左闭右开 [left, right)      开区间 (left, right)
  left       right            left         right          left       right
   ↓           ↓               ↓             ↓             ↓           ↓
[  .   .   .   .  ]         [  .   .   .   .  )         (  .   .   .   .  )
```

| 维度 | 1. 闭区间 `[left, right]` | 2. 左闭右开 `[left, right)` | 3. 开区间 `(left, right)` |
| :--- | :--- | :--- | :--- |
| **初始化** | `left = 0, right = n - 1` | `left = 0, right = n` | `left = -1, right = n` |
| **循环条件** | `while left <= right:` | `while left < right:` | `while left + 1 < right:` |
| **若 $nums[mid] < target$** | `left = mid + 1` | `left = mid + 1` | `left = mid` |
| **若 $nums[mid] \ge target$** | `right = mid - 1` | `right = mid` | `right = mid` |
| **循环结束状态** | `right + 1 == left` | `left == right` | `left + 1 == right` |
| **返回值** | `return left` (或 `right + 1`) | `return left` (或 `right`) | `return right` (或 `left + 1`) |

### 三种模版的完整代码对比：

```python
# 1. 闭区间模版 [left, right]
def lower_bound_closed(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# 2. 左闭右开模版 [left, right)
def lower_bound_half_open(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# 3. 开区间模版 (left, right)
def lower_bound_open(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    return right
```

---

## 5. Step-by-Step Walkthrough with Example / 样例图解分析

假设 `nums = [5, 7, 7, 8, 8, 10]`, `target = 8`

### 第一步：查找起始点 `start = lower_bound(nums, 8)`
* 初始：`left = 0`, `right = 5` (区间 `[0, 5]`)
  * `mid = (0 + 5) // 2 = 2`，`nums[2] = 7 < 8` $\to$ `left = mid + 1 = 3`
  * `mid = (3 + 5) // 2 = 4`，`nums[4] = 8 >= 8` $\to$ `right = mid - 1 = 3`
  * `mid = (3 + 3) // 2 = 3`，`nums[3] = 8 >= 8` $\to$ `right = mid - 1 = 2`
* 循环结束（`left = 3 > right = 2`），返回 `left = 3`。
* 检查：`start = 3 < 6` 且 `nums[3] == 8`，有效。

### 第二步：查找结束点 `end = lower_bound(nums, 9) - 1`
* 查找第一个 $\ge 9$ 的位置：
  * 初始：`left = 0`, `right = 5`
  * 经过二分定位到 `nums[5] = 10 >= 9`，最终 `lower_bound(nums, 9)` 返回下标 `5`。
* `end = 5 - 1 = 4`。
* 最终返回 `[start, end] = [3, 4]`。

---

## 6. Key FAQs & Edge Cases / 核心答疑与边界分析

### Q1: 为什么要对 `start` 做双重检查 (`start == len(nums)` 或 `nums[start] != target`)？
* **情况 1（`start == len(nums)`）**：当 `target` 比数组中所有元素都大时（如在 `[5, 7, 7]` 中搜 `8`），二分查找会一直向右移动 `left`，最终 `left = len(nums)`。此时如果直接访问 `nums[start]` 会引发 **IndexError (数组越界)**。
* **情况 2（`nums[start] != target`）**：当 `target` 不在数组中，但处于数组数值范围内时（如在 `[5, 7, 7, 10]` 中搜 `8`），`lower_bound` 会返回第一个大于 `8` 的元素下标（即 `10` 对应的下标 `3`）。此时 `nums[start] == 10 != 8`，说明 `8` 不存在。

### Q2: 为什么 `end` 计算时不需要再额外特判是否存在？
* 如果 `start` 的特判通过了，说明数组中**至少存在一个**等于 `target` 的元素。
* 因此 `target + 1` 的 `lower_bound` 减 1 必然落在有效的合法下标上，且 `nums[end]` 必然等于 `target`。

### Q3: 为什么 `mid` 的计算推荐写成 `left + (right - left) // 2`？
* 在 Python 中整数不会溢出，但对于 C++ / Java 等强类型语言，如果 `left` 和 `right` 很大，`left + right` 可能会超过 32 位整型上限导致**整型溢出 (Integer Overflow)**。养成 `left + (right - left) // 2` 的习惯是算法工程的最佳实践。

---

## 7. Complexity Analysis / 复杂度分析

| 指标 | 复杂度 | 详解 |
| :--- | :--- | :--- |
| **时间复杂度 (Time)** | $\mathcal{O}(\log n)$ | 调用了两次标准的二分查找，每次耗时 $\mathcal{O}(\log n)$，整体仍为对数时间复杂度。 |
| **空间复杂度 (Space)** | $\mathcal{O}(1)$ | 仅使用常数个辅助变量（`left`, `right`, `mid`, `start`, `end`），无任何额外内存开销。 |
