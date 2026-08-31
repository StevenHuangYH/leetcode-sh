# LC 0209: Minimum Size Subarray Sum | 长度最小的子数组

- **LeetCode ID**: LC 0209
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 01: Sliding Window)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/minimum-size-subarray-sum/)
- **Solution File**: [`06-lc-0209-minimum-size-subarray-sum.py`](problems/luffy/06-lc-0209-minimum-size-subarray-sum.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0.

### [CN] 中文描述
给定一个含有 n 个正整数的数组和一个正整数 target 。找出该数组中满足其总和大于等于 target 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

### Constraints / 约束条件
1 <= target <= 10^9, 1 <= nums.length <= 10^5, 1 <= nums[i] <= 10^4

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Sliding Window]`

```
┌────────────────────────────────────────────────────────┐
│ 滑动窗口: 右移累加，和 >= target 时持续收缩左边界      │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
正整数单调性：窗口扩大和单调增加，窗口缩小和单调减少。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List

#sliding window 
#sum >= target?
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        fast = 0
        sum = 0
        min_len = float('inf')
        
        while fast < len(nums):
            sum += nums[fast]
            
            while sum >= target:
                min_len = min(min_len, fast - slow + 1)
                sum -= nums[slow]
                slow += 1
                
            fast += 1
            
        return min_len if min_len != float('inf') else 0
    
#note: 
# target has not yet met, move fast pointer to the right
# when target has met, move slow pointer to the right to find the minimum length of subarry
```

1. 基于 `06-lc-0209-minimum-size-subarray-sum.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“数组含负数时滑动窗口是否成立？”*
  - **Candidate**: 不成立，因和失去单调性，需改用前缀和 + 单调队列（LC 862）。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 初始值错误 | ans=0 导致 min 永远为 0 | 极值初始化错误 | 必须初始化为 inf |

### Complete Dry-Run Table / 实例推演表

输入: `target=7, nums=[2,3,1,2,4,3]` -> min len = 2 ([4,3])

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 每个元素进出窗口最多一次。 |
| **Space Complexity** | $O(1)$ | 仅维护指针和求和变量。 |
