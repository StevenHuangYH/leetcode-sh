# LC 0026: Remove Duplicates from Sorted Array | 删除有序数组中的重复项

- **LeetCode ID**: LC 0026
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 01: In-Place Two Pointers)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- **Solution File**: [`05-lc-0026-remove-duplicates-from-sorted-array.py`](luffy/05-lc-0026-remove-duplicates-from-sorted-array.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements.

### [CN] 中文描述
给你一个非递减序排列的整数数组 `nums` ，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。

### Constraints / 约束条件
1 <= nums.length <= 3 * 10^4, -100 <= nums[i] <= 100

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Two Pointer]`

```
┌────────────────────────────────────────────────────────┐
│ 快慢双指针: read 扫描，write 维护不重复前缀            │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
有序前缀无重复不变量：$nums[0...write]$ 中所有元素严格单调递增。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read=0
        write=0
        while read<len(nums):
            if nums[read]==nums[write]:
                read+=1
            else:
                write+=1
                nums[write]=nums[read]

        return write+1
```

1. 基于 `05-lc-0026-remove-duplicates-from-sorted-array.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何保留最多 k 个重复项？”*
  - **Candidate**: 比较条件改为 `nums[read] != nums[write - k]`。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 开辟新数组 | 违反原地 O(1) 空间要求 | 理解偏差 | 必须在 nums 上原地覆写 |

### Complete Dry-Run Table / 实例推演表

输入: `nums=[1,1,2]` -> write=1, nums=[1,2,2], return 2

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 读指针遍历数组一次。 |
| **Space Complexity** | $O(1)$ | 原地修改。 |
