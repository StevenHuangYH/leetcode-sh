# LeetCode 209. Minimum Size Subarray Sum (长度最小的子数组)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (滑动窗口 / 双指针 / 连续子数组和单调性 / 最小长度维护)
- **Tags:** Array, Binary Search, Sliding Window, Prefix Sum
- **Corresponding Python File:** [`top-100/lc-0209-minimum-size-subarray-sum.py`](top-100/lc-0209-minimum-size-subarray-sum.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.
* **[CN]** 给定一个含有 `n` 个正整数的数组和一个正整数 `target` 。找出该数组中满足其总和大于等于 `target` 的长度最小的 **连续子数组** ，并返回其长度。如果不存在符合条件的子数组，返回 `0` 。

### Constraints / 约束条件
* $1 \le \text{target} \le 10^9$
* $1 \le \text{nums.length} \le 10^5$
* $1 \le \text{nums}[i] \le 10^4$ (所有元素均为严格正整数)

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 正整数单调累加性质 (Positive Numbers Invariant):                         │
│    • 因为 nums[i] > 0，窗口右移扩大和单调增加，左移收缩和单调减小。         │
│ 2. 滑动窗口收缩不变量 (Minimizing Window Invariant):                        │
│    • 当窗口和 s >= target 时，记录长度 ans = min(ans, right - left + 1)；    │
│    • 随后左指针右移 s -= nums[left]; left += 1，寻找更短的合法窗口。         │
│ 3. 哨兵初始值与无解判定: ans 初始为 n + 1，若最终 ans <= n 则返回 ans，否则 0。│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0209-minimum-size-subarray-sum.py`](top-100/lc-0209-minimum-size-subarray-sum.py) 中的实现进行逐行深入解析：

```python
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1 # 1. 哨兵初始值设置为不可能达到的极大值 n + 1
        s = 0       # 2. 记录当前窗口内元素之和
        left = 0    # 3. 初始化滑动窗口左指针

        # 4. 枚举窗口右边界
        for right, x in enumerate(nums):
            s += x  # 扩展窗口，累加元素
          
            # 5. 核心收缩：当窗口和满足条件 >= target 时，持续尝试收缩左端点以求最短长度
            while s >= target:
                ans = min(ans, right - left + 1) # 维护全局最小长度
                s -= nums[left]                  # 移出左端元素
                left += 1                        # 左指针右移

        # 6. 若 ans 仍为初始值 n + 1 说明无解返回 0，否则返回最小长度 ans
        return ans if ans <= n else 0
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 每个元素最多被 `right` 访问一次，被 `left` 移出一次，双指针各扫描数组一次，总时间严格为 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用常数个辅助变量维护窗口状态。 |
