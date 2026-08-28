# LeetCode 33. Search in Rotated Sorted Array (搜索旋转排序数组)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (二分查找 / 红蓝开区间二分 / 旋转有序分段 / 分类讨论)
- **Tags:** Array, Binary Search
- **Corresponding Python File:** [`top-100/lc-0033-search-in-rotated-sorted-array.py`](top-100/lc-0033-search-in-rotated-sorted-array.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the sorted rotated array `nums` of unique integers and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`. You must write an algorithm with $O(\log n)$ runtime complexity.
* **[CN]** 整数数组 `nums` 按升序排列，数组中的值 **互不相同** 。在传递给函数之前，`nums` 在预先未知的某个下标上进行了旋转。给你 旋转后 的数组 `nums` 和一个整数 `target` ，如果 `nums` 中存在这个目标值 `target` ，则返回它的下标，否则返回 `-1` 。你必须设计一个时间复杂度为 $O(\log n)$ 的算法解决此问题。

### Constraints / 约束条件
* $1 \le \text{nums.length} \le 5000$
* $-10^4 \le \text{nums}[i], \text{target} \le 10^4$
* `nums` 中的每个值都 **独一无二**

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 旋转断点与参考锚点不变量 (Reference Element Invariant):                   │
│    • 以末尾元素 x = nums[-1] 为基准：                                       │
│      - 若 nums[i] > x: 说明 nums[i] 位于左侧上半段阶梯；                     │
│      - 若 nums[i] <= x: 说明 nums[i] 位于右侧下半段阶梯。                    │
│ 2. 二分决策真值表 (Decision Truth Table for is_blue(mid)):                   │
│    • 若 target > x (目标在上半段):                                           │
│      - 仅当 nums[mid] > x 且 nums[mid] >= target 时，mid 处于 target 右侧 (蓝)│
│    • 若 target <= x (目标在下半段):                                          │
│      - 若 nums[mid] > x (在上半段)，说明 mid 在 target 左侧 (红)；            │
│      - 若 nums[mid] <= x (在下半段)，当 nums[mid] >= target 时为蓝。          │
│ 3. 开区间边界: left = -1, right = n - 1，二分收敛后检查 nums[right] == target。 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0033-search-in-rotated-sorted-array.py`](top-100/lc-0033-search-in-rotated-sorted-array.py) 中的实现进行逐行深入解析：

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def is_blue(i: int) -> bool:
            end = nums[-1]
            # 情况 1: target 位于左侧高段
            if target > end:
                return nums[i] > end and nums[i] >= target
            # 情况 2: target 位于右侧低段
            else:
                return nums[i] <= end and nums[i] >= target

        # 开区间二分 (-1, len(nums) - 1)
        left = -1
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid # 蓝色向左收缩
            else:
                left = mid  # 红色向右收缩

        # 检查收敛点是否命中 target
        return right if nums[right] == target else -1
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(\log n)$ | 每次通过 `is_blue(mid)` 判断将搜索空间减半，严格满足二分对数时间复杂度。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用常数个指针与闭包变量。 |
