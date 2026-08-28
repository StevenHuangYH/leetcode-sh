# LeetCode 167. Two Sum II - Input Array Is Sorted (两数之和 II - 输入有序数组)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (有序数组对撞双指针 / 1-Indexed 返回 / 单调性空间收缩)
- **Tags:** Array, Two Pointers, Binary Search
- **Corresponding Python File:** [`top-100/lc-0167-two-sum-ii-input-array-is-sorted.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers added by one.
* **[CN]** 给你一个下标从 **1 开始** 的整数数组 `numbers` ，该数组已按 **非递减顺序排列** ，请你从数组中找出满足相加之和等于目标数 `target` 的两个数。返回这两个数的下标值（1-indexed）。

### Constraints / 约束条件
* $2 \le \text{numbers.length} \le 3 \times 10^4$
* $-1000 \le \text{numbers}[i] \le 1000$
* `numbers` 按 **非递减顺序** 排列
* 题目保证 **存在且仅存在一个有效答案**

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 有序单调收敛不变量 (Sorted Inward Convergence Invariant):                │
│    • left = 0, right = n - 1。                                              │
│    • 若 sum > target: 说明当前 numbers[right] 太大，任何与 right 搭配的数   │
│      和都会 > target，安全排除右侧：right -= 1。                            │
│    • 若 sum < target: 说明当前 numbers[left] 太小，安全排除左侧：left += 1。 │
│ 2. 1-Based Index 要求: 返回 [left + 1, right + 1]。                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0167-two-sum-ii-input-array-is-sorted.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py) 中的实现进行逐行深入解析：

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. 初始化两端对撞指针
        left = 0
        n = len(numbers)
        right = n - 1

        # 2. 向内收缩循环
        while left < right:
            result = numbers[left] + numbers[right]

            # 命中目标值直接 break 退出循环
            if result == target:
                break
            # 和偏大，右指针左移减小和
            if result > target:
                right -= 1
            # 和偏小，左指针右移增大和
            else:
                left += 1

        # 3. 转换为 1-based 下标返回
        return [left + 1, right + 1]
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 双指针从两端向内逼近，每轮循环必移动一个指针，最多扫描 $n$ 个元素，线性时间。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用 `left`, `right`, `result` 等常数个局部变量。 |
