# LC 0704: Binary Search | 二分查找

- **LeetCode ID**: LC 0704
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 02: Binary Search)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/binary-search/)
- **Solution File**: [`07-lc-0704-binary-search.py`](luffy/07-lc-0704-binary-search.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

### [CN] 中文描述
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

### Constraints / 约束条件
1 <= nums.length <= 10^4, -10^4 < nums[i], target < 10^4

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 闭区间二分: left=0, right=n-1, while left <= right     │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
搜索区间不变量：目标值若存在必在 $[left, right]$ 中。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List

#binary search
#left closed and right closed interval

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) #binary search property

        mid = (left + right) //2

        while left < right: # left must be smaller than the right
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # since mid is not target, so +1
            elif nums[mid] > target:
                right = mid
            
            mid = (left + right)//2

        return mid
```

1. 基于 `07-lc-0704-binary-search.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么循环条件带等号？”*
  - **Candidate**: 闭区间下 $left == right$ 仍代表区间内包含 1 个有效待检元素。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 死循环 | left=mid 导致区间无法缩小 | 未加减 1 | 闭区间必须 left=mid+1 / right=mid-1 |

### Complete Dry-Run Table / 实例推演表

输入: `nums=[-1,0,3,5,9,12], target=9` -> mid=4 (val=9) -> return 4

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(\log n)$ | 每轮折半。 |
| **Space Complexity** | $O(1)$ | 常数级指针。 |
